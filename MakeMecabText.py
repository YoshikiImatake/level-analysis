import os, sys, shutil, MeCab

#AnacondaPromptで実行すること

newdir_stu = 'C:/Users/Yoshiki/OneDrive/translation-analysis-data/mcb_text/student_mcb/'
newdir_rev = 'C:/Users/Yoshiki/OneDrive/translation-analysis-data/mcb_text/reviewed_mcb/'
dir_stu = 'C:/Users/Yoshiki/OneDrive/translation-analysis-data/text/student/'
dir_rev = 'C:/Users/Yoshiki/OneDrive/translation-analysis-data/text/reviewed/'
files_stu = os.listdir(dir_stu)
files_rev = os.listdir(dir_rev)
m = MeCab.Tagger ("-r C:\progra~2\MeCab\etc\mecabrc-u")

try:
    shutil.rmtree(newdir_stu)
    shutil.rmtree(newdir_rev)
except FileNotFoundError:
    pass

os.makedirs(newdir_stu)
os.makedirs(newdir_rev)

#studentディレクトリのMeCab化

for filename_stu in files_stu:
    path = dir_stu + filename_stu
    path_mcb = newdir_stu + filename_stu.replace('.txt', '_mcb.txt')
    with open(path, mode='r', encoding='utf-8') as file:
        with open(path_mcb, mode='w', encoding='utf-8') as file_mcb:
            for row in file:
                file_mcb.write(m.parse (row))
            
#reviewedディレクトリのMeCab化
for filename_rev in files_rev:
    path = dir_rev + filename_rev
    path_mcb = newdir_rev + filename_rev.replace('.txt', '_mcb.txt')
    with open(path, mode='r', encoding='utf-8') as file:
        with open(path_mcb, mode='w', encoding='utf-8') as file_mcb:
            for row in file:
                file_mcb.write(m.parse (row))