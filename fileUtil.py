import os
import pydicom
from matplotlib import pyplot as plt
import cv2

from dicomUtil import Dicom


def importFile(file_path):
    # 在此处编写导入文件的操作代码
    # 例如，读取文件内容，进行相应处理等
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    return None

#
# # 读取DICOM文件
# dicom_file = pydicom.dcmread("data\data")
#
# # 获取像素数据和元数据
# pixel_array = dicom_file.pixel_array
#
# # 提取横断面、纵断面和斜视图像
# # Region1 Location Max Y1 = 575
# # Region1 Location Max X1 = 799, Min X1 = 224
# transverse_view = pixel_array[0, :575, :, :]
# sagittal_view = pixel_array[:, :575, 512, :].transpose(1, 0, 2)
# coronal_view = pixel_array[:, 285, 224:799, :].transpose(1, 0, 2)
#
# # Region3 Location Y: 800-1023, X: 0-1021
# # 纵断面和斜视图像需要调整横纵坐标
# y = 1023 - 800 + 1
# x = 1021 - 0 + 1
# sagittal_view_resized = cv2.resize(sagittal_view, (x, y))
# coronal_view_resized = cv2.resize(coronal_view, (x, y))

dicom = Dicom("data/data")
transverse_view = dicom.pixelTransverse(0)
sagittal_view_resized = dicom.pixelSagittal()
coronal_view_resized = dicom.pixelCoronal()
# 绘制横断面视图
plt.imshow(transverse_view)
plt.title("Transverse View")
plt.show()

# 绘制纵断面视图
plt.imshow(sagittal_view_resized)
plt.title("Sagittal View")
plt.show()

# 绘制斜视图
plt.imshow(coronal_view_resized)
plt.title("Coronal View")
plt.show()