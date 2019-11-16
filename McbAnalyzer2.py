# coding: utf-8
import re

class McbAnalyzer:
    def __init__(self, datalist):
        self.hyoso = datalist[0]
        self.kihon = datalist[1]
        self.hinshi = datalist[2]
        self.sai1 = datalist[3]
        self.sai2 = datalist[4]
        self.sai3 = datalist[5]
        self.katsuyou = datalist[6]
        self.sentence = datalist[7]
        self.total = datalist[8]

    def freq(self):
        """
        動詞、接続詞、受動態の頻度を出力する
        """
        pos_freq = dict()
        for pos in self.hinshi:
            pos_freq[pos] = pos_freq.get(pos, 0) + 1
            #該当する品詞の出現数（デフォルト値０）に１を足す。
        try:
            verb = pos_freq["動詞"]
        except KeyError:
            verb = 0
        try:
            particle = pos_freq["助詞"]
        except KeyError:
            particle = 0
        try:
            conjunction = pos_freq["接続詞"]
        except KeyError:
            conjunction = 0
        passive = 0
        for word in self.kihon:
            if word == "れる" or word == "られる":
                passive += 1
        
        return verb, particle, conjunction, passive


    def pos_rate(self):
        """
        各品詞(動詞、接続詞、文に対する受動態)の出現割合を出力する
        """
        pos_freq = dict()
        for pos in self.hinshi:
            pos_freq[pos] = pos_freq.get(pos, 0) + 1
            #元の形はpos_freq[b[0]] = pos_freq.get(b[0], 0) + 1
            #該当する品詞の出現数（デフォルト値０）に１を足す。

        posdata = dict()
        try:
            noun = pos_freq["名詞"]
        except KeyError:
            noun = 0
        posdata["noun_rate"] = noun / self.total

        try:
            verb = pos_freq["動詞"]
        except KeyError:
            verb = 0
        posdata["verb_rate"] = verb / self.total
        try:
            particle = pos_freq["助詞"]
        except KeyError:
            particle = 0
        posdata["particle_rate"] = particle / self.total
        try:
            conjunction = pos_freq["接続詞"]
        except KeyError:
            conjunction = 0
        posdata["conjunction_rate"] = conjunction / self.total

        passive = 0
        for word in self.kihon:
            if word == "れる" or word == "られる":
                passive += 1
        posdata["passive_rate"] = passive / verb

        #形容詞と形容動詞の合計の割合
        keiyoudoushi = 0
        for bunrui in self.sai1:
            if bunrui == "形容動詞語幹":
                keiyoudoushi += 1
        for bunrui in self.sai2:
            if bunrui == "形容動詞語幹":
                keiyoudoushi += 1
        try:
            adj = pos_freq["形容詞"]
        except KeyError:
            adj = 0
        posdata["adj_rate"] = (adj + keiyoudoushi) / self.total



        #print("動詞の割合：{0} \n 助詞・接続詞の割合:{1}".format(verb_rate, partconj_rate))
        return posdata
        
        #特定の品詞の割合を出したいが、文字コードの都合か"動詞"をキーとして認識してくれない→Anacondaで実行すると解決

    def kanji_rate(self):
        """
        漢字のみの単語の割合を出力する
        """
        wordcount = 0 #総語数を数える変数
        kanjicount = 0 #漢字のみの語数を数える変数
        for word in self.hyoso:
            wordcount += 1
            if re.match('[一-龥]', word) and not re.search('[あ-ん]', word):
                kanjicount += 1
        kanjirate = kanjicount / wordcount
        #print("漢字のみの単語の割合", ":", kanjirate)
        return kanjirate

    def rentai(self):
        """
        連体形(組み込み文)の割合を出力する
        """
        rentai_count = 0
        verb = 0
        for i in range(len(self.hyoso)):
            if self.hinshi[i] == "動詞":
                verb += 1
                try:
                    if self.katsuyou[i] == "基本形" and (self.hinshi[i+1] == "名詞" or self.hinshi[i+1] == "形容詞"):
                        rentai_count += 1
                except IndexError:
                    pass
        rentai_rate = rentai_count / verb
        return rentai_rate

