# coding:utf-8
# split -l 1000 popular-names.txt
import argparse
import pandas as pd
import numpy as np


def arg():
    parser = argparse.ArgumentParser(description="自然数")
    parser.add_argument('n', help='num')

    args = parser.parse_args()
    return args.n


def main():
    path = './popular-names.txt'
    n = int(arg())
    df = pd.read_csv(path, sep='\t', header=None)

    chunks = np.split(df, n)

    for i in range(n):
        print(chunks[i])


if __name__ == "__main__":
    main()
