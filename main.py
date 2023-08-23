
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from UI import mainWindow

class DicomViewer(QMainWindow, mainWindow.Ui_MainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setupUi(self) # 渲染页面控件
        self.connect_signals() # 设置信号槽

    def connect_signals(self):
        pass

def main():
    app = QApplication(sys.argv)
    myWindow = DicomViewer()
    myWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

