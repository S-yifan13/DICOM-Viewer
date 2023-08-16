from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal, QThread, QMetaObject, QCoreApplication
import os
import requests
from config import *

from UI.progressDialog import Ui_progressDialog


class CheckThread(QThread):
    progress_update = pyqtSignal(float)

    def __init__(self, frame_index, dicom=None):
        super().__init__()
        self.frame_index = frame_index
        self.dicom = dicom
        self.predictions = None

    def getCheckPredictionByIndex(self, frame_index, dicom):
        # 保存图片
        self.progress_update.emit(0)
        temp_path = os.path.join(TEMP_DIR, "frame_{}.png".format(frame_index))
        dicom.frame2Png(frame_index, temp_path)
        image = open(temp_path, 'rb')
        files = {'image': image}
        self.progress_update.emit(50)
        try:
            response = requests.post(CHECK_MODEL_URL, files=files)
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


    def run(self):
        if self.dicom is None or self.frame_index is None:
            self.progress_update.emit(-2)
        if self.getCheckPredictionByIndex(self.frame_index, self.dicom):
            self.progress_update.emit(100)
        else:
            self.progress_update.emit(-1)


class CheckDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.thread = None
        self.ui = Ui_progressDialog()
        self.ui.setupUi(self)

    def update_progress(self, value):
        if value == -2:
            self.ui.setLabel('未导入dicom文件或未指定帧')
        elif value == -1:
            self.ui.setLabel('请求错误')
        elif value == 0:
            self.ui.setLabel('检测中，请耐心等待...')
        elif value == 50:
            self.ui.setLabel('检测中，请耐心等待...')
            self.ui.setProgressBar(50)
        elif value == 100:
            self.ui.setLabel('检测完成')
            self.ui.setProgressBar(100)

    def start_check(self, dicom, frame_index):
        self.thread = CheckThread(frame_index, dicom)
        self.thread.progress_update.connect(self.update_progress)
        self.thread.finished.connect(self.check_finished)
        self.thread.start()

    def check_finished(self):
        print("check finished")

    def getPredictions(self):
        return self.thread.predictions
