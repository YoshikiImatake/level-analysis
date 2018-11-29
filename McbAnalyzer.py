
class McbAnalyzer:
    def __init__(self, pos_freq):
        self.pos_freq = pos_freq
 
    def pos_rate(self): #各品詞の出現割合を出力する
        total = 0
        for pos in self.pos_freq:
            total += self.pos_freq[pos]

        for key in self.pos_freq:
            key_freq = self.pos_freq[key]
            key_rate = key_freq / total
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

            








