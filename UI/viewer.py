# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewer.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1838, 983)
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
        self.label_7 = QtWidgets.QLabel(self.showControl)
        self.label_7.setStyleSheet("font-weight: bold; color:rgb(0, 0, 127);margin-top:5px")
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.firstControl = QtWidgets.QWidget(self.showControl)
        self.firstControl.setObjectName("firstControl")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.firstControl)
        self.horizontalLayout_4.setContentsMargins(5, 0, 5, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.checkBox = QtWidgets.QCheckBox(self.firstControl)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_4.addWidget(self.checkBox)
        self.firstColor = QtWidgets.QPushButton(self.firstControl)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.firstColor.sizePolicy().hasHeightForWidth())
        self.firstColor.setSizePolicy(sizePolicy)
        self.firstColor.setMinimumSize(QtCore.QSize(25, 0))
        self.firstColor.setMaximumSize(QtCore.QSize(25, 25))
        self.firstColor.setBaseSize(QtCore.QSize(0, 0))
        self.firstColor.setText("")
        self.firstColor.setObjectName("firstColor")
        self.horizontalLayout_4.addWidget(self.firstColor)
        self.verticalLayout.addWidget(self.firstControl)
        self.secondControl = QtWidgets.QWidget(self.showControl)
        self.secondControl.setObjectName("secondControl")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.secondControl)
        self.horizontalLayout_5.setContentsMargins(5, 0, 5, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.checkBox_5 = QtWidgets.QCheckBox(self.secondControl)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_5.sizePolicy().hasHeightForWidth())
        self.checkBox_5.setSizePolicy(sizePolicy)
        self.checkBox_5.setObjectName("checkBox_5")
        self.horizontalLayout_5.addWidget(self.checkBox_5)
        self.secondColor = QtWidgets.QPushButton(self.secondControl)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.secondColor.sizePolicy().hasHeightForWidth())
        self.secondColor.setSizePolicy(sizePolicy)
        self.secondColor.setMinimumSize(QtCore.QSize(25, 0))
        self.secondColor.setMaximumSize(QtCore.QSize(25, 25))
        self.secondColor.setBaseSize(QtCore.QSize(0, 0))
        self.secondColor.setText("")
        self.secondColor.setObjectName("secondColor")
        self.horizontalLayout_5.addWidget(self.secondColor)
        self.verticalLayout.addWidget(self.secondControl)
        self.thirdControl = QtWidgets.QWidget(self.showControl)
        self.thirdControl.setObjectName("thirdControl")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.thirdControl)
        self.horizontalLayout_6.setContentsMargins(5, 0, 5, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.checkBox_6 = QtWidgets.QCheckBox(self.thirdControl)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_6.sizePolicy().hasHeightForWidth())
        self.checkBox_6.setSizePolicy(sizePolicy)
        self.checkBox_6.setObjectName("checkBox_6")
        self.horizontalLayout_6.addWidget(self.checkBox_6)
        self.pushButton_5 = QtWidgets.QPushButton(self.thirdControl)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setMinimumSize(QtCore.QSize(25, 0))
        self.pushButton_5.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_5.setBaseSize(QtCore.QSize(0, 0))
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_6.addWidget(self.pushButton_5)
        self.verticalLayout.addWidget(self.thirdControl)
        self.show_nidus_name = QtWidgets.QCheckBox(self.showControl)
        self.show_nidus_name.setStyleSheet("margin-left: 19px; margin-top: 2px")
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
        self.ratio.setText("")
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
        self.setRatio = QtWidgets.QPushButton(self.widget_7)
        self.setRatio.setObjectName("setRatio")
        self.horizontalLayout_10.addWidget(self.setRatio)
        self.verticalLayout.addWidget(self.widget_7)
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
        self.radioButton = QtWidgets.QRadioButton(self.modelChoose)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout_2.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.modelChoose)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout_2.addWidget(self.radioButton_2)
        self.pushButton_2 = QtWidgets.QPushButton(self.modelChoose)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.Info = QtWidgets.QFrame(self.centralwidget)
        self.Info.setGeometry(QtCore.QRect(1560, 30, 261, 891))
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
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem3)
        self.gridLayout.addWidget(self.coronal, 1, 1, 1, 1)
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
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem4)
        self.label_23 = QtWidgets.QLabel(self.frame_7)
        self.label_23.setText("")
        self.label_23.setObjectName("label_23")
        self.verticalLayout_6.addWidget(self.label_23)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem5)
        self.gridLayout.addWidget(self.frame_7, 1, 0, 1, 1)
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
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem6)
        self.sImage = QtWidgets.QLabel(self.sagittal)
        self.sImage.setMaximumSize(QtCore.QSize(615, 420))
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
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem7)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem8)
        self.gridLayout.addWidget(self.sagittal, 0, 1, 1, 1)
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
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem9)
        self.tImage = QtWidgets.QLabel(self.transverse)
        self.tImage.setMaximumSize(QtCore.QSize(615, 350))
        self.tImage.setText("")
        self.tImage.setObjectName("tImage")
        self.verticalLayout_4.addWidget(self.tImage)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem10)
        self.gridLayout.addWidget(self.transverse, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1838, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.importFile = QtWidgets.QAction(MainWindow)
        self.importFile.setObjectName("importFile")
        self.exportFile = QtWidgets.QAction(MainWindow)
        self.exportFile.setObjectName("exportFile")
        self.uploadFile = QtWidgets.QAction(MainWindow)
        self.uploadFile.setObjectName("uploadFile")
        self.menu.addAction(self.importFile)
        self.menu.addAction(self.exportFile)
        self.menu.addAction(self.uploadFile)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "显示控制区"))
        self.label_7.setText(_translate("MainWindow", "检测结果病灶显示："))
        self.checkBox.setText(_translate("MainWindow", "第一类病灶"))
        self.checkBox_5.setText(_translate("MainWindow", "第二类病灶"))
        self.checkBox_6.setText(_translate("MainWindow", "第三类病灶"))
        self.checkBox_2.setText(_translate("MainWindow", "显示病灶名称"))
        self.label_9.setText(_translate("MainWindow", "置信度"))
        self.setRatio.setText(_translate("MainWindow", "设置置信度"))
        self.label_2.setText(_translate("MainWindow", "病灶透明度"))
        self.label_3.setText(_translate("MainWindow", "病灶颜色"))
        self.colorPickerTrigger.setText(_translate("MainWindow", "选择颜色"))
        self.label_4.setText(_translate("MainWindow", "当前帧数"))
        self.pushButton.setText(_translate("MainWindow", "跳转到帧"))
        self.label_5.setText(_translate("MainWindow", "模型选择区"))
        self.radioButton.setText(_translate("MainWindow", "检测算法"))
        self.radioButton_2.setText(_translate("MainWindow", "分割算法"))
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
