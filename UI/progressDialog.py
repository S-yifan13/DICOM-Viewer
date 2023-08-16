from PyQt5 import QtCore, QtWidgets


class Ui_progressDialog(object):

    def setupUi(self, progress_dialog):
        progress_dialog.setObjectName("progressDialog")
        progress_dialog.resize(428, 200)
        self.horizontalLayout = QtWidgets.QHBoxLayout(progress_dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(20, -1, 20, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(progress_dialog)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.progressBar = QtWidgets.QProgressBar(progress_dialog)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout)

        QtCore.QMetaObject.connectSlotsByName(progress_dialog)

    def setLabel(self, text):
        self.label.setText(text)

    def setProgressBar(self, value):
        self.progressBar.setValue(value)

    def setProgressBarStyle(self, style):
        self.progressBar.setStyleSheet(style)