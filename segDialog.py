import os

import requests
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QDialog

import config
from UI.progressDialog import Ui_progressDialog
from dicomUtil import Dicom


class SegThread(QThread):
    progress_update = pyqtSignal(float)

    def __init__(self, parent=None, dicom=None):
        super().__init__(parent)
        self.dicom = dicom
        self.predictions = None

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
        self.getSegResult(self.dicom, 0)


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

    def start_seg(self, dicom):
        self.thread = SegThread(self, dicom)
        self.thread.progress_update.connect(self.update_progress)
        # self.thread.progress_name.connect(self.update_label)
        # self.thread.check_finished.connect(self.close)
        self.thread.start()

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    dialog = SegDialog()
    dialog.show()
    dialog.start_seg(Dicom('data/data'))
    app.exec_()