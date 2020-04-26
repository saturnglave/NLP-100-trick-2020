# coding:utf-8


def n_gram(num, sentence):
    ans = []
    for i in range(len(sentence)):
        ans.append(sentence[i:i + num])
    return(ans)


def main():
    s = "I am an NLPer"
    w = s.split()
    print("文字列n-gram")
    print(n_gram(2, s))
    print("単語n-gram")
    print(n_gram(2, w))


if __name__ == "__main__":
    main()
