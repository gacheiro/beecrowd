# 3102 - Kikoho
# https://www.urionlinejudge.com.br/judge/pt/problems/view/3102

from math import sqrt


def dist(x1, y1, x2, y2):
    return sqrt((x1-x2)**2 + (y1-y2)**2)


def main():
    n = int(input())
    for _ in range(n):
        x1, y1, x2, y2, x3, y3 = map(int, input().split())
        # Esse problema pode ser resolvido com a Formula de Heron
        # https://www.todamateria.com.br/area-do-triangulo/

        # Calcula os 3 lados
        a = dist(x1, y1, x2, y2)
        b = dist(x2, y2, x3, y3)
        c = dist(x3, y3, x1, y1)
        # Calcula o semi perimetro
        p = (a+b+c)/2
        # Calcula a area
        s = sqrt(p * (p-a) * (p-b) * (p-c))
        print(f"{s:.3f}")


if __name__ == "__main__":
    main()
