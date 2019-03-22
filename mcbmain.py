import os, McbReader, McbAnalyzer
dirname = 'mcb_text/student_mcb/'
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
    print(data)