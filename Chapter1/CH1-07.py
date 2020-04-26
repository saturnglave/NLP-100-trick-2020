# coding:utf-8
import argparse


def arg():
    parser = argparse.ArgumentParser(description='x時のyはz 引数3つ')
    parser.add_argument('x', help='num')
    parser.add_argument('y', help='string')
    parser.add_argument('z', help='num')

    args = parser.parse_args()
    ans = args.x + '時の' + args.y + 'は' + args.z

    return(ans)


def main():
    print(arg())


if __name__ == "__main__":
    main()
