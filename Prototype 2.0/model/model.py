from pathlib import Path
from typing import OrderedDict
import numpy as np
import os
import joblib
import json

import model.preprocess.main as MPA

model_dir = Path(os.path.abspath(__file__)).parent.joinpath('models')
input_dir = Path(os.path.abspath(__file__)).parent.joinpath('input')
# model_dir = Path(os.path.abspath(__file__)).parent.joinpath('model').joinpath('models')
# input_dir = Path(os.path.abspath(__file__)).parent.joinpath('model').joinpath('input')

apt_translate = [
    'APT 1',
    'APT 10',
    'APT 21',
    'APT 29',
    '其他分类'
]
country_translate = [
    'China',
    'Russia',
    '其他分类'
]
translate_switch = {'APTGrouper': apt_translate, 'CountryGrouper': country_translate}

# with open('./model/models/models_info.json', 'r') as f:
with open(str(model_dir) + '/models_info.json', 'r') as f:
    models_info = json.load(f)

def predict(files=[], modelname='model1', threshold=0.5):
    '''

    modelname: 使用的预测模型名称（不要加后缀名）。所有模型请放在models文件夹下。

    threshold: 预测为某一分类的阈值，当所有类的预测概率均小于阈值时，会被预测为其他分类。取值为0到1。使用国家分类（二分类）时阈值相应地应设置的高一些。

    待预测文件请放在reports/predict目录下，默认会对该目录所有文件进行预测
    '''

    # 读取模型（应保证模型文件存在），判断模型类别（'APTGrouper','CountryGrouper','FamilyGrouper'）
    # 暂时不要使用类别为'CountrySeparatedGroupAndFamiliesGrouper'的模型！
    model = joblib.load(model_dir.joinpath(modelname + '.pkl'))
    # model = joblib.load('./model/models/' + modelname + '.pkl')
    grouper = getmodelinfo(modelname)['grouper']

    # 对输入样本进行预处理
    bag_of_words = MPA.work(files)
    x_test = bag_of_words.toarray()[1:]
    #print(len(x_test))
    # 选择标签翻译器
    translate = translate_switch[grouper]

    # 预测，取概率最大值为预测标签
    y_pred_proba = np.transpose(model.predict_proba(x_test))[1]
    y_pred_label = [np.argmax(y) if y[np.argmax(y)]>threshold else len(translate)-1 for y in y_pred_proba]

    #print(len(y_pred_label))

    # 读取病毒文件名称
    virus_names = files

    # 构成病毒预测结果
    result = dict()
    for i in range(min(len(virus_names), len(y_pred_label))):
        #print(virus_names[i])
        result[virus_names[i]] = dict()
        result[virus_names[i]]['model'] = modelname
        result[virus_names[i]]['proba'] = y_pred_proba[i]
        result[virus_names[i]]['label'] = translate[y_pred_label[i]]

    return result

def getmodelinfo(modelname):
    for k, v in models_info.items():
        if (modelname == k):
            return v

def _get_filenames():
    allfiles = []
    # for _, _, files in os.walk('./model/input/cuckoo_extracted_api'):
    for _, _, files in os.walk(input_dir.joinpath('cuckoo_extracted_api')):
        for file in files:
            if file != 'all_words.txt':
                allfiles.append(file)
    return allfiles
