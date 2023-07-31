import os
import pydicom
from matplotlib import pyplot as plt
import cv2

def importFile(file_path):
    # 在此处编写导入文件的操作代码
    # 例如，读取文件内容，进行相应处理等
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    return None


# 读取DICOM文件
dicom_file = pydicom.dcmread("data\data")
regions = dicom_file.SequenceOfUltrasoundRegions
print(regions[0])
print(regions[1])
print(regions[2])

# 获取像素数据和元数据
pixel_array = dicom_file.pixel_array

# 提取横断面、纵断面和斜视图像
# Region1 Location Max Y1 = 575
# Region1 Location Max X1 = 799, Min X1 = 224
transverse_view = pixel_array[0, :575, :, 0]
sagittal_view = pixel_array[:, :575, 512, 0].transpose(1, 0)
coronal_view = pixel_array[:, 285, 224:799, 0].transpose(1, 0)

# Region3 Location Y: 800-1023, X: 0-1021
# 纵断面和斜视图像需要调整横纵坐标
y = 1023 - 800 + 1
x = 1021 - 0 + 1
sagittal_view_resized = cv2.resize(sagittal_view, (x, y))
coronal_view_resized = cv2.resize(coronal_view, (x, y))

# 绘制横断面视图
plt.imshow(transverse_view, cmap='copper')
plt.title("Transverse View")
plt.show()

# 绘制纵断面视图
plt.imshow(sagittal_view_resized, cmap='copper')
plt.title("Sagittal View")
plt.show()

# 绘制斜视图
plt.imshow(coronal_view_resized, cmap='copper')
plt.title("Coronal View")
plt.show()