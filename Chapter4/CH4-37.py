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

    # 単語を抽出。今回は猫と同じ文に出てきた名詞と動詞のみ抽出
    for line in cat:
        if any(word['surface'] == '猫' for word in line):
            for word in line:
                if word['pos'] == '名詞' or word['pos'] == '動詞':
                    cat_word.append(word['surface'])

    # 句読点、空白、'猫'を抜く
    cat_word = [item for item in cat_word if item != '、' and item != '。'
                and item != '\u3000' and item != '「' and item != '」' and item != '猫']
    # print(cat_word)

    count_cat = collections.Counter(cat_word)
    top10 = count_cat.most_common(10)

    top10_word = [item[0] for item in top10]
    top10_count = [item[1] for item in top10]

    plt.bar(top10_word, top10_count)
    plt.title('猫と共起する単語上位10語')
    plt.show()


if __name__ == "__main__":
    main()
