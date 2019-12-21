import McbReader
from statistics import stdev

class SentenceAnalyzer:
    def __init__(self, text):
        self.text = text

    def sentence_length(self):
        '''
        テキストファイル中に含まれる文の長さの[0]平均値[1]標準偏差[2]変動係数を返す
        '''
        snum = 0 #文の数をかぞえる
        cnum = 0 #全文字数を数える
        length_list = list()
        for sentence in self.text:
            if len(sentence) != 0:
                snum += 1
                cnum += len(sentence)
                length_list.append(len(sentence))
        try:
            mean_length = cnum / snum
        except ZeroDivisionError:
            mean_length = 0
        stdev_length = stdev(length_list)
        cov_length = stdev_length / mean_length #変動係数
        #print("文字数：{0} 文の数：{1} 1文中の平均字数：{2}".format(cnum, snum, mean_length))
        return mean_length, stdev_length, cov_length
    '''
    #def ku_length(self):
        
        1文中の句の数の[0]中央値[1]最大値[2]分散
        句の長さの[3]中央値[4]最大値[5]分散
    '''