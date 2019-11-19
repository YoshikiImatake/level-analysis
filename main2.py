import os, McbReader, McbAnalyzer2


stu_dir = 'mcb_text/student_mcb/'
rev_dir = 'mcb_text/reviewed_mcb/'
label = "title,noun rate,verb rate,adj rate,particle rate,conjunction rate,passive rate,rentai rate,kanji rate,mean length,coefficient of variation of length,no,type" + "\n"
datafile = 'data/data5.csv'
f = open(datafile, 'w')
f.write(label)
f.close()

def make_data(dirname):
    """
    ディレクトリ名(stu_dirかrev_dir)を受け取って
    データをcsvファイルにして返す
    中身：1文中の平均字数, 漢字の割合, 動詞の割合, 接続詞？, 受動態の割合
    """
    files = os.listdir(dirname)
    if dirname == stu_dir:
            sr = 'student' #'sr'=「studentかreveiwedか」
    if dirname == rev_dir:
            sr = 'reviewed'
    f = open(datafile, 'a')
    for file in files:
        #print('ファイル区切り')
        path = dirname + file
        mcb = McbReader.McbReader(path)
        l = mcb.sentence_length()
        mean_length = l[0]
        cov_length = l[2]
        #print("1文中の平均字数", length)
        datalist = mcb.mcb_read()
        a1 = McbAnalyzer2.McbAnalyzer(datalist)
        pr = a1.pos_rate()
        noun_rate = pr["noun_rate"]
        verb_rate = pr["verb_rate"]
        adj_rate = pr["adj_rate"]
        particle_rate = pr["particle_rate"]
        conjunction_rate = pr["conjunction_rate"]
        passive_rate = pr["passive_rate"]
        rentai = a1.rentai()
        kanji = a1.kanji_rate()
        no = a1.no_repetition()
        content = str(file) + ',' + str(noun_rate) + ',' + str(verb_rate) + ',' + str(adj_rate) + ',' + str(particle_rate) + ',' + str(conjunction_rate) + ',' + str(passive_rate) + ',' + str(rentai) + ',' + str(kanji) + ',' + str(mean_length) + ',' + str(cov_length) + ',' + str(no) + ',' + sr + '\n'
        f.write(content)
    f.close()

       

make_data(stu_dir)
make_data(rev_dir)
