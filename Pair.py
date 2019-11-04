import re

class Pair:
    def __init__(self, filename):
        self.filename = re.sub('.*/', '', str(filename))

    def text2mcb(self):
        if "stu" in self.filename:
            return 'text/student/' + re.sub('.txt', '_mcb.txt', self.filename)
        else:
            return 'text/reviewed/' + re.sub('.txt', '_mcb.txt', self.filename)
         
    def mcb2text(self):
        if "stu" in self.filename:
            return 'text/student/' + re.sub('_mcb.txt', '.txt', self.filename)
        else:
            return 'text/reviewed/' + re.sub('_mcb.txt', '.txt', self.filename)

    def stu2rev(self):
        if "mcb" in self.filename:
            return 'mcb_text/reviewed_mcb/' + re.sub('stu', 'rev', self.filename)
        else:
            return 'text/reviewed/' + re.sub('stu', 'rev', self.filename)

    def rev2stu(self):
        if "mcb" in self.filename:
            return 'mcb_text/student_mcb/' + re.sub('rev', 'stu', self.filename)
        else:
            return 'text/student/' + re.sub('rev', 'stu', self.filename)
