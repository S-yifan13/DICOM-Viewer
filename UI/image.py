from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtGui import QPainter, QPixmap, QFont, QColor


class CustomLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)

        # 创建一个空的 pixmap
        self.pixmap = QPixmap(300, 200)
        self.pixmap.fill(Qt.white)

    def paintEvent(self, event):
        painter = QPainter(self.pixmap)

        # 清除 pixmap 内容
        self.pixmap.fill(Qt.white)

        # 设置字体
        font = QFont()
        font.setPointSize(14)
        painter.setFont(font)

        # 绘制矩形
        rectangle = self.rect()
        painter.drawRect(rectangle)

        # 在矩形的左上角显示文字
        textRectangle = rectangle.adjusted(10, 10, -10, -10)
        painter.drawText(textRectangle, Qt.AlignTop | Qt.AlignLeft, "Hello, World!")

        # 在标签上显示 pixmap
        self.setPixmap(self.pixmap)

        super().paintEvent(event)


# 测试
app = QApplication([])
label = CustomLabel()
label.show()
app.exec_()
