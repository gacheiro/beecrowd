# 1307 - Tudo o que Você Precisa e Amor
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1307


def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a%b)


def main():
    n = int(input())
    for i in range(1, n+1):
        s1 = int(input(), base=2)
        s2 = int(input(), base=2)
        if mdc(s1, s2) > 1:
            print(f"Pair #{i}: All you need is love!")
        else:
            print(f"Pair #{i}: Love is not all you need!")


if __name__ == '__main__':
    main()
