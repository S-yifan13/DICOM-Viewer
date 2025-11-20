import requests
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPainter, QPen
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

from utils.dicomUtil import Dicom
temp_path = '../temp/data.png'


dicom = Dicom("../data/oct_8_Apr_2022_04-23-56")
dicom.frame2Png(63, temp_path)
files = [('image', open(temp_path, 'rb')),
         ('image', open(temp_path, 'rb'))]
response = requests.post(url='http://10.212.253.234:8611/predict', files=files)
print(response.json()['predictions'])
prediction = response.json()['predictions'][0]
nidus_type = ['js', 'kq', 'xs']

# # PyQt5
app = QApplication([])
window = QMainWindow()
label = QLabel(window)
pixmap = QPixmap(temp_path)

scale = 615 / 1024
original_width = pixmap.width()
original_height = pixmap.height()

scaled_width = int(original_width * scale)
scaled_height = int(original_height * scale)
scale_pixmap = pixmap.scaled(pixmap.size() * scale, aspectRatioMode=Qt.KeepAspectRatio)

label.setPixmap(scale_pixmap)
painter = QPainter(label.pixmap())

pen = [QPen(Qt.red), QPen(Qt.green), QPen(Qt.blue)]
for i in range(1):
    count = min(5, len(prediction[nidus_type[i]]))
    for j in range(count):
        painter.setPen(pen[i])
        result = prediction[nidus_type[i]][j]
        left_top_x = result[0] * scale
        left_top_y = result[1] * scale
        right_bottom_x = result[2] * scale
        right_bottom_y = result[3] * scale
        width = right_bottom_x - left_top_x
        height = right_bottom_y - left_top_y
        painter.drawRect(int(left_top_x), int(left_top_y), int(width), int(height))
        print('left_top_x: {}, left_top_y: {}, width: {}, height: {}'.format(left_top_x, left_top_y, width, height))

painter.end()
label.setFixedSize(scaled_width, scaled_height)
label.setAlignment(Qt.AlignCenter)
window.setCentralWidget(label)
window.setGeometry(100, 100, scaled_width, scaled_height)
window.show()
app.exec_()

