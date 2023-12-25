import sys
import cv2
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QFileDialog
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('OpenCV and PyQt5 Demo')
        self.setGeometry(100, 100, 800, 600)

        self.label = QLabel(self)
        self.label.resize(640, 480)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setText('Load an image using the button below')

        self.button = QPushButton('Load Image', self)
        self.button.move(350, 520)
        self.button.clicked.connect(self.loadImage)

    def loadImage(self):
        imagePath, _ = QFileDialog.getOpenFileName()
        if imagePath:
            self.displayImage(imagePath)

    def displayImage(self, imagePath):
        img = cv2.imread(imagePath)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        height, width, channel = img.shape
        step = channel * width
        qImg = QImage(img.data, width, height, step, QImage.Format_RGB888)

        self.label.setPixmap(QPixmap.fromImage(qImg))


def main():
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
