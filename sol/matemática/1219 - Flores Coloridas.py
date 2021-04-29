# 1219 - Flores Coloridas
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1219

from math import sqrt, pi


def heron(a, b, c):
    # https://www.mathopenref.com/heronsformula.html
    p = (a + b + c) / 2
    return sqrt(p * (p - a) * (p - b) * (p - c))


def area_circuncicle(a, b, c):
    # https://www.mathopenref.com/trianglecircumcircle.html
    r = (a * b * c) \
         / sqrt((a + b + c) * (b + c - a) * (c + a - b) * (a + b - c))
    return pi * r*r


def area_incircle(a, b, c):
    # https://www.mathopenref.com/triangleincircle.html
    r = (2 * heron(a, b, c)) / (a + b + c)
    return pi * r*r


def main():
    while True:
        try:
            a, b, c = [int(x) for x in input().split()]
        except EOFError:
            break

        area_with_roses = area_incircle(a, b, c)
        area_with_violets = heron(a, b, c) - area_with_roses
        area_with_sunflowers = area_circuncicle(a, b, c) \
                               - area_with_violets - area_with_roses

        print(f"{area_with_sunflowers:.4f} {area_with_violets:.4f} "
              f"{area_with_roses:.4f}")


if __name__ == "__main__":
    main()
