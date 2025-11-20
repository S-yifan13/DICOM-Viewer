import requests
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtWidgets import QApplication, QTableWidget, QHeaderView

import config

columns = ['FID', 'PID', 'PName', 'PAge', 'PSex', 'PBirthday', 'FModality',
           'FInstitution', 'FPart', 'FTime', 'FFile']

columns_name = ['文件ID', '病人ID', '姓名', '年龄', '性别', '生日', '文件类型',
                '检查机构', '检查部位', '检查时间', '文件路径(ctrl+单击可进行下载)']


def getAllDicom():
    url = config.BACKEND_BASE_URL + '/allDicom'
    response = requests.get(url)
    if response.status_code != 200 or response.json()['errno'] != 200:
        return None
    return response.json()['data']


class SearchDialog(QtWidgets.QDialog):
    def cell_clicked(self, row, column):
        modifiers = QApplication.keyboardModifiers()
        if modifiers == Qt.ControlModifier and column == len(columns) - 1:
            # 获取网址单元格的文本
            item = self.table.item(row, column)
            url = config.BACKEND_BASE_URL + '/' + item.text()
            # 使用默认浏览器打开网址
            QDesktopServices.openUrl(QUrl(url))

    def __init__(self, table_data, parent=None):
        super().__init__(parent)
        self.table = QtWidgets.QTableWidget()
        self.table.setRowCount(len(table_data))
        self.table.setColumnCount(len(table_data[0]))
        self.table.setHorizontalHeaderLabels(columns_name)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.resizeColumnsToContents()
        for i, row in enumerate(table_data):
            for j in range(len(row)):
                self.table.setItem(i, j, QtWidgets.QTableWidgetItem(str(row[columns[j]])))

        self.table.cellClicked.connect(self.cell_clicked)
        self.widget = QtWidgets.QWidget()
        self.horizen_layout = QtWidgets.QHBoxLayout(self.widget)
        self.search_edit = QtWidgets.QLineEdit()
        self.search_edit.setPlaceholderText("请输入关键词")
        self.search_edit.returnPressed.connect(self.search_table)
        self.search_edit.setClearButtonEnabled(True)
        self.search_edit.setFixedSize(400, 30)
        self.search_button = QtWidgets.QPushButton("搜索")
        self.search_button.setFixedSize(50, 30)
        self.search_button.clicked.connect(self.search_table)
        self.horizen_layout.addWidget(self.search_edit)
        self.horizen_layout.addWidget(self.search_button)
        self.horizen_layout.setAlignment(Qt.AlignLeft)

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.widget)
        layout.addWidget(self.table)

        self.setGeometry(100, 100, 1300, 600)
        self.setWindowTitle("Table Example")
        self.show()

    def search_table(self):
        keyword = self.search_edit.text().strip().lower()

        for row in range(self.table.rowCount()):
            found = False
            for col in range(self.table.columnCount()):
                item = self.table.item(row, col)
                if item is not None and keyword in item.text().lower():
                    found = True
                    break
            self.table.setRowHidden(row, not found)


