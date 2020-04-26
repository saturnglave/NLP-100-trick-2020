# coding:utf-8


def cipher(letter):
    ans = ''
    for l in letter:
        if l.islower():
            ans += chr(219 - ord(l))
        else:
            ans += l
    return ans


def main():
    s = input()
    print(cipher(s))


if __name__ == "__main__":
    main()
