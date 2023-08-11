from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QApplication, QMainWindow, QVBoxLayout, QWidget, QCheckBox
from PyQt5.QtGui import QImage, QPixmap, QPen, QPainter
import numpy as np


class ImageLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.draw_box = False
        self.box_color = Qt.red
        self.setScaledContents(True)
        pixmap = QPixmap('../temp/data.png')
        self.setPixmap(pixmap)

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.draw_box:
            painter = QPainter(self)
            pen = QPen(self.box_color)
            painter.setPen(pen)
            painter.drawRect(10, 10, 100, 100)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Drawing Example")

        self.image_label = ImageLabel()
        self.setCentralWidget(QWidget())
        layout = QVBoxLayout(self.centralWidget())
        self.checkbox = QCheckBox("显示方框")
        self.checkbox.stateChanged.connect(self.toggleDrawBox)
        layout.addWidget(self.checkbox)
        layout.addWidget(self.image_label)



    def toggleDrawBox(self, state):
        if state == Qt.Checked:
            self.image_label.draw_box = True
        else:
            self.image_label.draw_box = False
        self.image_label.update()


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.setGeometry(500, 200, 400, 300)
    window.show()
    app.exec_()
