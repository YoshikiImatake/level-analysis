import os, Pair

class FileCheck():
    def __init__(self, dirname):
        """
        引数: text/student, text/reviewed等
        """
        self.dirname = dirname

    def main(self):
        files = os.listdir(self.dirname)
        for file in files:
            p = Pair.Pair(file)
            if self.dirname == "text/student":
                filename = p.stu2rev()
            else:
                filename = p.rev2stu()
            if os.path.exists(filename):
                pass
            else:
                print(filename)
        print("以上")

if __name__ == '__main__':
    print("studentにあってreviewedにないファイル：\n")
    stu_check = FileCheck("text/student")
    stu_check.main()

    print("\nreviewedにあってstudentにないファイル：\n")
    rev_check = FileCheck("text/reviewed")
    rev_check.main()

    