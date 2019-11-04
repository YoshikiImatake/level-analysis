import re
regex = '[一-龥]'
src = "日本語の漢字だけを置換する"

dst = re.sub('[一-龥]', "z", src)
print(dst)

regex2 = '[ぁ-んァ-ン]'
src = "日本語のひらがなとカタカナを置換する"
dst = re.sub(regex2, "z", src)
print(dst)