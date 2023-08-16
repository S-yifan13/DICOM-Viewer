from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTransform, QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget


class ZoomableLabel(QLabel):
    def __init__(self):
        super().__init__()
        # 设置初始的缩放级别
        self.scale_factor = 1.0

    def wheelEvent(self, event):
        # 获取鼠标滚轮的滚动方向
        delta = event.angleDelta().y()

        # 根据滚动方向进行缩放
        if delta > 0:
            self.zoom(1.1)
        else:
            self.zoom(0.9)

    def zoom(self, scale_factor):
        # 限制缩放级别的上下限
        min_scale = 0.1
        max_scale = 10.0
        new_scale_factor = self.scale_factor * scale_factor
        new_scale_factor = max(min(new_scale_factor, max_scale), min_scale)

        # 更新缩放级别
        self.scale_factor = new_scale_factor

        # 获取当前的 pixmap
        current_pixmap = self.pixmap()

        if current_pixmap is not None:
            # 进行缩放
            scaled_pixmap = current_pixmap.transformed(QTransform().scale(new_scale_factor, new_scale_factor),
                                                       Qt.SmoothTransformation)

            # 设置缩放后的 pixmap
            self.setPixmap(scaled_pixmap)


if __name__ == '__main__':
    app = QApplication([])

    # 创建一个QWidget作为主窗口
    window = QWidget()

    # 创建一个ZoomableLabel用于显示图片并响应滚轮事件
    label = ZoomableLabel()

    # 加载原始图片
    pixmap = QPixmap('../temp/data.png')

    # 设置初始的pixmap
    label.setPixmap(pixmap)

    # 创建一个垂直布局，并将 ZoomableLabel 添加到其中
    layout = QVBoxLayout()
    layout.addWidget(label)

    # 设置主窗口的布局
    window.setLayout(layout)

    # 显示主窗口
    window.show()

    app.exec_()
