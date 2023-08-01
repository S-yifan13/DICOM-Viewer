from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QApplication
from PyQt5.QtGui import QImage, QPixmap
import numpy as np

class ImageLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.frames = []
        self.frame_index = 0
        self.setScaledContents(True)

    def wheelEvent(self, event):
        frame_count = self.frames.shape[0]
        if frame_count > 0:
            # 垂直方向上的滚动量
            delta = event.angleDelta().y() // 120
            self.frame_index += delta
            self.frame_index = max(0, min(self.frame_index, frame_count - 1))
            self.showCurrentImage()

    def showCurrentImage(self):
        # 显示当前帧
        if self.frame_index < self.frames.shape[0]:
            pixel_array = self.frames[self.frame_index]
            height, width, channel = pixel_array.shape
            bytes_per_line = 3 * width
            image = QImage(pixel_array.data, width, height, bytes_per_line, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(image)
            # self.setPixmap(pixmap.scaled(self.size(), aspectRatioMode=Qt.KeepAspectRatio))
            self.setPixmap(pixmap)