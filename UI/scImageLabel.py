from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen, QImage, QPixmap
from PyQt5.QtWidgets import QLabel, QSizePolicy


class SCImageLabel(QLabel):
    def __init__(self, parent=None, show_line=True):
        super().__init__(parent)
        # 设置初始的缩放级别
        self.scale_factor = 1.0
        self.frame_index = 0
        self.total_frame = 0
        self.showLine = show_line

    def showCertainImage(self, pixel_array):
        self.setScaledContents(True)
        height, width, channel = pixel_array.shape
        bytes_per_line = channel * width
        color_format = QImage.Format_RGB888
        if channel == 4:
            color_format = QImage.Format_ARGB32
        image = QImage(pixel_array, width, height, bytes_per_line, color_format)
        pixmap = QPixmap.fromImage(image)
        self.setPixmap(pixmap.scaled(pixmap.size() * self.scale_factor, aspectRatioMode=Qt.KeepAspectRatio))

    def getX(self):
        if self.frame_index >= 0 and self.total_frame > 0:
            return (self.frame_index + 1) / self.total_frame * self.width()
        return 0

    def drawOneLine(self, painter):
        if self.frame_index >= 0 and self.total_frame > 0:
            painter.setPen(QPen(Qt.white, 1))
            x = self.getX()
            painter.drawLine(round(x), 0, round(x), self.height())

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        self.drawOneLine(painter)

    def setFrameIndex(self, frame_index):
        self.frame_index = frame_index
        self.update()

    def setTotalFrame(self, total_frame):
        self.total_frame = total_frame
        self.setFrameIndex(0)

    def setScale(self, scale):
        self.scale_factor = scale

    def getPixmapPainted(self):
        pixmap = self.pixmap()
        painter = QPainter(pixmap)
        if self.showLine:
            self.drawOneLine(painter)
        return pixmap

