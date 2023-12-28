# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'application.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(880, 740)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setAcceptDrops(False)
        icon = QtGui.QIcon.fromTheme("DefaultTheme")
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("font: 12pt \"Microsoft Sans Serif\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnChooseImage = QtWidgets.QPushButton(self.centralwidget)
        self.btnChooseImage.setGeometry(QtCore.QRect(30, 50, 141, 41))
        self.btnChooseImage.setObjectName("btnChooseImage")
        self.btnSaveImage = QtWidgets.QPushButton(self.centralwidget)
        self.btnSaveImage.setGeometry(QtCore.QRect(180, 50, 141, 41))
        self.btnSaveImage.setObjectName("btnSaveImage")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 90, 291, 21))
        self.label.setStyleSheet("font-size: 10px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.textCustomFilter = QtWidgets.QTextEdit(self.centralwidget)
        self.textCustomFilter.setGeometry(QtCore.QRect(30, 180, 291, 151))
        self.textCustomFilter.setStyleSheet("")
        self.textCustomFilter.setObjectName("textCustomFilter")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 140, 281, 31))
        self.label_2.setStyleSheet("font-weight: bold; font-size: 20px;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 620, 151, 31))
        self.label_3.setStyleSheet("font-weight: bold; font-size: 20px;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 10, 291, 31))
        self.label_4.setStyleSheet("font-weight: bold; font-size: 20px;")
        self.label_4.setObjectName("label_4")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 120, 311, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(20, 380, 851, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.btnApplyCustomFilter = QtWidgets.QPushButton(self.centralwidget)
        self.btnApplyCustomFilter.setGeometry(QtCore.QRect(30, 330, 291, 41))
        self.btnApplyCustomFilter.setObjectName("btnApplyCustomFilter")
        self.btnFilterLog = QtWidgets.QPushButton(self.centralwidget)
        self.btnFilterLog.setGeometry(QtCore.QRect(30, 490, 201, 41))
        self.btnFilterLog.setObjectName("btnFilterLog")
        self.btnFilterThreshold = QtWidgets.QPushButton(self.centralwidget)
        self.btnFilterThreshold.setGeometry(QtCore.QRect(40, 660, 141, 41))
        self.btnFilterThreshold.setObjectName("btnFilterThreshold")
        self.btnFilterLaplacian = QtWidgets.QPushButton(self.centralwidget)
        self.btnFilterLaplacian.setGeometry(QtCore.QRect(30, 450, 201, 41))
        self.btnFilterLaplacian.setObjectName("btnFilterLaplacian")
        self.btnFilterPointDetection = QtWidgets.QPushButton(self.centralwidget)
        self.btnFilterPointDetection.setGeometry(QtCore.QRect(30, 530, 201, 41))
        self.btnFilterPointDetection.setObjectName("btnFilterPointDetection")
        self.btnFilterVerticalLines = QtWidgets.QPushButton(self.centralwidget)
        self.btnFilterVerticalLines.setGeometry(QtCore.QRect(270, 460, 201, 41))
        self.btnFilterVerticalLines.setObjectName("btnFilterVerticalLines")
        self.btnFilterP45Lines = QtWidgets.QPushButton(self.centralwidget)
        self.btnFilterP45Lines.setGeometry(QtCore.QRect(270, 500, 201, 41))
        self.btnFilterP45Lines.setObjectName("btnFilterP45Lines")
        self.btnFilterM45Lines = QtWidgets.QPushButton(self.centralwidget)
        self.btnFilterM45Lines.setGeometry(QtCore.QRect(270, 540, 201, 41))
        self.btnFilterM45Lines.setObjectName("btnFilterM45Lines")
        self.btnFilterHorizontalLines = QtWidgets.QPushButton(self.centralwidget)
        self.btnFilterHorizontalLines.setGeometry(QtCore.QRect(270, 420, 201, 41))
        self.btnFilterHorizontalLines.setObjectName("btnFilterHorizontalLines")
        self.btnFilterVerticalEdges = QtWidgets.QPushButton(self.centralwidget)
        self.btnFilterVerticalEdges.setGeometry(QtCore.QRect(510, 460, 201, 41))
        self.btnFilterVerticalEdges.setObjectName("btnFilterVerticalEdges")
        self.btnFilterP45Edges = QtWidgets.QPushButton(self.centralwidget)
        self.btnFilterP45Edges.setGeometry(QtCore.QRect(510, 500, 201, 41))
        self.btnFilterP45Edges.setObjectName("btnFilterP45Edges")
        self.btnFilterM45Edges = QtWidgets.QPushButton(self.centralwidget)
        self.btnFilterM45Edges.setGeometry(QtCore.QRect(510, 540, 201, 41))
        self.btnFilterM45Edges.setObjectName("btnFilterM45Edges")
        self.btnFilterHorizontalEdges = QtWidgets.QPushButton(self.centralwidget)
        self.btnFilterHorizontalEdges.setGeometry(QtCore.QRect(510, 420, 201, 41))
        self.btnFilterHorizontalEdges.setObjectName("btnFilterHorizontalEdges")
        self.imageView = QtWidgets.QGraphicsView(self.centralwidget)
        self.imageView.setGeometry(QtCore.QRect(350, 20, 501, 351))
        self.imageView.setStyleSheet("")
        self.imageView.setObjectName("imageView")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 400, 281, 31))
        self.label_5.setStyleSheet("font-weight: bold; font-size: 20px;")
        self.label_5.setObjectName("label_5")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(20, 600, 851, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.sliderThreshold = QtWidgets.QSlider(self.centralwidget)
        self.sliderThreshold.setGeometry(QtCore.QRect(200, 670, 651, 22))
        self.sliderThreshold.setMaximum(255)
        self.sliderThreshold.setProperty("value", 128)
        self.sliderThreshold.setOrientation(QtCore.Qt.Horizontal)
        self.sliderThreshold.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.sliderThreshold.setTickInterval(8)
        self.sliderThreshold.setObjectName("sliderThreshold")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(190, 650, 31, 16))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(830, 650, 31, 16))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(490, 640, 71, 31))
        self.label_8.setStyleSheet("font-weight: bold")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(730, 440, 121, 121))
        self.groupBox.setObjectName("groupBox")
        self.radioEdgeDetectorSobel = QtWidgets.QRadioButton(self.groupBox)
        self.radioEdgeDetectorSobel.setGeometry(QtCore.QRect(10, 40, 101, 31))
        self.radioEdgeDetectorSobel.setChecked(True)
        self.radioEdgeDetectorSobel.setObjectName("radioEdgeDetectorSobel")
        self.radioEdgeDetectorPrewitt = QtWidgets.QRadioButton(self.groupBox)
        self.radioEdgeDetectorPrewitt.setGeometry(QtCore.QRect(10, 70, 101, 31))
        self.radioEdgeDetectorPrewitt.setObjectName("radioEdgeDetectorPrewitt")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 880, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Image Segmentor"))
        self.btnChooseImage.setText(_translate("MainWindow", "Choose Image"))
        self.btnSaveImage.setText(_translate("MainWindow", "Save Image"))
        self.label.setText(_translate("MainWindow", "Changing the image will discard any unsaved progress"))
        self.textCustomFilter.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Microsoft Sans Serif\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">0,-1,0</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">-1,5,-1</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">0,-1,0</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Custom Filter"))
        self.label_3.setText(_translate("MainWindow", "Thresholding"))
        self.label_4.setText(_translate("MainWindow", "Input/Output"))
        self.btnApplyCustomFilter.setText(_translate("MainWindow", "Apply"))
        self.btnFilterLog.setText(_translate("MainWindow", "Laplacian of Gaussian"))
        self.btnFilterThreshold.setText(_translate("MainWindow", "Apply"))
        self.btnFilterLaplacian.setText(_translate("MainWindow", "Laplacian"))
        self.btnFilterPointDetection.setText(_translate("MainWindow", "Point Detection"))
        self.btnFilterVerticalLines.setText(_translate("MainWindow", "Vertical Lines"))
        self.btnFilterP45Lines.setText(_translate("MainWindow", "+45 Lines"))
        self.btnFilterM45Lines.setText(_translate("MainWindow", "-45 Lines"))
        self.btnFilterHorizontalLines.setText(_translate("MainWindow", "Horizontal Lines"))
        self.btnFilterVerticalEdges.setText(_translate("MainWindow", "Vertical Edges"))
        self.btnFilterP45Edges.setText(_translate("MainWindow", "+45 Edges"))
        self.btnFilterM45Edges.setText(_translate("MainWindow", "-45 Edges"))
        self.btnFilterHorizontalEdges.setText(_translate("MainWindow", "Horizontal Edges"))
        self.label_5.setText(_translate("MainWindow", "Detection Filters"))
        self.label_6.setText(_translate("MainWindow", "0"))
        self.label_7.setText(_translate("MainWindow", "255"))
        self.label_8.setText(_translate("MainWindow", "Thresh"))
        self.groupBox.setTitle(_translate("MainWindow", "Edge Detector"))
        self.radioEdgeDetectorSobel.setText(_translate("MainWindow", "Sobel"))
        self.radioEdgeDetectorPrewitt.setText(_translate("MainWindow", "Prewitt"))
