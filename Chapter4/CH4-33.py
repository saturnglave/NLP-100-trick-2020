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
    a_no_b = []
    # print(cat[0])
    for line in cat:
        if (n := len(line)) >= 3:
            for i in range(n - 2):
                if line[i]['pos'] == '名詞' and (line[i + 1]['pos'] == '助詞' and line[i + 1]['surface'] == 'の') and line[i + 2]['pos'] == '名詞':
                    a_no_b.append(line[i]['surface'] + 'の' + line[i + 2]['surface'])

    print(a_no_b)


if __name__ == "__main__":
    main()
