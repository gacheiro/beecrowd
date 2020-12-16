# 1909 - Ajude Kiko
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1909

from functools import reduce


def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a%b)


def mmc_(a, b):
    return a*b//mdc(a, b)


def next_ball(balls, mmc, T):
    for i in range(2, T+1):
        if mmc_(i, mmc) == T and i not in balls:
            return i


def main():
    while True:
        N, T = map(int, input().split())
        if N == T == 0:
            break

        balls = {int(x) for x in input().split()}
        mmc = reduce(mmc_, balls, 1)
        if b := next_ball(balls, mmc, T):
            print(b)
        else:
            print("impossivel")


if __name__ == "__main__":
    main()
