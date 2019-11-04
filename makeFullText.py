import os, sys, shutil, codecs

#AnacondaPromptで実行すること
#学生の下訳と校閲済みの訳文をそれぞれ1つのファイルに統合する

newdir = 'full_text/'
dir_stu = 'text/student/'
dir_rev = 'text/reviewed/'
files_stu = os.listdir(dir_stu)
files_rev = os.listdir(dir_rev)

try:
    shutil.rmtree(newdir)
except FileNotFoundError:
    pass

os.makedirs(newdir)

#studentディレクトリの統合
path_stu = newdir + 'student_full.txt'
with open(path_stu, mode='w', encoding='utf-8')as fout:
    for filename_stu in files_stu:
        path = dir_stu + filename_stu
        try:
            with open(path, mode='r', encoding='utf-8') as fin:
                for row in fin:
                    fout.write(row)
        except UnicodeDecodeError:
            print(path)

 
#reviewedディレクトリの統合
path_rev = newdir + 'reveiwed_full.txt'
with open(path_rev, mode='w', encoding='utf-8')as fout:
    for filename_rev in files_rev:
        path = dir_rev + filename_rev
        try:
            with open(path, mode='r', encoding='utf-8') as fin:
                for row in fin:
                    fout.write(row)
        except UnicodeDecodeError:
            print(path)
