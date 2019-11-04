from functools import lru_cache
import sys
sys.setrecursionlimit(10000)

@lru_cache(maxsize=4090)
def ld(s, t):
    '''文字列のレーベンシュタイン距離を計算する'''

    #一方が空文字列なら、他方の長さが求める距離になる。
    if not s: return len(t)
    if not t: return len(s)
    
    #一文字目が一致なら、2文字目以降の距離が求める距離になる。
    if s[0] == t[0]: return ld(s[1:], t[1:])

    #一文字目が不一致なら、追加/削除/置換のそれぞれを実施し、
    #残りの文字列についてのコストを計算する。

    #sの先頭に追加
    l1 = ld(s, t[1:])

    #sの先頭を削除
    l2 = ld(s[1:], t)

    #sの先頭を置換
    l3 = ld(s[1:], t[1:])

    #追加/削除/置換を実施した分コスト(距離)1の消費は確定
    #残りの文字列についてのコストの最小値を足せば距離となる
    return 1 + min(l1, l2, l3)

def lds(s, t):
    '''標準化されたレーベンシュタイン距離を計算する'''
    return ld(s,t) / max(len(s), len(t))

def main():
    '''テスト用。一組のテキストファイルを対象に距離の測定を行う'''
    stxt = ''
    with open('text/student/41394_stu.txt', mode='r', encoding='utf-8')as sfin:
        for srow in sfin:
            stxt += srow
    rtxt = ''
    with open('text/reviewed/41394_rev.txt', mode='r', encoding='utf-8')as rfin:
        for rrow in rfin:
            rtxt += rrow
    s = stxt.split("。")
    t = rtxt.split("。")
    for (s, t) in zip(s, t):
        print(lds(s,t), '\n')
    #print("Levenshtein:",ld(stxt, rtxt))


if __name__ == '__main__':
    main()
