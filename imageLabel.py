from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QApplication
from PyQt5.QtGui import QImage, QPixmap, QPen, QPainter
import numpy as np

from config import MIN_CHECK_SHOW_RATIO


class ImageLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.draw_check = [False, False, False]
        self.check_color = [Qt.white, Qt.white, Qt.white]
        self.predictions = None
        self.frames = []
        self.frame_index = 0
        self.setScaledContents(True)
        self.slider = None
        self.label = None
        self.scale = 1

    def wheelEvent(self, event):
        frame_count = self.frames.shape[0]
        if frame_count > 0:
            # 垂直方向上的滚动量
            delta = event.angleDelta().y() // 120
            self.frame_index += delta
            self.frame_index = max(0, min(self.frame_index, frame_count - 1))
            self.showCurrentImage()
            self.updateFrame()

    def showCurrentImage(self):
        # 显示当前帧
        if 0 <= self.frame_index < self.frames.shape[0]:
            pixel_array = self.frames[self.frame_index]
            height, width, channel = pixel_array.shape
            bytes_per_line = 3 * width
            image = QImage(pixel_array.data, width, height, bytes_per_line, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(image)
            self.setPixmap(pixmap.scaled(pixmap.size() * self.scale, aspectRatioMode=Qt.KeepAspectRatio))

        elif self.frame_index < 0:
            self.frame_index = 0
            self.showCurrentImage()
            self.updateFrame()

        else:
            self.frame_index = self.frames.shape[0] - 1
            self.showCurrentImage()
            self.updateFrame()

    def updateFrame(self):
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
        self.updateFrame()
        self.showCurrentImage()

    def showCheckPrediction(self, i):
        self.draw_check[i] = True
        self.update()

    def hideCheckPrediction(self, i):
        self.draw_check[i] = False
        self.update()

    def setColor(self, i, color):
        self.check_color[i] = color
        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.predictions is not None:
            for i in range(3):
                if self.draw_check[i]:
                    prediction = self.predictions[i]
                    self.drawRect(prediction, self.check_color[i])
                    # painter.drawRect(10, 10, 100, 100)

    def drawRect(self, prediction, color):
        painter = QPainter(self)
        pen = QPen(color)
        painter.setPen(pen)
        i = 0
        for rect in prediction:
            if i >= 5:
                break
            i += 1
            # if rect[4] < MIN_CHECK_SHOW_RATIO:
            #     continue
            left_top_x = rect[0] * self.scale
            left_top_y = rect[1] * self.scale
            right_bottom_x = rect[2] * self.scale
            right_bottom_y = rect[3] * self.scale
            width = right_bottom_x - left_top_x
            height = right_bottom_y - left_top_y
            painter.drawRect(int(left_top_x), int(left_top_y), int(width), int(height))

    def setPredictions(self, predictions):
        self.predictions = predictions
