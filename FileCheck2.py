import os, re

revfiles = os.listdir("text/reviewed")
stufiles = os.listdir("text/student")
for (rev, stu) in zip(revfiles, stufiles):
    revid = re.sub("_rev.txt", "", rev)
    stuid = re.sub("_stu.txt", "", stu)
    if revid != stuid:
        print(revid)
    else:
        pass