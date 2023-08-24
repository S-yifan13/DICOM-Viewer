import numpy as np
import math
import cv2

from dicomUtil import Dicom

# PAI值
PI = math.pi
def create_line_image(img):
    height, width, channel = img.shape
    circle_radius = int(height / 2)
    circle_center = [height / 2, width / 2]
    # 极坐标转换后图像的高
    line_height = int(circle_radius)
    # 极坐标转换后图像的宽，一般是原来圆形的周长
    line_width = int(2 * circle_radius * PI)
    # 建立展开后的图像
    line_image = np.zeros((line_height, line_width, channel), dtype=np.uint8)
    # 按照圆的极坐标赋值
    for row in range(line_image.shape[0]):
        for col in range(line_image.shape[1]):
            # 角度，最后的-0.1是用于优化结果，可以自行调整
            theta = PI * 2 / line_width * (col + 1) - 0.2
            # 半径，减1防止超界
            rho = circle_radius - row - 1

            x = int(circle_center[0] + rho * math.cos(theta) + 0.0)
            y = int(circle_center[1] - rho * math.sin(theta) + 0.0)

            # 赋值
            line_image[row, col, :] = img[y, x, :]
    # 如果想改变输出图像方向，旋转就行了
    # line_image = cv2.rotate(line_image, cv2.ROTATE_90_CLOCKWISE)
    return line_image

#  极坐标转换为直角坐标
def polar2xy(r, theta, radius):
    theta = theta / 180 * math.pi
    x = r * math.cos(theta) + radius
    y = radius - r * math.sin(theta)
    return x, y

def getDiameterPixel(img, diameter, theta):
    height, width, channel = img.shape
    radius = int(height / 2)
    for i in range(-radius, radius):
        x, y = polar2xy(i, theta, radius)
        x = int(x)
        y = int(y)
        if 0 <= x < width and 0 <= y < height:
            diameter[i + radius] = img[y, x]
        else:
            diameter[i + radius] = np.array([0, 0, 0])


def getLongitudinal(pixel_array, theta, ratio, left_start=0):
    new_width, height, width, channel = pixel_array.shape
    longitudinal_view = np.zeros((new_width, height, channel), dtype=np.uint8)
    for index in range(len(pixel_array)):
        img = pixel_array[index][:, left_start:left_start + height, :]
        getDiameterPixel(img, longitudinal_view[index], theta)
    longitudinal_view = longitudinal_view.transpose(1, 0, 2)
    longitudinal_view = cv2.resize(longitudinal_view, (int(height * ratio), height))
    return longitudinal_view

def showImage(img):
    cv2.imshow("longitudinal", img)
    cv2.waitKey()
    cv2.destroyAllWindows()
    cv2.imwrite("temp/l.png", img)


def test_polar(img_path):
    # 读取图像
    img = cv2.imread(img_path)
    if img is None:
        print("please check image path")
        return
    # 图像重置为固定大小
    print(img.shape)

    # 展示原图
    cv2.imshow("src", img)
    output = create_line_image(img)
    print(output.shape)
    # 展示结果
    cv2.imshow("dst", output)
    cv2.waitKey()
    cv2.destroyAllWindows()
    cv2.imwrite("temp/0.png", output)

def test_longitudinal():
    dicom = Dicom('data/data')
    pixel_array = dicom.pixelAllTransverseRect()
    theta = 45
    ratio = dicom.longitudinalWidth / dicom.longitudinalHeight
    img = getLongitudinal(pixel_array, theta, ratio)
    showImage(img)


if __name__ == '__main__':
    # 输入图像路径
    # img_path = "temp/check/0.png"
    # test_polar(img_path)
    test_longitudinal()
