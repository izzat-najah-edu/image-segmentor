import sys

import cv2
import numpy as np
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QGraphicsScene
from application import Ui_MainWindow


class MyApplication(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Variables
        self.cv_image = None
        self.scene = QGraphicsScene(self)
        self.imageView.setScene(self.scene)

        # Set the window icon
        self.setWindowIcon(QIcon('./icon.png'))

        # Connect event handlers
        self.btnChooseImage.clicked.connect(self.choose_image_handler)
        self.btnSaveResult.clicked.connect(self.save_result_handler)
        self.btnApplyCustomFilter.clicked.connect(self.apply_custom_filter_handler)

    # Shows cv_image on QT graphics view component
    def update_display(self):
        if self.cv_image is not None:
            # Convert to a QImage and display it
            height, width = self.cv_image.shape
            bytes_per_line = width
            q_image = QImage(self.cv_image.data, width, height, bytes_per_line, QImage.Format_Grayscale8)
            pixmap = QPixmap.fromImage(q_image)
            self.scene.clear()
            self.scene.addPixmap(pixmap)
            self.imageView.fitInView(self.scene.itemsBoundingRect(), Qt.KeepAspectRatio)

    # Browse image file, stores it in cv_image, then displays it
    def choose_image_handler(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp)")
        if filename:
            # Load the image in grayscale using OpenCV
            self.cv_image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
            self.update_display()

    # Prompts save-file dialog to store cv_image
    def save_result_handler(self):
        if self.cv_image is not None:
            filename, _ = QFileDialog.getSaveFileName(self, "Save Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp)",
                                                      options=QFileDialog.Options())
            if filename:
                # Save the image using OpenCV
                cv2.imwrite(filename, self.cv_image)

    # Parses the custom fileter, then applies it to the image
    def apply_custom_filter_handler(self):
        filter_text = self.textCustomFilter.toPlainText()
        if self.cv_image is not None:
            kernel = np.array([[eval(num) for num in row.split(',')] for row in filter_text.split('\n')])
            if kernel is not None:
                self.apply_filter_to_image(kernel)
                self.update_display()

    # Applies the given filter on cv_image
    def apply_filter_to_image(self, kernel):
        try:
            filtered_image = cv2.filter2D(self.cv_image, -1, kernel)
            self.cv_image = filtered_image
        except Exception as e:
            print("Error applying custom filter:", e)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MyApplication()
    mainWindow.show()
    sys.exit(app.exec_())
