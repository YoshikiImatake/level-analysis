import os, McbReader, McbAnalyzer
import pandas as pd
import numpy as np
"""
以下のライブラリはここでは利用しない
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
"""
stu_dir = 'C:/Users/Yoshiki/OneDrive/translation-analysis-data/mcb_text/student_mcb/'
rev_dir = 'C:/Users/Yoshiki/OneDrive/translation-analysis-data/mcb_text/reviewed_mcb/'
label = "length,kanji rate,verb rate,conjunction rate,type" + "\n"
datafile = 'C:/Users/Yoshiki/OneDrive/translation-analysis-data/data/data.csv'
f = open(datafile, 'w')
f.write(label)
f.close()

def make_data(dirname):
    """
    ディレクトリ名(stu_dirかrev_dir)を受け取って
    データをcsvファイルにして返す
    中身：1文中の平均字数, 漢字の割合, 動詞の割合, 接続詞？の割合
    """
    files = os.listdir(dirname)
    if dirname == stu_dir:
            sr = 'student' #'sr'=「studentかreveiwedか」
    if dirname == rev_dir:
            sr = 'reviewed'
    f = open(datafile, 'a')
    for file in files:
        #print('ファイル区切り')
        path = dirname + file
        mcb = McbReader.McbReader(path)
        length = mcb.sentence_length()
        #print("1文中の平均字数", length)
        datalist = mcb.mcb_read()
        a1 = McbAnalyzer.McbAnalyzer(datalist)
        pr = a1.pos_rate()
        verb_rate = pr[0]
        partconj_rate = pr[1]
        kanji = a1.kanji_rate()
        content = str(length) + ',' + str(kanji) + ',' + str(verb_rate) + ',' + str(partconj_rate) + ',' + sr + '\n'
        f.write(content)
    f.close()

       

make_data(stu_dir)
make_data(rev_dir)
