import Levenshtein, os, sentenceMatch

stu_dir = 'text/student/'
rev_dir = 'text/reviewed/'
result = "data/Levenshtein_data.csv"
label = "Title, Levenshtein Distance\n"



sfiles = os.listdir(stu_dir)
f = open(result, 'w')
f.write(label)

for sfile in sfiles:
    num = sfile.replace('_stu.txt','')
    sfile = 'text/student/' + sfile
    rfile = 'text/reviewed/'+ num + '_rev.txt'
    s = sentenceMatch.read(sfile)
    r = sentenceMatch.read(rfile)
    if s == "TooLong" or r == "TooLong":
        print(num, ": 長すぎる文が含まれています\n")
        pass
    else:
        m = sentenceMatch.match(s,r)
        sum = 0
        for data in m:
            sum += data[1]
        ave = sum / len(m)
        title_result = "{0},{1}\n".format(num, ave)
        f.write(title_result)

    
    
    





f.close()