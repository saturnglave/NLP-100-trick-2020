# coding:utf-8
# mecab neko.txt > neko.txt.mecab
# 表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音
path = './neko.txt.mecab'
neko = []
sentence = []

with open(path) as f:
    for line in f:
        # [表層系, それ以外]として一行の中身をリスト化
        tmp_line = line.rstrip('\n').split('\t')
        # EOSの部分で一文とカウント。EOSだった場合はsentenceに何も入らない
        if len(tmp_line) == 1 and len(sentence) != 0:
            neko.append(sentence)
            sentence = []
        elif len(tmp_line) == 2:
            # 品詞以降の部分をカンマ区切りする
            tmp = tmp_line[1].split(',')
            # print(tmp[5])
            morpheme = {'surface': tmp_line[0],
                        'base': tmp[6],
                        'pos': tmp[0],
                        'pos1': tmp[1]}
            sentence.append(morpheme)


print(neko)
