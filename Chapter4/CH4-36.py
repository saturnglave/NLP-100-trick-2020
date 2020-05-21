# coding:utf-8
import collections
import matplotlib.pyplot as plt


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
    cat_word = []

    for line in cat:
        for word in line:
            cat_word.append(word['surface'])

    # 句読点、空白を抜く
    cat_word = [item for item in cat_word if item != '、' and item != '。'
                and item != '\u3000' and item != '「' and item != '」']
    # print(cat_word)
    count_cat = collections.Counter(cat_word)
    top10 = count_cat.most_common(10)
    # print(top10)
    top10_word = [item[0] for item in top10]
    top10_count = [item[1] for item in top10]
    print(top10_word)
    print(top10_count)
    plt.bar(top10_word, top10_count)
    plt.title('頻度上位10語')
    plt.show()


if __name__ == "__main__":
    main()
