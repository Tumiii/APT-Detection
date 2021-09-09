import sys

from PyQt5.QtGui import QPixmap

import MainWindow
import ModelWidget
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class ModelDialogInstance(ModelWidget.Ui_Form, QDialog):
    dlgList = []

    def __init__(self, model='basic', info=None):
        super(ModelDialogInstance, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(model)
        try:
            if info:
                self.algorithm = info['algorithm']
                self.grouper = info['grouper']
                self.sampling = info['sampling']

                self.accuracy_avg = info['metrics']['accuracy']['average']
                self.precision_avg = info['metrics']['precision']['average']
                self.recall_avg = info['metrics']['recall']['average']
                self.f1_avg = info['metrics']['f1']['average']

                self.titleLabel.setText(model+"模型参数")
                self.algorithmLabel.setText("分类算法： "+self.algorithm)
                self.grouperLabel.setText("分类指标： "+self.grouper)
                self.samplingLabel.setText("采样方法： "+self.sampling)

                self.accuracyLabel.setText("准确率（Accuracy）： " + '%.2f' % self.accuracy_avg)
                self.precisionLabel.setText("精确率（Precision）： " + '%.2f' % self.precision_avg)
                self.recallLabel.setText("召回率（recall）： " + '%.2f' % self.recall_avg)
                self.f1Label.setText("F-1： " + '%.2f' % self.f1_avg)

                self.confusionMatrixPixmap = QPixmap('./model/models/graphs/confusion_matrix_'+model+'.png')
                self.confusionMatrixLabel.setPixmap(self.confusionMatrixPixmap)
                self.confusionMatrixLabel.setScaledContents(True)

                self.rocPixmap = QPixmap('./model/models/graphs/roc_'+model+'.png')
                self.rocLabel.setPixmap(self.rocPixmap)
                self.rocLabel.setScaledContents(True)
        except:
            return

    def addDialog(self, model1: str, info1):
        dlg = ModelDialogInstance(model=model1, info=info1)
        self.dlgList.append(dlg)
        dlg.show()
        dlg.exec_()
