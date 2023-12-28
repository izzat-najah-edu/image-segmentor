import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from application import Ui_MainWindow  # Replace with your file name


class MyApplication(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Additional initialization or event binding can go here


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MyApplication()
    mainWindow.show()
    sys.exit(app.exec_())
