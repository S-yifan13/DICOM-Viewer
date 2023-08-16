from PyQt5 import QtWidgets, QtCore

class TableDialog(QtWidgets.QDialog):
    def __init__(self, table_data, parent=None):
        super().__init__(parent)
        self.table = QtWidgets.QTableWidget()
        self.table.setRowCount(len(table_data))
        self.table.setColumnCount(len(table_data[0]))
        self.table.setHorizontalHeaderLabels(["ID", "Name", "Age"])

        for i, row in enumerate(table_data):
            for j, item in enumerate(row):
                self.table.setItem(i, j, QtWidgets.QTableWidgetItem(str(item)))

        self.search_edit = QtWidgets.QLineEdit()
        self.search_button = QtWidgets.QPushButton("Search")
        self.search_button.clicked.connect(self.search_table)

        self.sort_button = QtWidgets.QPushButton("Sort")
        self.sort_button.clicked.connect(self.sort_table)

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.search_edit)
        layout.addWidget(self.search_button)
        layout.addWidget(self.sort_button)
        layout.addWidget(self.table)

        self.setGeometry(100, 100, 400, 300)
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

    def sort_table(self):
        self.table.sortItems()

# 测试对话框
table_data = [
    [3, "Bob", 30],
    [1, "John", 20],
    [2, "Jane", 25]
]

app = QtWidgets.QApplication([])
dialog = TableDialog(table_data)
app.exec_()
