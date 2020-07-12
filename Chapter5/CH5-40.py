# coding:utf-8
class Morph:
    def __init__(self, mp):
        self.surface = mp['surface']
        self.base = mp['base']
        self.pos = mp['pos']
        self.pos1 = mp['pos1']


def CabochaParser():
    path = 'ai.ja.txt.parsed'
    cabocha = []

    with open(path) as f:
        for line in f:
            tmp_line = line.split('EOS\n')
            tmp_line = list(filter(lambda x: x != '', tmp_line))
            # print(tmp_line)
            for item in tmp_line:
                # print(item)
                if item == '' or item[0] == '*':
                    continue
                (surface, attr) = item.split('\t')
                attr = attr.split(',')
                # print(surface, attr)
                attr_dic = {
                    'surface': surface,
                    'base': attr[6],
                    'pos': attr[0],
                    'pos1': attr[1]
                }
                cabocha.append(Morph(attr_dic))
    return cabocha


def main():
    res = CabochaParser()
    # Morphクラスのインスタンス変数がほしいので、varsで取り出す
    for i in res:
        print(vars(i))


if __name__ == "__main__":
    main()
