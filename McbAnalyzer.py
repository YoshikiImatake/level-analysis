# coding: UTF-8
import re

class McbAnalyzer:
    def __init__(self, datalist):
        self.hyoso = datalist[0]
        self.kihon = datalist[1]
        self.hinshi = datalist[2]
        self.sai1 = datalist[3]
        self.sai2 = datalist[4]
        self.sai3 = datalist[5]
        self.sentence = datalist[6]
        self.total = datalist[7]

    def pos_rate(self): #各品詞の出現割合を出力する
        pos_freq = dict()
        for pos in self.hinshi:
            pos_freq[pos] = pos_freq.get(pos, 0) + 1
            #元の形はpos_freq[b[0]] = pos_freq.get(b[0], 0) + 1
            #該当する品詞の出現数（デフォルト値０）に１を足す。

        for key in pos_freq:
            key_freq = pos_freq[key]
            key_rate = key_freq / self.total
            print(key, ":", key_rate)
            
                

        """
        verb = self.pos_freq["動詞"]
        total = 0
        for pos in self.pos_freq:
            total += self.pos_freq[pos]
        rate = verb / total
        print("動詞の割合：{0} ".format(rate))
        """
        #特定の品詞の割合を出したいが、文字コードの都合か"動詞"をキーとして認識してくれない

    def kanji_rate(self): #漢語の割合を出力する
        wordcount = 0 #総語数を数える変数
        kanjicount = 0 #漢字のみの語数を数える変数
        for word in self.hyoso:
            wordcount += 1
            if re.match('[一-龥]', word) and not re.search('[あ-ん]', word):
                kanjicount += 1
        kanjirate = kanjicount / wordcount
        print("漢字のみの単語の割合", ":", kanjirate)
           






            








