import Levenshtein

def match(s, t):
    """
    2つの記事s,tを受け取り、
    レーベンシュタイン距離が近い文同士をペアにして返す。
    return text1, text2, Levenshtein Distance
    """ 
    ldlist = []
    for ssen in s:
        ssen = ssen.replace("\n","")
        if len(ssen) == 0:
            pass
        else:
            ld = []
            lddict = {}
            for tsen in t:
                tsen = tsen.replace("\n","")
                ldresult = Levenshtein.lds(ssen,tsen)
                ld.append(ldresult)
                lddict[ldresult] = (ssen, tsen)
            u = lddict[min(ld)],min(ld)
            ldlist.append(u)
    return ldlist


def read(path):
    """
    テキストファイルのパスを受けとり、
    文ごとのリストにして返す
    """
    txt = ''
    with open(path, mode='r', encoding='utf-8')as fin:
        for row in fin:
            txt += row
    s = txt.split("。")
    for sen in s:
        if len(sen) > 150:
            return "TooLong"
    return s

def main():
    stxt = read('text/student/20160406_stu.txt')
    rtxt = read('text/reviewed/20160406_rev.txt')
    print(stxt, '\n')
    print(rtxt, '\n')
    print(match(stxt, rtxt))

if __name__=='__main__':
    main()