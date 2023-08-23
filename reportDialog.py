
from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog
from reportlab.platypus import SimpleDocTemplate, Paragraph

import config
from UI.progressDialog import Ui_progressDialog
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from pdfUtil import getStyle

pdfmetrics.registerFont(TTFont('SimSun', 'SimSun.ttf'))  #注册字体
styles = getSampleStyleSheet()
nidus_type = config.NIDUS_TYPE
seg_nidus = config.NIDUS_SEG


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

    def __init__(self, parent=None, to_path=None, check_predictions=None, seg_predictions=None):
        super().__init__(parent)
        self.pdf = SimpleDocTemplate(to_path)
        self.check_predictions = check_predictions
        self.seg_predictions = seg_predictions

    def goThroughPrediction(self, ratio=config.MIN_CHECK_SHOW_RATIO):
        result = []
        self.progress_name.emit('正在处理检测结果')
        nidus_check_contain,  nidus_seg_contain = [False, False, False], [False, False, False]
        for i in range(len(self.check_predictions)):
            problem = {
                'frame_index': i,
                'nidus_type': ''
            }
            prediction = self.check_predictions[i]
            for j in range(len(prediction)):
                for rect in prediction[nidus_type[j]]:
                    if rect[4] < ratio:
                        continue
                    problem['nidus_type'] += (nidus_type[j] + ',')
                    if nidus_check_contain[j] is False:
                        nidus_check_contain[j] = True
                    break

            prediction = self.seg_predictions[i]
            for j in range(len(prediction)):
                if len(prediction[str(j + 1)]) > 0:
                    problem['nidus_type'] += (seg_nidus[j] + ',')
                    if nidus_seg_contain[j] is False:
                        nidus_seg_contain[j] = True

            if problem['nidus_type'] != '':
                problem['nidus_type'] = problem['nidus_type'][:-1]
                result.append(problem)

            self.progress_update.emit((i + 1) / len(self.check_predictions) * 50)

        summary = ''
        for i in range(len(nidus_check_contain)):
            if nidus_check_contain[i]:
                summary += nidus_type[i] + ','
        for i in range(len(nidus_seg_contain)):
            if nidus_seg_contain[i]:
                summary += seg_nidus[i] + ','
        if summary != '':
            summary = summary[:-1]
            summary = '该患者数据中检测到{}等病灶。具体如下:'.format(summary)
        else:
            summary = '该患者数据中未检测到病灶。'
        self.progress_update.emit(50)
        return summary, result

    def generateReport(self, summary, result):
        self.progress_name.emit('正在生成报告')
        paragraph_normal, paragraph_bold, title_style = getStyle()
        contents = [Paragraph('OCT Report', title_style),
                    Paragraph(summary, paragraph_normal)]
        for r in result:
            subtitle = '帧_' + str(r['frame_index']) + ':{' + r['nidus_type'] + '}'
            contents.append(Paragraph(subtitle, paragraph_normal))
            self.progress_update.emit(min(50 + r['frame_index'] / len(result) * 50, 99))
        self.pdf.build(contents)
        self.progress_update.emit(100)

    def run(self):
        if self.check_predictions is None or self.seg_predictions is None:
            self.progress_name.emit('请先调用检测和分割模型')
            self.progress_update.emit(-1)
            return
        summary, result = self.goThroughPrediction()
        self.generateReport(summary, result)


class ReportDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_progressDialog()
        self.thread = None
        self.ui.setupUi(self)

    def start_report(self, output_path=None, check_predictions=None, seg_predictions=None):
        if output_path is not None:
            self.thread = ReportThread(self, output_path, check_predictions, seg_predictions)
            self.thread.progress_update.connect(self.update_progress)
            self.thread.progress_name.connect(self.update_label)
            self.thread.start()

    def update_progress(self, value):
        if value > 0:
            self.ui.setProgressBar(value)

    def update_label(self, value):
        self.ui.setLabel(value)


if __name__ == '__main__':
    check_file = open('data/predictions_check.txt', 'r')
    check_predictions = eval(check_file.read())
    check_file.close()
    seg_file = open('data/predictions_seg.txt', 'r')
    seg_predictions = eval(seg_file.read())
    seg_file.close()
    dialog = ReportDialog()
    dialog.show()
    dialog.start_report('data/report.pdf', check_predictions, seg_predictions)
    dialog.exec_()