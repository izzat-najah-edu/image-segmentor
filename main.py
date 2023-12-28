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
        self.btnSaveImage.clicked.connect(self.save_result_handler)
        self.btnApplyCustomFilter.clicked.connect(self.apply_custom_filter_handler)
        self.btnFilterLog.clicked.connect(self.filter_log_handler)
        self.btnFilterThreshold.clicked.connect(self.filter_threshold_handler)
        self.btnFilterLaplacian.clicked.connect(self.filter_laplacian_handler)
        self.btnFilterPointDetection.clicked.connect(self.filter_point_detection_handler)
        self.btnFilterHorizontalLines.clicked.connect(self.filter_horizontal_lines_handler)
        self.btnFilterVerticalLines.clicked.connect(self.filter_vertical_lines_handler)
        self.btnFilterP45Lines.clicked.connect(self.filter_p45_lines_handler)
        self.btnFilterM45Lines.clicked.connect(self.filter_m45_lines_handler)
        self.btnFilterHorizontalEdges.clicked.connect(self.filter_horizontal_edges_handler)
        self.btnFilterVerticalEdges.clicked.connect(self.filter_vertical_edges_handler)
        self.btnFilterP45Edges.clicked.connect(self.filter_p45_edges_handler)
        self.btnFilterM45Edges.clicked.connect(self.filter_m45_edges_handler)

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

    # Applies the given filter on cv_image
    def apply_filter(self, kernel):
        if not isinstance(kernel, np.ndarray):
            kernel = np.array(kernel)
        if self.cv_image is not None:
            try:
                filtered_image = cv2.filter2D(self.cv_image, -1, kernel)
                self.cv_image = filtered_image
            except Exception as e:
                print("Error applying custom filter:", e)

    # Decides which type of edge detector based on the radio group then applies it
    def apply_edge_detector(self, sobel_kernel, prewitt_kernel):
        if self.radioEdgeDetectorSobel.isChecked() == "sobel":
            self.apply_filter(sobel_kernel)
        else:
            self.apply_filter(prewitt_kernel)
        self.update_display()

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
        kernel = np.array([[eval(num) for num in row.split(',')] for row in filter_text.split('\n')])
        if kernel is not None:
            self.apply_filter(kernel)
            self.update_display()

    # Applies the laplacian of gaussian filter on cv_image
    def filter_log_handler(self):
        self.apply_filter([
            [0, 0, -1, 0, 0],
            [0, -1, -2, -1, 0],
            [-1, -2, 16, -2, -1],
            [0, -1, -2, -1, 0],
            [0, 0, -1, 0, 0]
        ])
        self.update_display()

    # Applies thresholding on cv_image
    def filter_threshold_handler(self):
        thresh = self.sliderThreshold.value()
        _, self.cv_image = cv2.threshold(self.cv_image, thresh, 255, cv2.THRESH_BINARY)
        self.update_display()

    # Applies the laplacian filter on cv_image
    def filter_laplacian_handler(self):
        self.apply_filter([
            [0, 1, 0],
            [1, -4, 1],
            [0, 1, 0]
        ])
        self.update_display()

    # Applies points detector on cv_image
    def filter_point_detection_handler(self):
        self.apply_filter([
            [-1, -1, -1],
            [-1, 8, -1],
            [-1, -1, -1]
        ])
        self.update_display()

    # Applies horizontal lines detector on cv_image
    def filter_horizontal_lines_handler(self):
        self.apply_filter([
            [-1, -1, -1],
            [2, 2, 2],
            [-1, -1, -1]
        ])
        self.update_display()

    # Applies vertical lines detector on cv_image
    def filter_vertical_lines_handler(self):
        self.apply_filter([
            [-1, 2, -1],
            [-1, 2, -1],
            [-1, 2, -1]
        ])
        self.update_display()

    # Applies +45 lines detector on cv_image
    def filter_p45_lines_handler(self):
        self.apply_filter([
            [-1, -1, 2],
            [-1, 2, -1],
            [2, -1, -1]
        ])
        self.update_display()

    # Applies -45 lines detector on cv_image
    def filter_m45_lines_handler(self):
        self.apply_filter([
            [2, -1, -1],
            [-1, 2, -1],
            [-1, -1, 2]
        ])
        self.update_display()

    # Applies horizontal edges detector on cv_image
    def filter_horizontal_edges_handler(self):
        self.apply_edge_detector([
            [-1, -2, -1],
            [0, 0, 0],
            [1, 2, 1]
        ], [
            [-1, -1, -1],
            [0, 0, 0],
            [1, 1, 1]
        ])

    # Applies vertical edges detector on cv_image
    def filter_vertical_edges_handler(self):
        self.apply_edge_detector([
            [-1, 0, 1],
            [-2, 0, 2],
            [-1, 0, 1]
        ], [
            [-1, 0, 1],
            [-1, 0, 1],
            [-1, 0, 1]
        ])

    # Applies +45 edges detector on cv_image
    def filter_p45_edges_handler(self):
        self.apply_edge_detector([
            [-2, -1, 0],
            [-1, 0, 1],
            [0, 1, 2]
        ], [
            [-1, -1, 0],
            [-1, 0, 1],
            [0, 1, 1]
        ])

    # Applies -45 edges detector on cv_image
    def filter_m45_edges_handler(self):
        self.apply_edge_detector([
            [0, 1, 2],
            [-1, 0, 1],
            [-2, -1, 0]
        ], [
            [0, 1, 1],
            [-1, 0, 1],
            [-1, -1, 0]
        ])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MyApplication()
    mainWindow.show()
    sys.exit(app.exec_())
