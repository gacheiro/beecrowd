# 2489 - Flecha no Coelho
# https://www.urionlinejudge.com.br/judge/pt/problems/view/2489

from math import radians, tan


def main():
    while True:
        try:
            A, D, R = [float(x) for x in input().split()]
        except EOFError:
            break

        if R == 90:
            H = A
        elif R > 90:
            r = R - 90
            h = tan(radians(r)) * D
            H = A + h
        elif R < 90:
            r = 90 - R
            h = tan(radians(r)) * D
            H = A - h
        print("{:.4f}".format(H))


if __name__ == "__main__":
    main()
