import re

class Analyzer:
    def __init__(self, text, reviewed):
        self.text = text
        self.reviewed = reviewed
 
    def sentence_length(self):
        text_splitted = re.split('\n|。', self.text)
        snum = 0 #文の数をかぞえる
        cnum = 0 #文字数を数える
        for sentence in text_splitted:
            if len(sentence) != 0:
                snum += 1
                cnum += len(sentence)
        mean_length = cnum / snum
        print("文字数：{0} 文の数：{1} 1文中の平均字数：{2}".format(cnum, snum, mean_length))
        

            








