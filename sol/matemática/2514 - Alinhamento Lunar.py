# 2514 - Alinhamento Lunar
# https://www.urionlinejudge.com.br/judge/pt/problems/view/2514


def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a%b)


def mmc(a, b):
    return a*b//mdc(a, b)


def main():
    while True:
        try:
            m = int(input())
        except EOFError:
            break

        l1, l2, l3 = map(int, input().split())
        n = mmc(l1, mmc(l2, l3)) - m
        print(n)


if __name__ == "__main__":
    main()
