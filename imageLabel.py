from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QApplication
from PyQt5.QtGui import QImage, QPixmap, QPen, QPainter
import numpy as np

from config import MIN_CHECK_SHOW_RATIO

nidus_type = ['js', 'kq', 'xs']


def drawOneRect(painter, prediction, color, scale=1, left_start=0, top_start=0):
    pen = QPen(color)
    painter.setPen(pen)
    i = 0
    for rect in prediction:
        if i >= 5:
            break
        # if rect[4] < MIN_CHECK_SHOW_RATIO:
        #     continue
        i += 1
        left_top_x = (rect[0] + left_start) * scale
        left_top_y = (rect[1] + top_start) * scale
        width = (rect[2] - rect[0]) * scale
        height = (rect[3] - rect[1]) * scale
        painter.drawRect(int(left_top_x), int(left_top_y), int(width), int(height))
        # print('left_top_x: {}, left_top_y: {}, width: {}, height: {}'.format(left_top_x, left_top_y, width, height))


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
        self.left_start = 0
        self.top_start = 0
        self.s_label = None
        self.c_label = None

    def setSCLabel(self, s_label, c_label):
        self.s_label = s_label
        self.c_label = c_label

    def setFrames(self, frames):
        self.frames = frames
        self.frame_index = 0
        self.showCurrentImage()
        if self.s_label is not None:
            self.s_label.setTotalFrame(len(self.frames))
        if self.c_label is not None:
            self.c_label.setTotalFrame(len(self.frames))

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
        self.s_label.setFrameIndex(frame_index)
        self.c_label.setFrameIndex(frame_index)

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
        try:
            if self.predictions is not None:
                painter = QPainter(self)
                for i in range(3):
                    if self.draw_check[i]:
                        prediction = self.predictions[nidus_type[i]]
                        drawOneRect(painter, prediction, self.check_color[i], self.scale,
                                    left_start=self.left_start, top_start=self.top_start)
        except Exception as e:
            print(e)

    def setPredictions(self, predictions):
        self.predictions = predictions

    def setScale(self, scale):
        self.scale = scale

    def getPixmapPainted(self):
        pixmap = self.pixmap().copy()
        painter = QPainter(pixmap)
        if self.predictions is not None:
            for i in range(3):
                if self.draw_check[i]:
                    prediction = self.predictions[nidus_type[i]]
                    drawOneRect(painter, prediction, self.check_color[i], self.scale,
                                left_start=self.left_start, top_start=self.top_start)
        return pixmap

    def setStart(self, left_start, top_start):
        self.left_start = left_start
        self.top_start = top_start


