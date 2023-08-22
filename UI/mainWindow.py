# -*- coding: utf-8 -*-
import sys

import requests

from searchDialog import SearchDialog, getAllDicom
from UI.checkColorWidget import CheckColorWidget
from UI.imageViewer import ImageViewDialog
from UI.upload import UploadDialog
from checkDialog import CheckDialog
import config
from imageLabel import ImageLabel
# Form implementation generated from reading ui file 'viewer.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QColorDialog, QLabel

from dicomUtil import Dicom
from scImageLabel import SCImageLabel
from segDialog import SegDialog


def showCertainImage(label, pixel_array):
    label.setScaledContents(True)
    height, width, channel = pixel_array.shape
    bytes_per_line = 3 * width
    image = QImage(pixel_array, width, height, bytes_per_line, QImage.Format_RGB888)
    pixmap = QPixmap.fromImage(image)
    label.setPixmap(pixmap)

def imageView(image_label):
    imageViewer = ImageViewDialog()
    if type(image_label) is QPixmap:
        imageViewer.setPixmap(image_label)
    elif type(image_label) is QLabel:
        pixmap = image_label.pixmap().copy()
        imageViewer.setPixmap(pixmap)
    imageViewer.exec_()

class Ui_MainWindow(object):
    def __init__(self):
        self.dicomFile = None
        self.imageGenerate = True

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1835, 980)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setBaseSize(QtCore.QSize(615, 0))
        MainWindow.setToolTipDuration(-5)
        MainWindow.setStyleSheet("background-color: rgb(227, 227, 227);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.showControl = QtWidgets.QFrame(self.centralwidget)
        self.showControl.setGeometry(QtCore.QRect(20, 30, 211, 671))
        self.showControl.setStyleSheet("background-color: rgb(255,255,255);")
        self.showControl.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.showControl.setFrameShadow(QtWidgets.QFrame.Raised)
        self.showControl.setObjectName("showControl")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.showControl)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.showControl)
        self.label.setStyleSheet("fontsize: 15px; font-weight: bold")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_14 = QtWidgets.QLabel(self.showControl)
        self.label_14.setStyleSheet("font-weight: bold; color:rgb(0, 0, 127);margin-top:5px")
        self.label_14.setObjectName("label_14")
        self.verticalLayout.addWidget(self.label_14)
        self.widget_3 = QtWidgets.QWidget(self.showControl)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.widget_3)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.frameIndexLable = QtWidgets.QLabel(self.widget_3)
        self.frameIndexLable.setText("")
        self.frameIndexLable.setObjectName("frameIndexLable")
        self.horizontalLayout_3.addWidget(self.frameIndexLable)
        self.verticalLayout.addWidget(self.widget_3)
        self.widget_2 = QtWidgets.QWidget(self.showControl)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frameIndexSpinBox = QtWidgets.QSpinBox(self.widget_2)
        self.frameIndexSpinBox.setObjectName("frameIndexSpinBox")
        self.horizontalLayout_2.addWidget(self.frameIndexSpinBox)
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout.addWidget(self.widget_2)
        self.label_7 = QtWidgets.QLabel(self.showControl)
        self.label_7.setStyleSheet("font-weight: bold; color:rgb(0, 0, 127);margin-top:5px")
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)

        # 检测病灶显示控制
        self.firstControl = CheckColorWidget(self.showControl, '第一类病灶js', index=0)
        self.verticalLayout.addWidget(self.firstControl)
        self.secondControl = CheckColorWidget(self.showControl, '第二类病灶kq', index=1)
        self.verticalLayout.addWidget(self.secondControl)
        self.thirdControl = CheckColorWidget(self.showControl, '第三类病灶xs', index=2)
        self.verticalLayout.addWidget(self.thirdControl)

        self.show_nidus_name = QtWidgets.QCheckBox(self.showControl)
        self.show_nidus_name.setStyleSheet("margin-left: 15px; margin-top: 2px")
        self.show_nidus_name.setObjectName("show_nidus_name")
        self.verticalLayout.addWidget(self.show_nidus_name)
        self.widget_8 = QtWidgets.QWidget(self.showControl)
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_11.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_9 = QtWidgets.QLabel(self.widget_8)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_11.addWidget(self.label_9)
        self.ratio = QtWidgets.QLabel(self.widget_8)
        self.ratio.setText(str(config.MIN_CHECK_SHOW_RATIO))
        self.ratio.setObjectName("ratio")
        self.horizontalLayout_11.addWidget(self.ratio)
        self.verticalLayout.addWidget(self.widget_8)
        self.widget_7 = QtWidgets.QWidget(self.showControl)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.widget_7)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.horizontalLayout_10.addWidget(self.doubleSpinBox)
        self.setRatioButton = QtWidgets.QPushButton(self.widget_7)
        self.setRatioButton.setObjectName("setRatioButton")
        self.horizontalLayout_10.addWidget(self.setRatioButton)
        self.verticalLayout.addWidget(self.widget_7)
        self.label_10 = QtWidgets.QLabel(self.showControl)
        self.label_10.setStyleSheet("font-weight: bold; color:rgb(0, 0, 127);margin-top:5px")
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)

        self.segmentationControl = CheckColorWidget(self.showControl, '分割结果', index=3)
        self.verticalLayout.addWidget(self.segmentationControl)

        self.label_2 = QtWidgets.QLabel(self.showControl)
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet('margin-left: 15px;')
        self.verticalLayout.addWidget(self.label_2)
        self.alphaSlider = QtWidgets.QSlider(self.showControl)
        self.alphaSlider.setOrientation(QtCore.Qt.Horizontal)
        self.alphaSlider.setObjectName("alphaSlider")
        self.alphaSlider.setRange(0, 255)
        self.alphaSlider.setValue(255)
        self.alphaSlider.setStyleSheet('margin-left: 30px;')
        self.verticalLayout.addWidget(self.alphaSlider)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.modelChoose = QtWidgets.QFrame(self.centralwidget)
        self.modelChoose.setGeometry(QtCore.QRect(20, 710, 211, 211))
        self.modelChoose.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.modelChoose.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.modelChoose.setFrameShadow(QtWidgets.QFrame.Raised)
        self.modelChoose.setObjectName("modelChoose")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.modelChoose)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.modelChoose)
        self.label_5.setStyleSheet("fontsize: 15px; font-weight: bold")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.checkModel = QtWidgets.QRadioButton(self.modelChoose)
        self.checkModel.setObjectName("checkModel")
        self.verticalLayout_2.addWidget(self.checkModel)
        self.segmentationModel = QtWidgets.QRadioButton(self.modelChoose)
        self.segmentationModel.setObjectName("segmentationModel")
        self.verticalLayout_2.addWidget(self.segmentationModel)
        self.callModelButton = QtWidgets.QPushButton(self.modelChoose)
        self.callModelButton.setObjectName("callModelButton")
        self.verticalLayout_2.addWidget(self.callModelButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.Info = QtWidgets.QFrame(self.centralwidget)
        self.Info.setGeometry(QtCore.QRect(1560, 30, 261, 871))
        self.Info.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.Info.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Info.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Info.setObjectName("Info")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Info)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.Info)
        self.label_6.setStyleSheet("fontsize: 15px; font-weight: bold")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.pid = QtWidgets.QLabel(self.Info)
        self.pid.setObjectName("pid")
        self.verticalLayout_3.addWidget(self.pid)
        self.name = QtWidgets.QLabel(self.Info)
        self.name.setObjectName("name")
        self.verticalLayout_3.addWidget(self.name)
        self.sex = QtWidgets.QLabel(self.Info)
        self.sex.setObjectName("sex")
        self.verticalLayout_3.addWidget(self.sex)
        self.birthday = QtWidgets.QLabel(self.Info)
        self.birthday.setObjectName("birthday")
        self.verticalLayout_3.addWidget(self.birthday)
        self.age = QtWidgets.QLabel(self.Info)
        self.age.setObjectName("age")
        self.verticalLayout_3.addWidget(self.age)
        self.label_12 = QtWidgets.QLabel(self.Info)
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.verticalLayout_3.addWidget(self.label_12)
        self.label_13 = QtWidgets.QLabel(self.Info)
        self.label_13.setStyleSheet("fontsize: 15px; font-weight: bold")
        self.label_13.setObjectName("label_13")
        self.verticalLayout_3.addWidget(self.label_13)
        self.institution = QtWidgets.QLabel(self.Info)
        self.institution.setWordWrap(True)
        self.institution.setObjectName("institution")
        self.verticalLayout_3.addWidget(self.institution)
        self.part = QtWidgets.QLabel(self.Info)
        self.part.setObjectName("part")
        self.verticalLayout_3.addWidget(self.part)
        self.time = QtWidgets.QLabel(self.Info)
        self.time.setWordWrap(True)
        self.time.setObjectName("time")
        self.verticalLayout_3.addWidget(self.time)
        self.modality = QtWidgets.QLabel(self.Info)
        self.modality.setObjectName("modality")
        self.verticalLayout_3.addWidget(self.modality)
        self.frameNum = QtWidgets.QLabel(self.Info)
        self.frameNum.setObjectName("frameNum")
        self.verticalLayout_3.addWidget(self.frameNum)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.rhreeView = QtWidgets.QFrame(self.centralwidget)
        self.rhreeView.setGeometry(QtCore.QRect(240, 20, 1311, 911))
        self.rhreeView.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rhreeView.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rhreeView.setObjectName("rhreeView")
        self.gridLayout = QtWidgets.QGridLayout(self.rhreeView)
        self.gridLayout.setContentsMargins(11, -1, -1, -1)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.transverse = QtWidgets.QFrame(self.rhreeView)
        self.transverse.setAutoFillBackground(False)
        self.transverse.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.transverse.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.transverse.setFrameShadow(QtWidgets.QFrame.Raised)
        self.transverse.setObjectName("transverse")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.transverse)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_4 = QtWidgets.QWidget(self.transverse)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_7.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, 11)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_18 = QtWidgets.QLabel(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        self.label_18.setStyleSheet("color:rgb(255, 255, 255);font-weight: bold; font-size: 15;")
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_7.addWidget(self.label_18)
        self.viewTrans = QtWidgets.QPushButton(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.viewTrans.sizePolicy().hasHeightForWidth())
        self.viewTrans.setSizePolicy(sizePolicy)
        self.viewTrans.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.viewTrans.setStyleSheet("color: rgb(255, 255, 255);font-weight: bold; font-size: 15;")
        self.viewTrans.setObjectName("viewTrans")
        self.horizontalLayout_7.addWidget(self.viewTrans)
        self.verticalLayout_4.addWidget(self.widget_4)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        # self.tImage = QtWidgets.QLabel(self.transverse)
        self.tImage = ImageLabel(self.transverse)
        # self.tImage.setMaximumSize(QtCore.QSize(615, 350))
        self.tImage.setText("")
        self.tImage.setObjectName("tImage")
        self.verticalLayout_4.addWidget(self.tImage)
        self.firstControl.setTImage(self.tImage)
        self.secondControl.setTImage(self.tImage)
        self.thirdControl.setTImage(self.tImage)
        self.segmentationControl.setTImage(self.tImage)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem4)
        self.gridLayout.addWidget(self.transverse, 0, 0, 1, 1)
        self.sagittal = QtWidgets.QFrame(self.rhreeView)
        self.sagittal.setAutoFillBackground(False)
        self.sagittal.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.sagittal.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sagittal.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sagittal.setObjectName("sagittal")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.sagittal)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget_5 = QtWidgets.QWidget(self.sagittal)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, 11)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_20 = QtWidgets.QLabel(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        self.label_20.setStyleSheet("color:rgb(255, 255, 255);font-weight: bold; font-size: 15;")
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_8.addWidget(self.label_20)
        self.viewSagi = QtWidgets.QPushButton(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.viewSagi.sizePolicy().hasHeightForWidth())
        self.viewSagi.setSizePolicy(sizePolicy)
        self.viewSagi.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.viewSagi.setStyleSheet("color: rgb(255, 255, 255);font-weight: bold; font-size: 15;")
        self.viewSagi.setObjectName("viewSagi")
        self.horizontalLayout_8.addWidget(self.viewSagi)
        self.verticalLayout_5.addWidget(self.widget_5)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem11)
        self.sImage = SCImageLabel(self.sagittal)
        # self.sImage.setMaximumSize(QtCore.QSize(615, 420))
        self.sImage.setText("")
        self.sImage.setObjectName("sImage")
        self.verticalLayout_5.addWidget(self.sImage)
        self.frameIndexSlider = QtWidgets.QSlider(self.sagittal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameIndexSlider.sizePolicy().hasHeightForWidth())
        self.frameIndexSlider.setSizePolicy(sizePolicy)
        self.frameIndexSlider.setStyleSheet("")
        self.frameIndexSlider.setOrientation(QtCore.Qt.Horizontal)
        self.frameIndexSlider.setObjectName("frameIndexSlider")
        self.verticalLayout_5.addWidget(self.frameIndexSlider)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem12)
        self.gridLayout.addWidget(self.sagittal, 0, 1, 1, 1)
        self.frame_7 = QtWidgets.QFrame(self.rhreeView)
        self.frame_7.setAutoFillBackground(False)
        self.frame_7.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_22 = QtWidgets.QLabel(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)
        self.label_22.setStyleSheet("color:rgb(255, 255, 255);font-weight: bold; font-size: 15;")
        self.label_22.setText("")
        self.label_22.setObjectName("label_22")
        self.verticalLayout_6.addWidget(self.label_22)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem7)
        self.label_23 = QtWidgets.QLabel(self.frame_7)
        self.label_23.setText("")
        self.label_23.setObjectName("label_23")
        self.verticalLayout_6.addWidget(self.label_23)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem8)
        self.gridLayout.addWidget(self.frame_7, 1, 0, 1, 1)
        self.coronal = QtWidgets.QFrame(self.rhreeView)
        self.coronal.setAutoFillBackground(False)
        self.coronal.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.coronal.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.coronal.setFrameShadow(QtWidgets.QFrame.Raised)
        self.coronal.setObjectName("coronal")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.coronal)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.widget_6 = QtWidgets.QWidget(self.coronal)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_9.setContentsMargins(-1, 0, -1, 11)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_24 = QtWidgets.QLabel(self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy)
        self.label_24.setStyleSheet("color:rgb(255, 255, 255);font-weight: bold; font-size: 15;")
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_9.addWidget(self.label_24)
        self.viewCoro = QtWidgets.QPushButton(self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.viewCoro.sizePolicy().hasHeightForWidth())
        self.viewCoro.setSizePolicy(sizePolicy)
        self.viewCoro.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.viewCoro.setStyleSheet("color: rgb(255, 255, 255);font-weight: bold; font-size: 15;")
        self.viewCoro.setObjectName("viewCoro")
        self.horizontalLayout_9.addWidget(self.viewCoro)
        self.verticalLayout_7.addWidget(self.widget_6)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem9)
        self.cImage = SCImageLabel(self.coronal)
        # self.cImage.setMaximumSize(QtCore.QSize(615, 200))
        self.cImage.setText("")
        self.cImage.setObjectName("cImage")
        self.verticalLayout_7.addWidget(self.cImage)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem10)
        self.gridLayout.addWidget(self.coronal, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.tImage.setSCLabel(self.sImage, self.cImage)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1835, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.importFile = QtWidgets.QAction(MainWindow)
        self.importFile.setObjectName("importFile")
        self.importFile.triggered.connect(self.importFileAction)
        self.exportFile = QtWidgets.QAction(MainWindow)
        self.exportFile.setObjectName("exportFile")
        self.exportFile.triggered.connect(self.exportFileAction)
        self.uploadFile = QtWidgets.QAction(MainWindow)
        self.uploadFile.setObjectName("uploadFile")
        self.uploadFile.triggered.connect(self.uploadFileAction)
        self.searchFile = QtWidgets.QAction(MainWindow)
        self.searchFile.setObjectName("searchFile")
        self.searchFile.triggered.connect(self.searchFileAction)
        self.menu.addAction(self.importFile)
        self.menu.addAction(self.exportFile)
        self.menu.addAction(self.uploadFile)
        self.menu.addAction(self.searchFile)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.toFrame)
        self.callModelButton.clicked.connect(self.callModel)
        self.setRatioButton.clicked.connect(self.setRatio)

        self.viewSagi.clicked.connect(self.sagittalView)
        self.viewCoro.clicked.connect(self.coronalView)
        self.viewTrans.clicked.connect(self.transverseView)

        self.alphaSlider.valueChanged.connect(self.tImage.setAlpha)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def importFileAction(self):
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "选择文件", "", "All Files (*)")
        if file_path:
            print("选择的文件路径：", file_path)
            dicomFile = Dicom(file_path)
            self.dicomFile = dicomFile
            self.showInfo(dicomFile)
            self.showImage(dicomFile)

    def exportFileAction(self):
        pass

    def searchFileAction(self):
        table_data = getAllDicom()
        dialog = SearchDialog(table_data)
        dialog.exec_()

    def setRatio(self):
        config.MIN_CHECK_SHOW_RATIO = self.doubleSpinBox.value()
        self.ratio.setText(str(config.MIN_CHECK_SHOW_RATIO))
        self.tImage.update()

    def uploadFileAction(self):
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "选择文件", "", "All Files (*)")
        if file_path:
            print("选择的文件路径：", file_path)
            upload_dialog = UploadDialog()
            upload_dialog.start_upload(file_path=file_path, url='http://127.0.0.1:8000/api/storeDicom')
            upload_dialog.exec_()

    def showImage(self, dicomFile):
        scale = config.IMAGE_WIDTH / dicomFile.columns  # 宽度
        print("scale:", scale)
        self.tImage.setScale(scale)
        self.sImage.setScale(scale)
        self.cImage.setScale(scale)
        self.tImage.setFixedSize(config.IMAGE_WIDTH, dicomFile.transverseHeight * scale)
        self.sImage.setFixedSize(config.IMAGE_WIDTH, dicomFile.longitudinalHeight * scale)
        self.cImage.setFixedSize(config.IMAGE_WIDTH, dicomFile.longitudinalHeight * scale)
        self.frameIndexSpinBox.setRange(1, dicomFile.frame_count)
        self.tImage.setFrames(dicomFile.pixelAllTransverse())
        self.tImage.setSlider(self.frameIndexSlider, dicomFile.frame_count)
        self.tImage.setLabel(self.frameIndexLable)
        self.tImage.setStart(dicomFile.transverseMinX, dicomFile.transverseMinY)
        showCertainImage(self.sImage, dicomFile.pixelSagittal())
        showCertainImage(self.cImage, dicomFile.pixelCoronal())
        self.tImage.setShowNameCheckbox(self.show_nidus_name)

    def toFrame(self):
        if self.dicomFile:
            self.tImage.setFrameIndex(self.frameIndexSpinBox.value() - 1)

    def transverseView(self):
        imageView(self.tImage.getPixmapPainted())

    def sagittalView(self):
        imageView(self.sImage.getPixmapPainted())

    def coronalView(self):
        imageView(self.cImage.getPixmapPainted())

    def callCheckModel(self):
        if self.dicomFile is None:
            return
        checkDialog = CheckDialog()
        checkDialog.start_check(self.dicomFile, self.imageGenerate)
        checkDialog.exec_()
        self.tImage.setPredictions(checkDialog.getPredictions())

    def callSegModel(self):
        if self.dicomFile is None:
            return
        segDialog = SegDialog()
        segDialog.start_seg(self.dicomFile, self.imageGenerate)
        segDialog.exec_()
        self.tImage.setSegPrediction(segDialog.getPredictions())

    def callModel(self):
        if self.dicomFile is None:
            return
        if self.checkModel.isChecked():
            self.callCheckModel()
            self.imageGenerate = True

        elif self.segmentationModel.isChecked():
            self.callSegModel()
            self.imageGenerate = True

    def showInfo(self, dicomFile):
        patient = dicomFile.patient
        self.name.setText("姓名：" + patient.name)
        self.sex.setText("性别：" + patient.sex)
        self.age.setText("年龄:" + patient.age)
        self.pid.setText("id：" + patient.pid)
        self.birthday.setText("生日：" + patient.birthday)

        self.time.setText("检查时间：" + dicomFile.study_date)
        self.modality.setText("类型：" + dicomFile.modality)
        self.institution.setText("检查机构：" + dicomFile.institution_name)
        self.frameNum.setText("帧数：" + str(dicomFile.pixel_array.shape[0]))
        self.part.setText("检查部位：" + dicomFile.body_part_examined)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "显示控制区"))
        self.label_7.setText(_translate("MainWindow", "检测结果病灶显示："))
        self.label_10.setText(_translate("MainWindow", "分割结果病灶显示："))
        self.label_14.setText(_translate("MainWindow", "帧显示："))
        self.show_nidus_name.setText(_translate("MainWindow", "显示病灶名称"))
        self.label_9.setText(_translate("MainWindow", "置信度"))
        self.setRatioButton.setText(_translate("MainWindow", "设置置信度"))
        self.label_2.setText(_translate("MainWindow", "病灶透明度"))
        self.label_4.setText(_translate("MainWindow", "当前帧数"))
        self.pushButton.setText(_translate("MainWindow", "跳转到帧"))
        self.label_5.setText(_translate("MainWindow", "模型选择区"))
        self.checkModel.setText(_translate("MainWindow", "检测算法"))
        self.segmentationModel.setText(_translate("MainWindow", "分割算法"))
        self.callModelButton.setText(_translate("MainWindow", "确定调用"))
        self.label_6.setText(_translate("MainWindow", "病人信息"))
        self.pid.setText(_translate("MainWindow", "ID"))
        self.name.setText(_translate("MainWindow", "姓名"))
        self.sex.setText(_translate("MainWindow", "性别"))
        self.birthday.setText(_translate("MainWindow", "生日"))
        self.age.setText(_translate("MainWindow", "年龄"))
        self.label_13.setText(_translate("MainWindow", "文件信息"))
        self.institution.setText(_translate("MainWindow", "检查机构"))
        self.part.setText(_translate("MainWindow", "检查部位"))
        self.time.setText(_translate("MainWindow", "检查时间"))
        self.modality.setText(_translate("MainWindow", "类型"))
        self.frameNum.setText(_translate("MainWindow", "帧数"))
        self.label_24.setText(_translate("MainWindow", "冠状面 Coronal View"))
        self.viewCoro.setText(_translate("MainWindow", "点击查看"))
        self.label_20.setText(_translate("MainWindow", "矢状面 Sagittal View"))
        self.viewSagi.setText(_translate("MainWindow", "点击查看"))
        self.label_18.setText(_translate("MainWindow", "轴位面 Transverse View"))
        self.viewTrans.setText(_translate("MainWindow", "点击查看"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.importFile.setText(_translate("MainWindow", "导入"))
        self.exportFile.setText(_translate("MainWindow", "导出"))
        self.uploadFile.setText(_translate("MainWindow", "上传"))
        self.searchFile.setText(_translate("MainWindow", "查询"))
