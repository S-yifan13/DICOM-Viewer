import cv2
import numpy as np
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from matplotlib import pyplot as plt

from dicomUtil import Dicom
from PIL import Image

dicom = Dicom("../data/data")
sagittal_view = dicom.pixelSagittal()
# image = Image.fromarray(sagittal_view)
# print(image.mode)
# # cv2
# sagittal_view_cvt = cv2.cvtColor(sagittal_view, cv2.COLOR_RGB2BGR)
# cv2.imwrite('trans.png', sagittal_view_cvt)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# # plt
# plt.imshow(sagittal_view)
# plt.show()

# PyQt5
app = QApplication([])
window = QMainWindow()
label_1 = QLabel(window)
height, width, channel = sagittal_view.shape
bytes_per_line = 3 * width
image = QImage(sagittal_view, width,
               height, bytes_per_line, QImage.Format_RGB888)
pixmap = QPixmap.fromImage(image)
label_1.setPixmap(pixmap)
window.setCentralWidget(label_1)
window.show()
app.exec_()


# app = QApplication([])
# window = QMainWindow()
# label_1 = QLabel(window)
# image = QImage(sagittal_view, sagittal_view.shape[1],
#                 sagittal_view.shape[0], QImage.Format_RGB888)
# pixmap = QPixmap.fromImage(image)
# label_1.setPixmap(pixmap)
# window.setCentralWidget(label_1)
# window.show()
# app.exec_()

# image = Image.open('sagittal.png')
#
# min_r, max_r = image.getextrema()[0][:2]
# min_g, max_g = image.getextrema()[1][:2]
# min_b, max_b = image.getextrema()[2][:2]
# print("Red channel range: {} - {}".format(min_r, max_r))
# print("Green channel range: {} - {}".format(min_g, max_g))
# print("Blue channel range: {} - {}".format(min_b, max_b))
#
# # 打印图片的尺寸
# width, height = image.size
# print("Image size: {} x {}".format(width, height))
#
# # 打印图片的通道顺序
# mode = image.mode
# print("Image mode: {}".format(mode))
# image = image.convert('RGBA')
# image.save('sagittal4.png', 'PNG')