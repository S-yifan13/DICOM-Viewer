# -*- coding: utf-8 -*-
from imageLabel import ImageLabel
# Form implementation generated from reading ui file 'viewer.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QColorDialog

from dicomUtil import Dicom


def showCertainImage(label, pixel_array):
    label.setScaledContents(True)
    height, width, channel = pixel_array.shape
    bytes_per_line = 3 * width
    image = QImage(pixel_array, width, height, bytes_per_line, QImage.Format_RGB888)
    pixmap = QPixmap.fromImage(image)
    label.setPixmap(pixmap)


class Ui_MainWindow(object):
    def __init__(self):
        self.dicomFile = None

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
        self.showControl.setGeometry(QtCore.QRect(30, 30, 191, 441))
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
        self.checkBox = QtWidgets.QCheckBox(self.showControl)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.showControl)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout.addWidget(self.checkBox_2)
        self.label_2 = QtWidgets.QLabel(self.showControl)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalSlider = QtWidgets.QSlider(self.showControl)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalLayout.addWidget(self.horizontalSlider)
        self.label_3 = QtWidgets.QLabel(self.showControl)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.widget = QtWidgets.QWidget(self.showControl)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.colorPickerTrigger = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorPickerTrigger.sizePolicy().hasHeightForWidth())
        self.colorPickerTrigger.setSizePolicy(sizePolicy)
        self.colorPickerTrigger.setObjectName("colorPickerTrigger")
        self.horizontalLayout.addWidget(self.colorPickerTrigger)
        self.colorLabel = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorLabel.sizePolicy().hasHeightForWidth())
        self.colorLabel.setSizePolicy(sizePolicy)
        self.colorLabel.setMinimumSize(QtCore.QSize(25, 25))
        self.colorLabel.setMaximumSize(QtCore.QSize(25, 25))
        self.colorLabel.setText("")
        self.colorLabel.setObjectName("colorLabel")
        self.horizontalLayout.addWidget(self.colorLabel)
        self.verticalLayout.addWidget(self.widget)
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
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.modelChoose = QtWidgets.QFrame(self.centralwidget)
        self.modelChoose.setGeometry(QtCore.QRect(30, 500, 201, 421))
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
        self.radioButton = QtWidgets.QRadioButton(self.modelChoose)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout_2.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.modelChoose)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout_2.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.modelChoose)
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout_2.addWidget(self.radioButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.modelChoose)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
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
        self.label_18 = QtWidgets.QLabel(self.transverse)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        self.label_18.setStyleSheet("color:rgb(255, 255, 255);font-weight: bold; font-size: 15;")
        self.label_18.setObjectName("label_18")
        self.verticalLayout_4.addWidget(self.label_18)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        # self.tImage = QtWidgets.QLabel(self.transverse)
        self.tImage = ImageLabel(self.transverse)
        self.tImage.setMaximumSize(QtCore.QSize(615, 350))
        self.tImage.setText("")
        self.tImage.setObjectName("tImage")
        self.verticalLayout_4.addWidget(self.tImage)
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
        self.label_20 = QtWidgets.QLabel(self.sagittal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        self.label_20.setStyleSheet("color:rgb(255, 255, 255);font-weight: bold; font-size: 15;")
        self.label_20.setObjectName("label_20")
        self.verticalLayout_5.addWidget(self.label_20)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem5)
        self.sImage = QtWidgets.QLabel(self.sagittal)
        self.sImage.setMaximumSize(QtCore.QSize(615, 350))
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
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem6)
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
        self.label_24 = QtWidgets.QLabel(self.coronal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy)
        self.label_24.setStyleSheet("color:rgb(255, 255, 255);font-weight: bold; font-size: 15;")
        self.label_24.setObjectName("label_24")
        self.verticalLayout_7.addWidget(self.label_24)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem9)
        self.cImage = QtWidgets.QLabel(self.coronal)
        self.cImage.setMaximumSize(QtCore.QSize(615, 200))
        self.cImage.setText("")
        self.cImage.setObjectName("cImage")
        self.verticalLayout_7.addWidget(self.cImage)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem10)
        self.gridLayout.addWidget(self.coronal, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
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
        self.menu.addAction(self.importFile)
        self.menu.addAction(self.exportFile)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.colorPickerTrigger.clicked.connect(self.clickColorPickerTrigger)  # 颜色选择器
        self.pushButton.clicked.connect(self.toFrame)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def clickColorPickerTrigger(self):
        color = QColorDialog.getColor()
        if color.isValid():
            # 在 Label 上显示选择的颜色
            self.colorLabel.setStyleSheet(f'background-color: {color.name()}')

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

    def showImage(self, dicomFile):
        self.frameIndexSpinBox.setRange(1, dicomFile.frame_count)
        self.tImage.frames = dicomFile.pixelAllTransverse()
        self.tImage.setSlider(self.frameIndexSlider, dicomFile.frame_count)
        self.tImage.showCurrentImage()
        self.tImage.setLabel(self.frameIndexLable)
        showCertainImage(self.sImage, dicomFile.pixelSagittal())
        showCertainImage(self.cImage, dicomFile.pixelCoronal())

    def toFrame(self):
        if self.dicomFile:
            self.tImage.setFrameIndex(self.frameIndexSpinBox.value())

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
        self.checkBox.setText(_translate("MainWindow", "显示病灶"))
        self.checkBox_2.setText(_translate("MainWindow", "显示病灶名称"))
        self.label_2.setText(_translate("MainWindow", "病灶透明度"))
        self.label_3.setText(_translate("MainWindow", "病灶颜色"))
        self.colorPickerTrigger.setText(_translate("MainWindow", "选择颜色"))
        self.label_4.setText(_translate("MainWindow", "当前帧数"))
        self.pushButton.setText(_translate("MainWindow", "跳转到帧"))
        self.label_5.setText(_translate("MainWindow", "模型选择区"))
        self.radioButton.setText(_translate("MainWindow", "模型1"))
        self.radioButton_2.setText(_translate("MainWindow", "模型2"))
        self.radioButton_3.setText(_translate("MainWindow", "模型3"))
        self.pushButton_2.setText(_translate("MainWindow", "确定调用"))
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
        self.label_18.setText(_translate("MainWindow", "轴位面 Transverse View"))
        self.label_20.setText(_translate("MainWindow", "矢状面 Sagittal View"))
        self.label_24.setText(_translate("MainWindow", "冠状面 Coronal View"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.importFile.setText(_translate("MainWindow", "导入"))
        self.exportFile.setText(_translate("MainWindow", "导出"))
