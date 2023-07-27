from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget, QColorDialog, QLabel
from PyQt5.QtGui import QColor


class ColorPickerWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.button = QPushButton('选择颜色', self)
        self.button.clicked.connect(self.open_color_picker)

        self.color_label = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.color_label)
        self.setLayout(layout)

    def open_color_picker(self):
        color = QColorDialog.getColor()

        if color.isValid():
            # 在 Label 上显示选择的颜色
            self.color_label.setStyleSheet(f'background-color: {color.name()}')


if __name__ == '__main__':
    app = QApplication([])
    widget = ColorPickerWidget()
    widget.show()
    app.exec_()
