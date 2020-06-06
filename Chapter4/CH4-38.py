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
    cat_word = []

    # 単語を抽出
    for line in cat:
        for word in line:
            cat_word.append(word['surface'])

    # 句読点、空白、記号類を抜く
    cat_word = [item for item in cat_word if item != '、' and item != '。'
                and item != '\u3000' and item != '「' and item != '」']
    # print(cat_word)

    count_cat = collections.Counter(cat_word)
    cat_freq = count_cat.most_common()
    # print(cat_freq)
    # 出現数だけリスト化
    cat_list = list(zip(*cat_freq))[1]
    print(cat_list)

    plt.hist(cat_list, bins=20, range=(1, 20), color='salmon', ec='darkred')
    plt.title('吾輩は猫である　単語出現頻度')
    plt.xlim(xmin=1, xmax=20)
    plt.xticks([1, 5, 10, 15, 20])
    plt.xlabel('出現頻度')
    plt.ylabel('単語の種類数')
    plt.show()


if __name__ == "__main__":
    main()
