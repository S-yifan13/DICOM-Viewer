from PyQt5 import QtCore
from PyQt5.QtCore import QRect, QSize, Qt
from PyQt5.QtGui import QPen, QPainter
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QCheckBox, QSizePolicy, QPushButton, QColorDialog


class Ui_CheckColorWidget(object):
    def setupUi(self, check_color_widget, check_box_text):
        # check_color_widget.setObjectName(name)
        self.horizontalLayout = QHBoxLayout(check_color_widget)
        self.horizontalLayout.setContentsMargins(5, 0, 5, 0)
        self.checkBox = QCheckBox(check_color_widget)
        self.checkBox.setText(check_box_text)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy)
        self.horizontalLayout.addWidget(self.checkBox)
        self.pushButton = QPushButton(check_color_widget)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum,QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QSize(25, 25))
        self.pushButton.setMaximumSize(QSize(25, 25))
        self.pushButton.setBaseSize(QSize(0, 0))
        self.pushButton.setText("")
        self.horizontalLayout.addWidget(self.pushButton)

        QtCore.QMetaObject.connectSlotsByName(check_color_widget)


class CheckColorWidget(QWidget):
    def __init__(self, parent=None, check_box_text="", tImage=None):
        super().__init__(parent)
        self.ui = Ui_CheckColorWidget()
        self.ui.setupUi(self, check_box_text)
        self.tImage = tImage
        self.prediction = None
        self.color = Qt.white
        self.ui.pushButton.clicked.connect(self.chooseColor)
        self.ui.checkBox.stateChanged.connect(self.checkChange)

    def setPrediction(self, prediction):
        self.prediction = prediction

    def chooseColor(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.ui.pushButton.setStyleSheet("background-color: rgb({},{},{});".format(color.red(), color.green(), color.blue()))
            self.color = color

    def setPrediction(self, prediction):
        self.prediction = prediction

    def setTImage(self, tImage):
        self.tImage = tImage

    def checkChange(self):
        if self.ui.checkBox.isChecked() and self.prediction is not None:
            self.tImage.showCheckPrediction(self.prediction, self.color)
            pen = QPen(self.color)
            pixmap = self.tImage.pixmap()
            painter = QPainter(pixmap)
            painter.setPen(pen)
            painter.drawRect(10, 10, 100, 100)
            painter.end()
            self.tImage.setPixmap(pixmap)
