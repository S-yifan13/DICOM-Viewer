import cv2
import numpy as np
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from matplotlib import pyplot as plt
import nibabel as nib
from dicomUtil import Dicom
from PIL import Image

result = nib.load("../data/result.nii")
image_data = result.get_fdata()
header = result.header
print(header)
print(image_data.shape)
plt.imshow(image_data[:, :, 15], cmap='gray', alpha=0.5)
plt.show()

# # PyQt5
# app = QApplication([])
# window = QMainWindow()
# label_1 = QLabel(window)
# height, width, channel = sagittal_view.shape
# bytes_per_line = 3 * width
# image = QImage(sagittal_view, width,
#                height, bytes_per_line, QImage.Format_RGB888)
# pixmap = QPixmap.fromImage(image)
# label_1.setPixmap(pixmap)
# window.setCentralWidget(label_1)
# window.show()
# app.exec_()


