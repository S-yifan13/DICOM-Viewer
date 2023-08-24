import os
import shutil

import requests
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QDialog

import config
from UI.progressDialog import Ui_progressDialog
from dicomUtil import Dicom


class SegThreadAll(QThread):
    progress_update = pyqtSignal(float)
    progress_name = pyqtSignal(str)
    seg_finished = pyqtSignal()

    def __init__(self, parent=None, dicom=None, generate=False):
        super().__init__(parent)
        self.dicom = dicom
        self.predictions = None
        self.generate = generate

    def frame2PngAll(self, target_path, progress_num=20):
        if self.dicom is not None:
            for i in range(self.dicom.pixel_array.shape[0]):
                self.dicom.frame2Png(i, target_path + str(i) + '.png')
                self.progress_update.emit(i / self.dicom.pixel_array.shape[0] * progress_num)

    def getSegResultAll(self, dicom):
        if not self.generate:
            self.progress_name.emit('正在处理帧图像...')
            self.progress_update.emit(0)
            if os.path.exists(config.TEMP_CHECK_DIR):
                shutil.rmtree(config.TEMP_CHECK_DIR)
            os.mkdir(config.TEMP_CHECK_DIR)
            self.frame2PngAll(config.TEMP_SEG_DIR)
            print('store temp seg image success')
            self.generate = True
        self.progress_update.emit(20)
        self.progress_name.emit('正在检测...')
        batch_size = config.SEG_BATCH_SIZE
        batch = dicom.frame_count // batch_size + 1
        predictions = []
        try:
            for i in range(batch):
                size = batch_size
                if i == batch - 1:
                    size = dicom.frame_count - i * batch_size
                files = []
                for j in range(batch_size * i, batch_size * i + size):
                    temp_path = config.TEMP_CHECK_DIR + "{}.png".format(j)
                    files.append(('image', open(temp_path, 'rb')))
                response = requests.post(config.SEGMENTATION_MODEL_URL, files=files)
                predictions += response.json()['predictions']
                print('get seg prediction success' + str(i))
                self.progress_update.emit(20 + 80 * i / batch)
            self.progress_update.emit(100)
            self.progress_name.emit('检测完成!')
            return predictions
        except requests.exceptions.RequestException as e:
            self.progress_update.emit(-1)
            self.progress_name.emit('请求错误')
            print(e)
            return False

    def getSegResult(self, dicom, frame_index):
        if dicom is None or frame_index < 0 or frame_index >= dicom.pixel_array.shape[0]:
            return None
        temp_path = os.path.join(config.TEMP_DIR, "frame_{}.png".format(frame_index))
        dicom.frame2Png(frame_index, temp_path)
        image = open(temp_path, 'rb')
        files = {'image': image}
        self.progress_update.emit(50)

        try:
            response = requests.post(config.SEGMENTATION_MODEL_URL, files=files)
            if response.status_code != 200:
                return False
            print('get seg prediction success')
            self.predictions = response.json()['predictions'][0]
            image.close()
            os.remove(temp_path)
            self.progress_update.emit(100)
            return True

        except requests.exceptions.RequestException as e:
            self.progress_update.emit(-1)
            print(e)
            image.close()
            os.remove(temp_path)
            return False

    def run(self):
        if self.dicom is None:
            self.progress_update.emit(-2)
            self.progress_name.emit('未导入dicom文件')
        else:
            self.predictions = self.getSegResultAll(self.dicom)
            self.seg_finished.emit()


class SegDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_progressDialog()
        self.ui.setupUi(self)
        self.thread = None

    def getPredictions(self):
        return self.thread.predictions

    def update_progress(self, value):
        if value > 0:
            self.ui.setProgressBar(value)

    def update_label(self, value):
        self.ui.setLabel(value)

    def start_seg(self, dicom, generate=False):
        self.thread = SegThreadAll(self, dicom, generate)
        self.thread.progress_update.connect(self.update_progress)
        self.thread.progress_name.connect(self.update_label)
        self.thread.seg_finished.connect(self.close)
        self.thread.start()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    dialog = SegDialog()
    dialog.show()
    dialog.start_seg(Dicom('data/oct_20_May_2022_14-16-51'), True)
    predictions = dialog.getPredictions()
    file = open('data/predictions.txt', 'w')
    file.write(str(predictions))
    app.exec_()