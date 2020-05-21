# coding:utf-8


def neko_load():
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
                morpheme = {'surface': tmp_line[0],
                            'base': tmp[6],
                            'pos': tmp[0],
                            'pos1': tmp[1]}
                sentence.append(morpheme)
    return(neko)


def main():
    cat = neko_load()
    # print(cat)
    ans = []

    for line in cat:
        if (n := len(line)) >= 2:
            tmp = ''
            count = 0
            # 名詞が連続している部分を探す
            for i in range(n):
                if line[i]['pos'] == '名詞':
                    tmp += line[i]['surface']
                    count += 1
                # 名詞が2つ以上続いた時だけ答えに入れる
                elif line[i]['pos'] != '名詞' and tmp != '' and count >= 2:
                    ans.append(tmp)
                    tmp = ''
                    count = 0
                # 名詞がひとつ来てその次名詞以外だった場合はリセット
                elif line[i]['pos'] != '名詞' and tmp != '' and count == 1:
                    tmp = ''
                    count = 0

    print(ans)


if __name__ == "__main__":
    main()
