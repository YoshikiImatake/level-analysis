import McbAnalyzer

pos_freq = {} #各品詞の出現数を記録する辞書
sc = 0 #文の数を数えるカウンター．EOSで１増える.sentence counterの略
linect = 0 #行数のカウンター,配列の添え字に使う
hyoso = list()
kihon = list()
hinshi = list()
sai1 = list()
sai2 = list()
sai3 = list()
sentence = list()
sentence.insert(sc, "")
total = 0 #語数を数える

while True: #形態素解析されたテキストを読み込む
    try:
        text = input()
        if text == "EOS":
            sc += 1
            sentence.insert(sc, "")
        else:
            a = text.split('\t')
            b = a[1].split(',')
            if b[6]=="*": #基本形が"*"になっているときは表層形を基本形とする
                b[6]=a[0]

            hyoso.insert(linect, a[0])
            kihon.insert(linect, b[6])
            hinshi.insert(linect, b[0])
            sai1.insert(linect, b[1])
            sai2.insert(linect, b[2])
            sai3.insert(linect, b[3])
            sentence[sc] = sentence[sc] + hyoso[linect]
            total += 1
            linect += 1
    except EOFError:
        break

datalist = [hyoso, kihon, hinshi, sai1, sai2, sai3, sentence, total]

a1 = McbAnalyzer.McbAnalyzer(datalist)
a1.pos_rate()
a1.kanji_rate()