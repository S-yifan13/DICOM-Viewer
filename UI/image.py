import numpy as np
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from matplotlib import pyplot as plt

from dicomUtil import Dicom

# 创建 QApplication 实例
app = QApplication([])

# 创建 QMainWindow 实例
window = QMainWindow()

# 创建 QLabel 实例
label_1 = QLabel(window)

# 假设您的数组 transverse_view 是一个 numpy 数组
# 这里使用随机生成的数组作为示例
dicom = Dicom("../data/data")
transverse_view = dicom.pixelCoronal()
# 将数组转换为 QByteArray

plt.imshow(transverse_view)
plt.show()
# 创建 QImage 对象，使用 QByteArray 数据初始化
image = QImage(transverse_view, transverse_view.shape[1], transverse_view.shape[0], QImage.Format_RGB888)

# 将 QImage 转换为 QPixmap
pixmap = QPixmap.fromImage(image)

# 将 QPixmap 设置为 QLabel 的 pixmap
label_1.setPixmap(pixmap)

# 在 QMainWindow 中添加 label_1
window.setCentralWidget(label_1)

# 显示 QMainWindow
window.show()

# 运行应用程序的事件循环
app.exec_()