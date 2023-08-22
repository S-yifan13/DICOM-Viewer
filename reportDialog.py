import os
import shutil

import requests
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, cm
from reportlab.platypus import SimpleDocTemplate

import config
from UI.mainWindow import Ui_MainWindow
from UI.progressDialog import Ui_progressDialog
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

from checkDialog import CheckDialog
from dicomUtil import Dicom
from pdfUtil import getStyle, createReport

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

    def __init__(self, parent=None, dicom=None, to_path=None, predictions=None):
        super().__init__(parent)
        self.predictions = predictions
        self.pdf = SimpleDocTemplate(to_path)
        self.dicom = dicom

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

    def generateReport(self, result):
        self.progress_name.emit('正在生成报告')
        createReport(result, self.pdf)

    def run(self):
        if self.predictions is None:
            if type(self.parent().parent()) is Ui_MainWindow:
                checkDialog = CheckDialog()
                checkDialog.show()
                checkDialog.start_check(self.dicom)
                self.predictions = checkDialog.getPredictions()
            else:
                self.progress_name.emit('请先调用检测和分割模型')
                self.progress_update.emit(-1)
                return
        result = self.goThroughCheckResult(self.dicom.predictions, config.MIN_CHECK_SHOW_RATIO)
        self.generateReport(result)


class ReportDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_progressDialog()
        self.thread = None
        self.ui.setupUi(self)

    def start_report(self, output_path=None, dicom=None, predictions=None):
        if output_path is not None:
            self.thread = ReportThread(parent=self, to_path=output_path, dicom=dicom, predictions=predictions)
            self.thread.progress_update.connect(self.update_progress)
            self.thread.progress_name.connect(self.update_label)
            self.thread.start()

    def update_progress(self, value):
        if value > 0:
            self.ui.setProgressBar(value)

    def update_label(self, value):
        self.ui.setLabel(value)


if __name__ == '__main__':
    dicom = Dicom('data/data')
    pdf = canvas.Canvas('output.pdf', pagesize='A4')
    writeBasicInfo(dicom, pdf)
    pdf.save()