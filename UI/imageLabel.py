from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QImage, QPixmap, QPen, QPainter, QColor
import numpy as np
import config
from utils.polar import create_line_image, getLongitudinal, polar2xy

nidus_type = config.NIDUS_TYPE
seg_type = config.NIDUS_SEG
check_type = config.NIDUS_CHECK

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

def draw_seg_nidus(array, painter, color, scale=1, left_start=0, top_start=0):
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
        self.l_label = None
        self.draw_check = [False, False, False]
        self.check_color = [Qt.white, Qt.white, Qt.white, Qt.white, Qt.white, Qt.white]
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
        self.draw_seg = [False, False, False]
        self.p_label = None
        self.polar_show = False
        self.polar_checkbox = None
        self.model_info = None
        self.theta = 0
        self.longitudinalHeight = 0

    def setTheta(self, theta):
        self.theta = theta
        self.setLongitudinal()
        self.update()

    def setLongitudinal(self):
        if len(self.frames) == 0 or self.longitudinalHeight == 0:
            return
        scale = self.frames.shape[2] / self.longitudinalHeight
        longitudinal_view = getLongitudinal(self.frames, self.theta, scale, self.left_start)
        self.l_label.showCertainImage(longitudinal_view)

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

    def setSCPLLabel(self, s_label, c_label, p_label, l_label):
        self.s_label = s_label
        self.c_label = c_label
        self.p_label = p_label
        self.l_label = l_label

    def updatePLabel(self):
        if self.frames is None or len(self.frames) == 0:
            return
        pixmap = self.getPixmapPainted(False)
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
        if self.l_label is not None:
            self.l_label.setTotalFrame(len(self.frames))

    def setAlpha(self, value):
        for i in range(3, 6):
            if type(self.check_color[i]) is not QColor:
                color = QColor(self.check_color[3])
                color.setAlpha(value)
                self.check_color[i] = color
            else:
                self.check_color[i].setAlpha(value)
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
            self.changeModelInfo()

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
        self.l_label.setFrameIndex(frame_index)

    def setShowCheckPrediction(self, i, value):
        self.hidePolar()
        if 0 <= i < 3:
            self.draw_check[i] = value
            self.update()
        elif 3 <= i < 5:
            self.draw_seg[i-3] = value
            self.update()
        self.changeModelInfo()


    def setColor(self, i, color):
        self.hidePolar()
        self.check_color[i] = color
        self.update()

    def hidePolar(self):
        self.polar_show = False
        self.polar_checkbox.setChecked(False)
        self.p_label.setPixmap(QPixmap())

    def drawDiameter(self, painter):
        if self.frames is None or len(self.frames) == 0:
            return
        radius = self.frames.shape[1] // 2
        x1, y1 = polar2xy(radius, self.theta, radius)
        x2, y2 = polar2xy(-radius, self.theta, radius)
        x1 = (x1 + self.left_start) * self.scale
        y1 = (y1 + self.top_start) * self.scale
        x2 = (x2 + self.left_start) * self.scale
        y2 = (y2 + self.top_start) * self.scale
        pen = QPen(Qt.white)
        painter.setPen(pen)
        painter.drawLine(int(x1), int(y1), int(x2), int(y2))

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        self.drawDiameter(painter)
        if self.polar_show:
            self.updatePLabel()
        if self.check_predictions is not None:
            for i in range(3):
                text = check_type[i] if self.show_name else None
                if self.draw_check[i]:
                    prediction = self.check_predictions[self.frame_index][nidus_type[i]]
                    drawOneRect(painter, prediction, self.check_color[i], self.scale,
                                left_start=self.left_start, top_start=self.top_start,
                                text=text)

        if self.seg_predictions is not None:
            for i in range(3):
                if self.draw_seg[i]:
                    prediction = self.seg_predictions[self.frame_index][str(i + 1)]
                    draw_seg_nidus(prediction, painter, self.check_color[3], self.scale, self.left_start, self.top_start)

    def setCheckPredictions(self, predictions):
        self.check_predictions = predictions
        self.changeModelInfo()

    def setScale(self, scale):
        self.scale = scale

    def getPixmapPainted(self, show_line=True):
        pixmap = self.pixmap().copy()
        painter = QPainter(pixmap)
        if show_line:
            self.drawDiameter(painter)
        if self.check_predictions is not None:
            for i in range(3):
                text = check_type[i] if self.show_name else None
                if self.draw_check[i]:
                    prediction = self.check_predictions[self.frame_index][nidus_type[i]]
                    drawOneRect(painter, prediction, self.check_color[i], self.scale,
                                left_start=self.left_start, top_start=self.top_start,
                                text=text)
        if self.seg_predictions is not None:
            for i in range(3):
                if self.draw_seg[i]:
                    prediction = self.seg_predictions[self.frame_index][str(i + 1)]
                    draw_seg_nidus(prediction, painter, self.check_color[3], self.scale, self.left_start, self.top_start)

        return pixmap

    def setStart(self, left_start, top_start, left_end):
        self.left_start = left_start
        self.top_start = top_start
        self.left_end = left_end

    def changeModelInfo(self):
        if self.model_info is None:
            return
        string = '第' + str(self.frame_index) + '帧'
        if self.check_predictions is None and self.seg_predictions is None:
            self.model_info.setText(string + '未进行检测或分割')
        else:
            nidus_str = ''
            nidus_count = 0
            if self.check_predictions is not None:
                nidus_check = self.check_predictions[self.frame_index]
                for i in range(3):
                    count = 0
                    for k in nidus_check[nidus_type[i]]:
                        if k[4] > config.MIN_CHECK_SHOW_RATIO:
                            count += 1
                    if count > 0:
                        nidus_str += check_type[i] + ','
                        nidus_count += 1
            if self.seg_predictions is not None:
                nidus_seg = self.seg_predictions[self.frame_index]
                for i in range(3):
                    if len(nidus_seg[str(i + 1)]) > 0:
                        nidus_str += seg_type[i] + ','
                        nidus_count += 1
            if len(nidus_str) == 0:
                string += '未检测到病灶'
            else:
                string += '共检测到病灶{}种，类型包括：'.format(nidus_count) + nidus_str[:-1]
            self.model_info.setText(string)



