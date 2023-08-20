import os
import shutil

import requests
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, cm

import config
from UI.progressDialog import Ui_progressDialog
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

from dicomUtil import Dicom
from pdfUtil import getStyle

pdfmetrics.registerFont(TTFont('SimSun', 'SimSun.ttf'))  #注册字体
styles = getSampleStyleSheet()
nidus_type = config.NIDUS_TYPE


def writeBasicInfo(dicom, pdf):
    patient = dicom.patient
    title = 'OCT Report'
    pdf.setFont("Helvetica-Bold", 20)
    pdf.drawString(100, 700, title)
    pdf.setFont("SimSun", 12)
    pdf.drawString(100, 680, '姓名：' + patient.name)
    pdf.drawString(500, 680, '性别：' + patient.sex)


class ReportThread(QtCore.QThread):
    progress_update = QtCore.pyqtSignal(float)
    progress_name = QtCore.pyqtSignal(str)

    def __init__(self, parent=None, pdf=None):
        super().__init__(parent)
        self.pdf = pdf

    # def getAllCheckResult(self, dicom):
    #     if os.path.exists(config.TEMP_CHECK_DIR):
    #         shutil.rmtree(config.TEMP_CHECK_DIR)
    #     os.mkdir(config.TEMP_CHECK_DIR)
    #     self.progress_name.emit('正在处理帧图像')
    #     self.progress_update.emit(0)
    #     dicom.frame2PngAll(config.TEMP_CHECK_DIR)
    #     print('store temp check image success')
    #     self.progress_update.emit(9)
    #
    #     self.progress_name.emit('正在检测')
    #     batch_size = config.CHECK_BATCH_SIZE
    #     batch = dicom.frame_count // batch_size + 1
    #     predictions = []
    #     for i in range(batch):
    #         size = batch_size
    #         if i == batch - 1:
    #             size = dicom.frame_count - i * batch_size
    #         files = []
    #         for j in range(batch_size * i, batch_size * i + size):
    #             temp_path = config.TEMP_CHECK_DIR + "{}.png".format(i)
    #             files.append(('image', open(temp_path, 'rb')))
    #         response = requests.post(config.CHECK_MODEL_URL, files=files)
    #         predictions += response.json()['predictions']
    #         print('get check prediction success' + str(i))
    #         self.progress_update.emit(9 + 40 * i / batch)
    #     self.progress_update.emit(49)
    #     return predictions

    def goThroughCheckResult(self, predictions, ratio=config.MIN_CHECK_SHOW_RATIO):
        result = []
        self.progress_name.emit('正在处理检测结果')
        for i in range(len(predictions)):
            prediction = predictions[i]
            problem = {
                'frame_index': i
            }
            for j in range(len(prediction)):
                problem[nidus_type[j]] = []
                for rect in prediction[nidus_type[j]]:
                    if rect[4] < ratio:
                        continue
                    problem[nidus_type[j]].append(rect)
            if len(problem['js']) + len(problem['kq']) + len(problem['xs']) > 0:
                result.append(problem)
        self.progress_update.emit(50)
        return result

    def generateReport(self, dicom, result):
        self.progress_name.emit('正在生成报告')

    def run(self):
        predictions = self.getAllCheckResult(self.dicom)
        result = self.goThroughCheckResult(predictions, config.MIN_CHECK_SHOW_RATIO)
        self.generateReport(self.dicom, result)




class ReportDialog(QDialog):
    def __init__(self, parent=None, output_path=None, dicom=None):
        super().__init__(parent)
        self.ui = Ui_progressDialog()
        if output_path is not None and os.path.exists(output_path):
            self.pdf = canvas.Canvas(output_path, pagesize='A4')
        else:
            self.pdf = None
        self.dicom = dicom
        self.thread = ReportThread(parent=self, pdf=self.pdf, dicom=dicom)


if __name__ == '__main__':
    dicom = Dicom('data/data')
    pdf = canvas.Canvas('output.pdf', pagesize='A4')
    writeBasicInfo(dicom, pdf)
    pdf.save()