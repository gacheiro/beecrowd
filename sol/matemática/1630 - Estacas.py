# 1630 - Estacas
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1630


def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a%b)


def main():
    while True:
        try:
            x, y = map(int, input().split())
        except EOFError:
            break

        n = (x*2 + y*2) // mdc(x, y)
        print(n)


if __name__ == "__main__":
    main()
