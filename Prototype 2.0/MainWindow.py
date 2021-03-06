# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(886, 748)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout1.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout1.setObjectName("horizontalLayout1")
        self.databasePathLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.databasePathLabel.setFont(font)
        self.databasePathLabel.setObjectName("databasePathLabel")
        self.horizontalLayout1.addWidget(self.databasePathLabel)
        self.databasePathLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.databasePathLineEdit.setFont(font)
        self.databasePathLineEdit.setObjectName("databasePathLineEdit")
        self.horizontalLayout1.addWidget(self.databasePathLineEdit)
        self.connectDatabaseBtn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.connectDatabaseBtn.setFont(font)
        self.connectDatabaseBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.connectDatabaseBtn.setObjectName("connectDatabaseBtn")
        self.horizontalLayout1.addWidget(self.connectDatabaseBtn)
        self.refreshBtn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.refreshBtn.setFont(font)
        self.refreshBtn.setObjectName("refreshBtn")
        self.horizontalLayout1.addWidget(self.refreshBtn)
        self.horizontalLayout1.setStretch(0, 1)
        self.horizontalLayout1.setStretch(1, 3)
        self.horizontalLayout1.setStretch(2, 1)
        self.horizontalLayout1.setStretch(3, 1)
        self.verticalLayout.addLayout(self.horizontalLayout1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.selectFileLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.selectFileLabel.setFont(font)
        self.selectFileLabel.setObjectName("selectFileLabel")
        self.horizontalLayout_2.addWidget(self.selectFileLabel)
        self.selectFileCombox = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.selectFileCombox.setFont(font)
        self.selectFileCombox.setObjectName("selectFileCombox")
        self.horizontalLayout_2.addWidget(self.selectFileCombox)
        self.selectFileBtn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.selectFileBtn.setFont(font)
        self.selectFileBtn.setObjectName("selectFileBtn")
        self.horizontalLayout_2.addWidget(self.selectFileBtn)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 4)
        self.horizontalLayout_2.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout2.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout2.setObjectName("horizontalLayout2")
        self.selectModelLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.selectModelLabel.setFont(font)
        self.selectModelLabel.setObjectName("selectModelLabel")
        self.horizontalLayout2.addWidget(self.selectModelLabel)
        self.selectModelComboBox = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.selectModelComboBox.setFont(font)
        self.selectModelComboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.selectModelComboBox.setObjectName("selectModelComboBox")
        self.selectModelComboBox.addItem("")
        self.selectModelComboBox.addItem("")
        self.selectModelComboBox.addItem("")
        self.selectModelComboBox.addItem("")
        self.selectModelComboBox.addItem("")
        self.selectModelComboBox.addItem("")
        self.horizontalLayout2.addWidget(self.selectModelComboBox)
        self.showModelBtn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.showModelBtn.setFont(font)
        self.showModelBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.showModelBtn.setObjectName("showModelBtn")
        self.horizontalLayout2.addWidget(self.showModelBtn)
        self.horizontalLayout2.setStretch(0, 1)
        self.horizontalLayout2.setStretch(1, 4)
        self.horizontalLayout2.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout2)
        self.horizontalLayout3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout3.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout3.setObjectName("horizontalLayout3")
        self.filePathLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.filePathLabel.setFont(font)
        self.filePathLabel.setObjectName("filePathLabel")
        self.horizontalLayout3.addWidget(self.filePathLabel)
        self.filePathLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.filePathLineEdit.setFont(font)
        self.filePathLineEdit.setObjectName("filePathLineEdit")
        self.horizontalLayout3.addWidget(self.filePathLineEdit)
        self.filePathBtn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.filePathBtn.setFont(font)
        self.filePathBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.filePathBtn.setObjectName("filePathBtn")
        self.horizontalLayout3.addWidget(self.filePathBtn)
        self.horizontalLayout3.setStretch(0, 1)
        self.horizontalLayout3.setStretch(1, 4)
        self.horizontalLayout3.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.thresholdValueLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.thresholdValueLabel.setFont(font)
        self.thresholdValueLabel.setObjectName("thresholdValueLabel")
        self.horizontalLayout_4.addWidget(self.thresholdValueLabel)
        self.thresholdValueSlider = QtWidgets.QSlider(self.centralwidget)
        self.thresholdValueSlider.setMaximum(100)
        self.thresholdValueSlider.setProperty("value", 50)
        self.thresholdValueSlider.setOrientation(QtCore.Qt.Horizontal)
        self.thresholdValueSlider.setObjectName("thresholdValueSlider")
        self.horizontalLayout_4.addWidget(self.thresholdValueSlider)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 4)
        self.horizontalLayout_4.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.startPredictBtn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.startPredictBtn.setFont(font)
        self.startPredictBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.startPredictBtn.setObjectName("startPredictBtn")
        self.horizontalLayout.addWidget(self.startPredictBtn)
        self.uploadResultBtn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.uploadResultBtn.setFont(font)
        self.uploadResultBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.uploadResultBtn.setObjectName("uploadResultBtn")
        self.horizontalLayout.addWidget(self.uploadResultBtn)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.resultWidget = QtWidgets.QWidget(self.centralwidget)
        self.resultWidget.setObjectName("resultWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.resultWidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.resultBrowser = QtWidgets.QTextBrowser(self.resultWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.resultBrowser.setFont(font)
        self.resultBrowser.setObjectName("resultBrowser")
        self.verticalLayout_3.addWidget(self.resultBrowser)
        self.verticalLayout_2.addWidget(self.resultWidget)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 5)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 1)
        self.verticalLayout.setStretch(5, 5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.statusbar.setStatusTip("")
        self.statusbar.setAutoFillBackground(False)
        self.statusbar.setObjectName("statusbar")
        self.statusbar.showMessage("未连接数据库")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.connectDatabaseBtn.clicked.connect(MainWindow.connectDatabase)
        self.showModelBtn.clicked.connect(MainWindow.showModel)
        self.filePathBtn.clicked.connect(MainWindow.filePath)
        self.selectModelComboBox.currentIndexChanged['QString'].connect(MainWindow.selectModel)
        self.uploadResultBtn.clicked.connect(MainWindow.uploadResult)
        # self.queryDatabaseBtn.clicked.connect(MainWindow.queryDatabase)
        self.startPredictBtn.clicked.connect(MainWindow.startPredict)
        self.selectFileBtn.clicked.connect(MainWindow.selectFile)
        self.refreshBtn.clicked.connect(MainWindow.refresh)
        self.thresholdValueSlider.valueChanged['int'].connect(MainWindow.updateThresholdValue)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "APT Predict"))
        self.databasePathLabel.setText(_translate("MainWindow", "数据库地址："))
        self.databasePathLineEdit.setText(_translate("MainWindow", "124.70.109.252"))
        self.connectDatabaseBtn.setText(_translate("MainWindow", "连接数据库"))
        self.refreshBtn.setText(_translate("MainWindow", "刷新"))
        self.selectFileLabel.setText(_translate("MainWindow", "数据库已有文件："))
        self.selectFileBtn.setText(_translate("MainWindow", "查询数据库"))
        self.selectModelLabel.setText(_translate("MainWindow", "选择测试模型："))
        self.selectModelComboBox.setItemText(0, _translate("MainWindow", "model1"))
        self.selectModelComboBox.setItemText(1, _translate("MainWindow", "model2"))
        self.selectModelComboBox.setItemText(2, _translate("MainWindow", "model3"))
        self.selectModelComboBox.setItemText(3, _translate("MainWindow", "model4"))
        self.selectModelComboBox.setItemText(4, _translate("MainWindow", "model5"))
        self.selectModelComboBox.setItemText(5, _translate("MainWindow", "model6"))
        self.showModelBtn.setText(_translate("MainWindow", "显示模型参数"))
        self.filePathLabel.setText(_translate("MainWindow", "待测文件路径："))
        self.filePathBtn.setText(_translate("MainWindow", "浏览"))
        self.thresholdValueLabel.setText(_translate("MainWindow", "阈值："))
        self.pushButton.setText(_translate("MainWindow", "重置阈值"))
        self.startPredictBtn.setText(_translate("MainWindow", "开始预测"))
        self.uploadResultBtn.setText(_translate("MainWindow", "上传预测结果"))
        self.resultBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">结果显示区域</p></body></html>"))
