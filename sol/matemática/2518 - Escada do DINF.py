# 2528 - Escada do DINF
# https://www.urionlinejudge.com.br/judge/pt/problems/view/2518

import math


def hip(a, b):
    return math.sqrt(a*a + b*b)


def step_surface_area(H, C, L):
    return L * hip(H, C)


def main():
    while True:

        try:
            N = int(input())
        except EOFError:
            return

        H, C, L = map(int, input().split())
        print('{:.4f}'.format(N * step_surface_area(H, C, L) / 10000)) # to m²


if __name__ == '__main__':
    main()
