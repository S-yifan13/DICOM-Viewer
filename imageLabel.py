from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QApplication
from PyQt5.QtGui import QImage, QPixmap, QPen, QPainter
import numpy as np

class ImageLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.frames = []
        self.frame_index = 0
        self.setScaledContents(True)
        self.slider = None
        self.label = None

    def wheelEvent(self, event):
        frame_count = self.frames.shape[0]
        if frame_count > 0:
            # 垂直方向上的滚动量
            delta = event.angleDelta().y() // 120
            self.frame_index += delta
            self.frame_index = max(0, min(self.frame_index, frame_count - 1))
            self.showCurrentImage()
            self.update()

    def showCurrentImage(self):
        # 显示当前帧
        if 0 <= self.frame_index < self.frames.shape[0]:
            pixel_array = self.frames[self.frame_index]
            height, width, channel = pixel_array.shape
            bytes_per_line = 3 * width
            image = QImage(pixel_array.data, width, height, bytes_per_line, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(image)
            # self.setPixmap(pixmap.scaled(self.size(), aspectRatioMode=Qt.KeepAspectRatio))
            self.setPixmap(pixmap)

        elif self.frame_index < 0:
            self.frame_index = 0
            self.showCurrentImage()
            self.update()

        else:
            self.frame_index = self.frames.shape[0] - 1
            self.showCurrentImage()
            self.update()

    def update(self):
        if self.slider is not None:
            self.slider.setValue(self.frame_index)
        if self.label is not None:
            self.label.setText(str(self.frame_index + 1))

    def setSlider(self, slider, max_value):
        self.slider = slider
        self.slider.setRange(0, max_value - 1)
        self.slider.valueChanged.connect(self.setFrameIndex)

    def setLabel(self, label):
        self.label = label
        self.label.setText(str(self.frame_index + 1))

    def setFrameIndex(self, frame_index):
        self.frame_index = frame_index
        self.update()
        self.showCurrentImage()

    def showCheckPrediction(self, prediction, color):
        pen = QPen(color)
        pixmap = self.pixmap().copy()
        painter = QPainter(pixmap)
        painter.setPen(pen)
        painter.drawRect(10, 10, 100, 100)
        painter.end()
        self.setPixmap(pixmap)
