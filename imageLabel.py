from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QApplication
from PyQt5.QtGui import QImage, QPixmap, QPen, QPainter, QColor
import numpy as np
import config
from polar import create_line_image

nidus_type = config.NIDUS_TYPE


def drawOneRect(painter, prediction, color, scale=1, left_start=0, top_start=0, text=None):
    pen = QPen(color)
    painter.setPen(pen)
    i = 0
    for rect in prediction:
        if i >= 5:
            break
        if rect[4] < config.MIN_CHECK_SHOW_RATIO:
            continue
        i += 1
        left_top_x = (rect[0] + left_start) * scale
        left_top_y = (rect[1] + top_start) * scale
        width = (rect[2] - rect[0]) * scale
        height = (rect[3] - rect[1]) * scale
        painter.drawRect(int(left_top_x), int(left_top_y), int(width), int(height))
        # print('left_top_x: {}, left_top_y: {}, width: {}, height: {}'.format(left_top_x, left_top_y, width, height))

        if text is not None and len(text) > 0:
            font = painter.font()
            font.setPointSize(10)
            painter.setFont(font)
            painter.drawText(int(left_top_x), int(left_top_y) - 3, text)

def draw_seg(array, painter, color, scale=1, left_start=0, top_start=0):
    pen = QPen(color)
    painter.setPen(pen)
    for point in array:
        x, y = point
        x = (x + left_start) * scale
        y = (y + top_start) * scale
        painter.drawPoint(int(x), int(y))

class ImageLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.draw_check = [False, False, False]
        self.check_color = [Qt.white, Qt.white, Qt.white, Qt.white]
        self.check_predictions = None
        self.frames = []
        self.frame_index = 0
        self.setScaledContents(True)
        self.slider = None
        self.label = None
        self.scale = 1
        self.left_start = 0
        self.left_end = 0
        self.top_start = 0
        self.s_label = None
        self.c_label = None
        self.show_name = False
        self.show_name_checkbox = None
        self.seg_predictions = None
        self.draw_seg = False
        self.p_label = None
        self.polar_show = False
        self.polar_checkbox = None

    def setSegPrediction(self, seg_predictions):
        self.seg_predictions = seg_predictions
        self.update()
    
    def setShowName(self, show_name):
        self.show_name = show_name
        self.update()

    def setPolarCheckbox(self, polar_checkbox):
        self.polar_checkbox = polar_checkbox
        polar_checkbox.stateChanged.connect(self.setPolarShow)

    def setPolarShow(self, value):
        if value == Qt.Unchecked:
            self.polar_show = False
        else:
            self.polar_show = True
        self.update()

    def setShowNameCheckbox(self, show_name_checkbox):
        self.show_name_checkbox = show_name_checkbox
        show_name_checkbox.stateChanged.connect(self.setShowName)

    def setSCPLabel(self, s_label, c_label, p_label):
        self.s_label = s_label
        self.c_label = c_label
        self.p_label = p_label

    def updatePLabel(self):
        if self.frames is None or len(self.frames) == 0:
            return
        pixmap = self.getPixmapPainted()
        pixmap = pixmap.scaled(pixmap.size() / self.scale, aspectRatioMode=Qt.KeepAspectRatio)
        image = pixmap.toImage()
        size = image.size()
        s = image.bits().asstring(size.width() * size.height() * image.depth() // 8)  # format 0xffRRGGBB
        arr = np.fromstring(s, dtype=np.uint8).reshape((size.height(), size.width(), image.depth() // 8))
        transverse_view = arr[:, self.left_start:self.left_end, :]
        polar_view = create_line_image(transverse_view)
        self.p_label.showCertainImage(polar_view)

    def setFrames(self, frames):
        self.frames = frames
        self.frame_index = 0
        self.showCurrentImage()
        if self.s_label is not None:
            self.s_label.setTotalFrame(len(self.frames))
        if self.c_label is not None:
            self.c_label.setTotalFrame(len(self.frames))

    def setAlpha(self, value):
        if type(self.check_color[3]) is not QColor:
            color = QColor(self.check_color[3])
            color.setAlpha(value)
            self.check_color[3] = color
        else:
            self.check_color[3].setAlpha(value)
        self.update()

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
            self.hidePolar()
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
        self.hidePolar()
        if 0 <= i < 3:
            self.draw_check[i] = True
            self.update()
        elif i == 3:
            self.draw_seg = True
            self.update()

    def hideCheckPrediction(self, i):
        self.hidePolar()
        if 0 <= i < 3:
            self.draw_check[i] = False
            self.update()
        elif i == 3:
            self.draw_seg = False
            self.update()

    def setColor(self, i, color):
        self.hidePolar()
        self.check_color[i] = color
        self.update()

    def hidePolar(self):
        self.polar_show = False
        self.polar_checkbox.setChecked(False)
        self.p_label.setPixmap(QPixmap())

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        if self.polar_show:
            self.updatePLabel()
        if self.check_predictions is not None:
            for i in range(3):
                text = nidus_type[i] if self.show_name else None
                if self.draw_check[i]:
                    prediction = self.check_predictions[self.frame_index][nidus_type[i]]
                    drawOneRect(painter, prediction, self.check_color[i], self.scale,
                                left_start=self.left_start, top_start=self.top_start,
                                text=text)

        if self.seg_predictions is not None and self.draw_seg:
            prediction = self.seg_predictions[self.frame_index]
            draw_seg(prediction, painter, self.check_color[3], self.scale, self.left_start, self.top_start)

    def setPredictions(self, predictions):
        self.check_predictions = predictions

    def setScale(self, scale):
        self.scale = scale

    def getPixmapPainted(self):
        pixmap = self.pixmap().copy()
        painter = QPainter(pixmap)
        if self.check_predictions is not None:
            for i in range(3):
                text = nidus_type[i] if self.show_name else None
                if self.draw_check[i]:
                    prediction = self.check_predictions[self.frame_index][nidus_type[i]]
                    drawOneRect(painter, prediction, self.check_color[i], self.scale,
                                left_start=self.left_start, top_start=self.top_start,
                                text=text)
        if self.seg_predictions is not None and self.draw_seg:
            prediction = self.seg_predictions[self.frame_index]
            draw_seg(prediction, painter, self.check_color[3], self.scale, self.left_start, self.top_start)

        return pixmap

    def setStart(self, left_start, top_start, left_end):
        self.left_start = left_start
        self.top_start = top_start
        self.left_end = left_end
