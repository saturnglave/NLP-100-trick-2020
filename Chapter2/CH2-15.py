# coding:utf-8
# tail -n 3 popular-names.txt
import argparse
import pandas as pd


def arg():
    parser = argparse.ArgumentParser(description='自然数')
    parser.add_argument('n', help='num')
    args = parser.parse_args()
    return(args.n)


def main():
    path = './popular-names.txt'
    n = int(arg())
    df = pd.read_csv(path, sep='\t', header=None)
    print(df[-n:])
    # print(df.tail(n))


if __name__ == "__main__":
    main()
