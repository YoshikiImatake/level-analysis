import os, McbReader, McbAnalyzer
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
stu_dir = 'C:/Users/Yoshiki/OneDrive/translation-analysis-data/mcb_text/student_mcb/'
rev_dir = 'C:/Users/Yoshiki/OneDrive/translation-analysis-data/mcb_text/reviewed_mcb/'
X = list()

def make_data(dirname):
    files = os.listdir(dirname)
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
        data = list()
        data.append(length)
        data.append(kanji)
        data.append(verb_rate)
        data.append(partconj_rate)
        #print(data)
        X.append(data)

"""
make_data(stu_dir)
make_data(rev_dir)
#print(X)
XArray = np.array(X)
#print(XArray)
#print(len(X))

#ラベルを付ける（学生＝０、校閲＝１）
y = list()
for i in range(0, 18):
    y.append(0)
for i in range(18, 36):
    y.append(1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1234)
#pred = KMeans(n_clusters=2).fit_predict()


lm = LinearRegression()
lm.fit(X_train, y_train)
y_pred = lm.predict(X_test)
print(y_pred)
print(y_test)
#confusion_matrix(y_test, y_pred)
"""