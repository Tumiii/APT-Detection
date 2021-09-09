# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
import os
import json
import shutil
import pymysql
import MainWindow
import ModelWidget
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from slot.ShowModel import ModelDialogInstance
from slot.Database import DBClient
import model.model as Model


class MainWindowInstance(MainWindow.Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(MainWindow.Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("APT")
        self.modelType = "model1"
        self.db = DBClient()
        self.res = None
        self.databaseFileList = []
        self.predictFileList = []
        self.fpp = FilePathProcess()
        self.thresholdValue = 0.5
        self.modelDialogInstance = ModelDialogInstance("basic")
        # 初始化时载入模型信息
        with open('./model/models/models_info.json', 'r') as f:
            self.modelsInfo = json.load(f)
        self.selectModelComboBox.insertItems(0, self.modelsInfo.keys())

    # 设置状态栏信息
    def updateStatusbar(self, text):
        self.statusbar.showMessage(text)

    # 设置输出区域信息
    def updateResultContent(self, text: str):
        self.resultBrowser.setText(text)

    # 格式化输出数据库查询的信息
    def showDatabaseResult(self, res):
        if res:
            print(res[0])
            modeltype = str(res[1])
        else:
            return None
        try:
            if modeltype == "model1" or modeltype == "model2" or modeltype == "model3":
                text = "\n测试文件名： " + str(res[0]) + "\
                    \n选择的模型： " + str(res[1]) + "\
                    \n预测为APT 1  的概率： " + str(res[2]) + "\
                    \n预测为APT 10 的概率： " + str(res[3]) + "\
                    \n预测为APT 21 的概率： " + str(res[4]) + "\
                    \n预测为APT 29 的概率： " + str(res[5]) + "\
                    \n预测结果： " + str(res[6]) + "\n"
                return text
            elif modeltype == "model4" or modeltype == "model5" or modeltype == "model6":
                text = "\n测试文件名： " + str(res[0]) + "\
                    \n选择的模型： " + str(res[1]) + "\
                    \n预测为 China 的概率： " + str(res[2]) + "\
                    \n预测为 Russia 的概率： " + str(res[3]) + "\
                    \n预测结果： " + str(res[4]) + "\n"
                return text
            else:
                return None
        except:
            return None

    # 格式化输出预测信息
    def showPredictResult(self, res):
        if not res:
            return False
        try:
            text = ""
            for k in res.keys():
                modeltype = str(res[k]['model'])
                if modeltype == "model1" or modeltype == "model2" or modeltype == "model3":
                    text += "\n测试文件名： " + str(k) + "\n"
                    text += "选择的模型： " + str(res[k]['model']) + "\n"
                    text += "预测为APT 1  的概率： " + str(res[k]['proba'][0]) + "\n"
                    text += "预测为APT 10 的概率： " + str(res[k]['proba'][1]) + "\n"
                    text += "预测为APT 21 的概率： " + str(res[k]['proba'][2]) + "\n"
                    text += "预测为APT 29 的概率： " + str(res[k]['proba'][3]) + "\n"
                    text += "预测结果： " + str(res[k]['label']) + "\n"
                elif modeltype == "model4" or modeltype == "model5" or modeltype == "model6":
                    text += "\n测试文件名： " + str(k) + "\n"
                    text += "选择的模型： " + str(res[k]['model']) + "\n"
                    text += "预测为 China 的概率：" + str(res[k]['proba'][0]) + "\n"
                    text += "预测为 Russia 的概率：" + str(res[k]['proba'][1]) + "\n"
                    text += "预测结果：" + str(res[k]['label']) + "\n"
                else:
                    return False
            self.updateResultContent(text)
            return True
        except:
            return False

    # 数据库查询语句处理
    def selectQueryProcess(self, modeltype: str, fileName: str):
        if modeltype == "model1" or modeltype == "model2" or modeltype == "model3":
            res = self.db.query(
                "select fileName,model,\
                accuracy1 as label1_accuracy,\
                accuracy2 as label2_accuracy,\
                accuracy3 as label3_accuracy,\
                accuracy4 as label4_accuracy,\
                label as predictionResult \
                from result \
                where fileName = \"" + fileName + "\";")
            # and model = \"" + modeltype + "\"
            return res
        elif modeltype == "model4" or modeltype == "model5" or modeltype == "model6":
            res = self.db.query(
                "select fileName,model,\
                accuracy1 as label1_accuracy,\
                accuracy2 as label2_accuracy,\
                label as predictionResult \
                from result \
                where fileName = \"" + fileName + "\";")
            # and model = \"" + modeltype + "\"
            return res
        else:
            self.updateResultContent("数据库中查询错误")
            return None

    # 数据库插入语句处理
    def insertQueryProcess(self):
        print(self.res.keys())
        for k in self.res.keys():
            modeltype = self.res[k]['model']
            print(k)
            if modeltype == "model1" or modeltype == "model2" or modeltype == "model3":
                self.db.query(
                    "REPLACE INTO result(fileName, model, accuracy1, accuracy2, accuracy3, accuracy4, label)\
                    values(\"" + k + "\"\
                    ,\"" + str(self.res[k]['model']) + "\"\
                    ," + str(self.res[k]['proba'][0]) + "\
                    ," + str(self.res[k]['proba'][1]) + "\
                    ," + str(self.res[k]['proba'][2]) + "\
                    ," + str(self.res[k]['proba'][3]) + "\
                    ,\"" + str(self.res[k]['label'] + "\");"))
            elif modeltype == "model4" or modeltype == "model5" or modeltype == "model6":
                self.db.query(
                    "REPLACE INTO result(fileName, model, accuracy1, accuracy2, label)\
                    values(\"" + k + "\"\
                    ,\"" + str(self.res[k]['model']) + "\"\
                    ," + str(self.res[k]['proba'][0]) + "\
                    ," + str(self.res[k]['proba'][1]) + "\
                    ,\"" + str(self.res[k]['label'] + "\");"))
            else:
                return False

    # 数据库连接成功时初始化数据库文件列表
    def initCombox(self):
        self.selectFileCombox.clear()
        for fileName in self.databaseFileList:
            self.selectFileCombox.insertItems(0, fileName)

    # SLOT 显示模型参数
    def showModel(self):
        self.modelDialogInstance.addDialog(self.modelType, self.modelsInfo[self.modelType])

    # SLOT 连接数据库
    def connectDatabase(self):
        self.db.connect(self.databasePathLineEdit.text())
        self.refresh()

    # SLOT 待测文件路径
    def filePath(self):
        self.predictFileList.clear()
        directory = QFileDialog.getOpenFileNames(
            None,
            "选取测试文件(在api或arguments文件夹中选取即可)",
            "./reports/full",
            "Text Files (*.txt)")
        if directory[0]:
            for file in directory[0]:
                self.predictFileList.append(file)
            self.filePathLineEdit.setText(str(directory[0]))
        else:
            self.filePathLineEdit.setText("")

    # SLOT 选择预测模型
    def selectModel(self):
        self.modelType = self.selectModelComboBox.currentText()

    # SLOT 上传预测结果
    def uploadResult(self):
        try:
            if self.db.status() and self.res:
                self.insertQueryProcess()
        except:
            return

    # SLOT 查询数据库
    '''
        def queryDatabase(self):
        if self.db.status():
            if len(self.predictFileList) > 0:
                for curFilePath in self.predictFileList:
                    self.updateStatusbar("正在进行查询")
                    curFileNameList = curFilePath.split('/')
                    curFileName = curFileNameList[len(curFileNameList) - 1]
                    modeltype = self.selectModelComboBox.currentText()
                    res = self.selectQueryProcess(modeltype, curFileName)
                    if res:
                        self.showDatabaseResult(res)
                    else:
                        self.updateResultContent("数据库中无此文件的"+modeltype+"的预测结果")
                    self.updateStatusbar("查询成功")
            else:
                self.updateResultContent("待预测文件路径为空!")
        else:
            self.updateStatusbar("数据库未连接")
    '''

    # SLOT 开始预测
    def startPredict(self):
        predictFiles = []
        if len(self.predictFileList) > 0:
            for i in range(len(self.predictFileList)):
                if self.fpp.copyFile(self.predictFileList[i]):
                    textList = self.predictFileList[i].split('/')
                    predictFiles.append(textList[len(textList) - 1])
                    self.updateResultContent("正在读取待测文件并运行测试程序")
                else:
                    self.updateResultContent("读取待测文件失败!")
                    return False
            self.res = Model.predict(files=predictFiles, modelname=self.modelType, threshold=self.thresholdValue)
            self.showPredictResult(self.res)
        else:
            self.updateResultContent("待预测文件路径为空!")

    # SLOT 选择数据库中已有测试文件
    def selectFile(self):
        curFile = self.selectFileCombox.currentText()
        if curFile:
            res = self.selectQueryProcess(self.modelType, curFile)
            if res:
                text = ""
                for item in res:
                    print(item)
                    text += self.showDatabaseResult(item)
                self.updateResultContent(text)
            else:
                self.updateResultContent("此文件无"+self.modelType+"的预测\n请更换模型或文件再查询")

    # SLOT 刷新数据库文件列表
    def refresh(self):
        if self.db.status():
            self.updateStatusbar("数据库连接状态：成功")
            self.db.query("use prediction;")
            self.databaseFileList = self.db.query("select DISTINCT fileName from result;")
            if len(self.databaseFileList):
                self.updateStatusbar("已连接到数据库：prediction")
                self.initCombox()
            else:
                self.updateStatusbar("连接到prediction数据库：失败")
        else:
            self.updateStatusbar("数据库连接状态：失败")

    # SLOT 更新阈值
    def updateThresholdValue(self):
        self.thresholdValue = self.thresholdValueSlider.value()*1.0/100.0
        self.thresholdValueLabel.setText("阈值： "+str(self.thresholdValue))

class FilePathProcess(object):
    reportsDirName = ["cuckoo_extracted_api", "cuckoo_extracted_arguments"]
    targetDir = "./model/input/"

    def copyFile(self, src: str):
        try:
            textList = src.split('/')
            for rdn in self.reportsDirName:
                textList[len(textList) - 2] = rdn
                srcPath = '/'.join(textList)
                shutil.copy(srcPath, self.targetDir + rdn)
            return True
        except:
            return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # res = Model.predict(["579bbcfbd9d5631489f5a2be73970ba67e51f3fcd7ac296695f83eeb04bcb2b0.txt"])
    # print(res)

    myApp = QApplication(sys.argv)
    myWindow = MainWindowInstance()
    myWindow.show()
    sys.exit(myApp.exec_())


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
