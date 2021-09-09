import sys
import os
from pathlib import Path
import shutil
from scipy import sparse
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
import re

dir_path = Path(os.path.abspath(__file__)).parent.parent
# input_path = Path('./model/input')
# text_reports_path = Path('./model/input/test_report')
# dir_path = Path(os.path.abspath(__file__)).parent.joinpath('model')
input_path = dir_path.joinpath('input')
text_reports_path = input_path.joinpath('test_report')

result_file = []

def process_sample(sample:(str,Path),words_in_sample:[str],s: str):
    file_path = text_reports_path.joinpath(sample[0]+'.txt')
    # file_path = './model/input/test_report/' + sample[0] + '.txt'
    result_file.append(file_path)
    with open(str(file_path), 'w', encoding='utf-8') as wf:
        wf.write('\n'.join(map(str, words_in_sample)))
        
def append_secondary_features(files: [Path], bag_of_words):
    secondary_features = {
        '"function_name":"IsNetworkAlive"': 'APT 1',
        '"regkey_r":"Software\\\\Microsoft\\\\AdvancedINFSetup"': 'APT 10',
        '"filepath": "C:\\Users\\John\\AppData\\Local\\Temp\\msi.dll"': 'APT 19',
        '"filepath":"C:\\Windows\\System32\\FastUserSwitchingCompatibilityex.dll"': 'APT 21',
        '"function_name":"_snwprintf"': 'APT 28',
        '"function_name": "CoInternetIsFeatureEnabledForUrl"': 'APT 29',
        '"mutant_name": "Microsoft': 'APT 30',
        '"process_name": "igfxext.exe"': 'Dark Hotel',
        '"regkey_r": "fertger"': 'Energetic Bear',
        '"newfilepath":"C:\\fanny.bmp"': 'Equation Group',
        '"filepath":"C:\\ProgramFiles\\CommonFiles\\MicrosoftShared\\OFFICE14\\1033\\ALRTINTL.DLL"': 'Gorgon Group',
        '"filepath":"C:\\Windows\\winmm.dll"': 'Winnti'
    }
    appendix = []
    for i in files:
        path_parts = Path(i).parts
        argument_file = input_path.joinpath('cuckoo_extracted_arguments', path_parts[-1])
        # argument_file = './model/input/cuckoo_extracted_arguments/' + path_parts[-1]
        content = open(str(argument_file), 'r', encoding='utf-8').read()
        secondary_features_result = []

        for j in secondary_features.keys():
            if j in content:
                secondary_features_result.append(1)
            else:
                secondary_features_result.append(0)

        appendix.append(secondary_features_result)
        
    bag_of_words_t = bag_of_words.transpose()
    appendix_t = sparse.csr_matrix(np.array(appendix)).transpose()
    combined = csr_vappend(bag_of_words_t, appendix_t)
    return sparse.csr_matrix(combined).transpose()

def csr_vappend(a, b):
    a.data = np.hstack((a.data, b.data))
    a.indices = np.hstack((a.indices, b.indices))
    a.indptr = np.hstack((a.indptr, (b.indptr + a.nnz)[1:]))
    a._shape = (a.shape[0] + b.shape[0], b.shape[1])
    return a

def work(files:list):

    if not os.path.exists(text_reports_path):
        os.makedirs(str(text_reports_path))
    else:
        shutil.rmtree(str(text_reports_path))
        os.makedirs(str(text_reports_path))

    result_file.clear()

    reports = []
    reports.append(('all_words', Path(input_path.joinpath('cuckoo_extracted_api').joinpath('all_words.txt'))))
    # reports.append(('all_words', Path('./model/input/cuckoo_extracted_api/all_words.txt')))

    p = Path(input_path.joinpath('cuckoo_extracted_api'))
    # p = Path('./model/input/cuckoo_extracted_api')

    for file in files:
        reports.append((re.split('[_ .]', file)[0], p.joinpath(file)))

    for report in reports:
        with open(str(report[1]),'r') as rf:
            process_sample(report,
                        [x.replace('\n', '').replace('"', '') for x in rf.readlines()],
                        report[0])

    vectorizer = CountVectorizer(input='filename', max_features=243, max_df=1.0)

    bag_of_words = vectorizer.fit_transform(map(str, result_file))
    bag_of_words = append_secondary_features(result_file, bag_of_words)

    return bag_of_words