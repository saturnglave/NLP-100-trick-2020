# coding:utf-8


def n_gram(num, sentence):
    ans = []
    for i in range(len(sentence)):
        ans.append(sentence[i:i + num])
    return(ans)


def is_se(sentence):
    if 'se' in sentence:
        return True
    return False


def main():
    s1 = "paraparaparadise"
    s2 = "paragraph"

    x = set(n_gram(2, s1))
    y = set(n_gram(2, s2))
    print('X')
    print(x)
    print('Y')
    print(y)

    print("和集合")
    print(x | y)
    print("積集合")
    print(x & y)
    print("差集合")
    print(x - y)

    print('x: ', is_se(x))
    print('y: ', is_se(y))


if __name__ == "__main__":
    main()
