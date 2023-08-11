import sys
from PyQt5.QtGui import QPixmap, QPainter, QPen, QColor, QImage
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QColorDialog, QPushButton

from dicomUtil import Dicom

class ImageLabel(QLabel):
    def showCurrentImage(self, pixel_array):
        # 显示当前帧
        height, width, channel = pixel_array.shape
        bytes_per_line = 3 * width
        image = QImage(pixel_array.data, width, height, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(image)
        # self.setPixmap(pixmap.scaled(self.size(), aspectRatioMode=Qt.KeepAspectRatio))
        self.setPixmap(pixmap)

    def showCheckPrediction(self):
        # 获取当前的 QPixmap
        color = QColorDialog.getColor()
        pixmap = self.pixmap()

        # 在 QPixmap 上绘制矩形
        painter = QPainter(pixmap)
        pen = QPen(color)
        painter.setPen(pen)
        painter.drawRect(10, 10, 100, 100)
        painter.end()

        # 更新 QLabel 显示的 QPixmap
        self.setPixmap(pixmap)

class MainWindow(QMainWindow):
    def __init__(self, pixel_array):
        super().__init__()
        self.initUI(pixel_array)

    def initUI(self, pixel_array):
        # 创建 QLabel
        self.label = ImageLabel(self)
        self.setCentralWidget(self.label)

        # 设置初始的 QPixmap
        height, width, channel = pixel_array.shape
        bytes_per_line = 3 * width
        image = QImage(pixel_array.data, width, height, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(image)
        self.label.setPixmap(pixmap)
        self.button = QPushButton('1', self)
        self.setGeometry(100, 100, 300, 300)
        self.setWindowTitle('叠加矩形')
        self.show()

        self.button.clicked.connect(self.label.showCheckPrediction)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    dicom = Dicom("../data/oct_8_Apr_2022_04-23-56")
    pixel_array = dicom.pixelTransverse(300)

    mainWindow = MainWindow(pixel_array)
    sys.exit(app.exec_())
