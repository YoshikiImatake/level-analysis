import csv, os, sys, shutil
"""
閾値を受け取って、
それ以上のレーベンシュタイン距離があるファイルのみのフォルダを作る
"""
class Classify:
    def __init__(self, ldfile, border):
        self.ldfile = ldfile
        self.border = border

    def read(self):
        data = []
        above = []
        f = open(self.ldfile, 'r')
        reader = csv.reader(f)
        for row in reader:
            data.append(row)
        f.close()
        for row in data[1:]:
            if float(row[1]) >= self.border:
                above.append(row[0])
        return above

    def make_dir(self):
        above = self.read()
        newdir = 'mcb_text_above' + str(self.border) + '/'
        newdir_s = newdir + 'student_mcb/'
        newdir_r = newdir + 'reviewed_mcb/'
        dir_s = 'mcb_text/student_mcb/'
        dir_r = 'mcb_text/reviewed_mcb/'
        os.makedirs(newdir_s)
        os.makedirs(newdir_r)
        
        #student
        for title in above:
            file_s = title + "_stu_mcb.txt"
            file_r = title + "_rev_mcb.txt"
            path_s = dir_s + file_s
            path_r = dir_r + file_r
            shutil.copy(path_s, newdir_s)
            shutil.copy(path_r, newdir_r)
