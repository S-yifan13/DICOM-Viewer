import shutil

from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal, QThread, QMetaObject, QCoreApplication
import os
import requests
import config

from UI.progressDialog import Ui_progressDialog
from dicomUtil import Dicom

class CheckThreadAll(QThread):
    progress_update = pyqtSignal(float)
    progress_name = pyqtSignal(str)
    check_finished = pyqtSignal()

    def __init__(self, dicom=None):
        super().__init__()
        self.dicom = dicom
        self.predictions = None

    def getCheckPredictionByIndex(self, frame_index, dicom):
        # 保存图片
        self.progress_update.emit(0)
        temp_path = os.path.join(config.TEMP_DIR, "frame_{}.png".format(frame_index))
        dicom.frame2Png(frame_index, temp_path)
        image = open(temp_path, 'rb')
        files = {'image': image}
        self.progress_update.emit(50)
        try:
            response = requests.post(config.CHECK_MODEL_URL, files=files)
            if response.status_code != 200:
                return False
            print('get check prediction success')
            self.predictions = response.json()['predictions'][0]
            image.close()
            os.remove(temp_path)
            return True

        except requests.exceptions.RequestException as e:
            self.progress_update.emit(-1)
            print(e)
            image.close()
            os.remove(temp_path)
            return False

    def frame2PngAll(self, target_path, progress_num=50):
        if self.dicom is not None:
            for i in range(self.dicom.pixel_array.shape[0]):
                self.dicom.frame2Png(i, target_path + str(i) + '.png')
                self.progress_update.emit(i / self.dicom.pixel_array.shape[0] * progress_num)

    def getAllCheckResult(self, dicom):
        if os.path.exists(config.TEMP_CHECK_DIR):
            shutil.rmtree(config.TEMP_CHECK_DIR)
        os.mkdir(config.TEMP_CHECK_DIR)
        self.progress_name.emit('正在处理帧图像...')
        self.progress_update.emit(0)
        self.frame2PngAll(config.TEMP_CHECK_DIR)
        print('store temp check image success')
        self.progress_update.emit(50)

        self.progress_name.emit('正在检测...')
        batch_size = config.CHECK_BATCH_SIZE
        batch = dicom.frame_count // batch_size + 1
        predictions = []
        try:
            for i in range(batch):
                size = batch_size
                if i == batch - 1:
                    size = dicom.frame_count - i * batch_size
                files = []
                for j in range(batch_size * i, batch_size * i + size):
                    temp_path = config.TEMP_CHECK_DIR + "{}.png".format(i)
                    files.append(('image', open(temp_path, 'rb')))
                response = requests.post(config.CHECK_MODEL_URL, files=files)
                predictions += response.json()['predictions']
                print('get check prediction success' + str(i))
                self.progress_update.emit(50 + 50 * i / batch)
                self.progress_update.emit(100)
                self.progress_name.emit('检测完成!')
                return predictions
        except requests.exceptions.RequestException as e:
            self.progress_update.emit(-1)
            self.progress_name.emit('请求错误')
            print(e)
            return False

    def run(self):
        if self.dicom is None:
            self.progress_update.emit(-2)
            self.progress_name.emit('未导入dicom文件')
        else:
            self.predictions = self.getAllCheckResult(self.dicom)
            self.check_finished.emit()

class CheckDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.thread = None
        self.ui = Ui_progressDialog()
        self.ui.setupUi(self)

    def update_progress(self, value):
        if value > 0:
            self.ui.setProgressBar(value)

    def update_label(self, value):
        self.ui.setLabel(value)

    def start_check(self, dicom):
        self.thread = CheckThreadAll(dicom)
        self.thread.progress_update.connect(self.update_progress)
        self.thread.progress_name.connect(self.update_label)
        self.thread.check_finished.connect(self.close)
        self.thread.start()

    def getPredictions(self):
        return self.thread.predictions


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    dialog = CheckDialog()
    dialog.show()
    dialog.start_check(Dicom('data/data'))
    app.exec_()
