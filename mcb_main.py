import McbAnalyzer

pos_freq = {} #各品詞の出現数を記録する辞書
while True:
    try:
        text = input()
        if text == "EOS":
            pass #EOSの行をsplitするとa[1]がout of rangeになる
        else:
            a = text.split('\t')
            b = a[1].split(',')
            pos_freq[b[0]] = pos_freq.get(b[0], 0) + 1
                #該当する品詞の出現数（デフォルト値０）に１を足す。
    except EOFError:
        break

a1 = McbAnalyzer.McbAnalyzer(pos_freq)
a1.pos_rate()