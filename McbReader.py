#coding:utf-8
import re, Pair
from statistics import stdev


class McbReader:
    def __init__(self, path):
        self.path = path

    def sentence(self):
        p = Pair.Pair(self.path)
        path = p.mcb2text()
        f = open(path, 'r', encoding="utf-8")
        text = f.read()
        f.close()
        text_splitted = re.split('。', text)
        return text_splitted

    
    def mcb_read(self):
        '''
        形態素解析されたファイルを受け取る
        return: hyoso, kihon, hinshi, sai1, sai2, sai3, sentence, total（それぞれがリスト）
        '''
        #pos_freq = {} #各品詞の出現数を記録する辞書
        sc = 0 #文の数を数えるカウンター．EOSで１増える.sentence counterの略
        linect = 0 #行数のカウンター,配列の添え字に使う
        hyoso = list()
        kihon = list()
        hinshi = list()
        sai1 = list()
        sai2 = list()
        sai3 = list()
        katsuyou = list()
        sentence = list()
        sentence.insert(sc, "")
        total = 0 #語数を数える
        f = open(self.path, 'r', encoding="utf-8")
        for row in f: #形態素解析されたテキストを読み込む
            try:
                
                if "EOS" in row: #行の中に"EOS"が含まれる場合
                    #sc += 1
                    #sentence.insert(sc, "")
                    pass
                    
                else:
                    a = row.split('\t')
                    b = a[1].split(',')
                    if "*" in b[6]: #基本形が"*"になっているときは表層形を基本形とする
                        b[6]=a[0]
        
                    hyoso.append(a[0])
                    kihon.append(b[6])
                    hinshi.append(b[0])
                    sai1.append(b[1])
                    sai2.append(b[2])
                    sai3.append(b[3])
                    katsuyou.append(b[5])
                    sentence[sc] = sentence[sc] + hyoso[linect]
                    total += 1
                    linect += 1
                    if a[0] == "。":
                        sc += 1
                        sentence.insert(sc, "")
            except EOFError:
                break
        
        if sentence[sc] == '':
            sentence.pop()
        f.close()
        datalist = [hyoso, kihon, hinshi, sai1, sai2, sai3, katsuyou, sentence, total]
        return datalist

   