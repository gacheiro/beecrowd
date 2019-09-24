# 2091 - Número Solitário
# https://www.urionlinejudge.com.br/judge/pt/problems/view/2091

from functools import reduce


def xor(a, b):
    return a ^ b


def main():
    while True:
        n = int(input())
        if n == 0:
            break
        values = map(int, input().split())
        print(reduce(xor, values))


if __name__ == '__main__':
    main()
