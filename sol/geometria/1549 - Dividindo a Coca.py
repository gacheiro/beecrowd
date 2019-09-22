# 1549 - Dividindo a Coca
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1549

import math

EPS = 0.0001


def volume_tronco_cone(h, B, b):
    return (h * math.pi/3) * (B**2 + B*b + b**2)


def bsearch(H, b, B, pessoas, vol_coca):
    first, last = 0, H
    while first <= last:
        h = (first + last) / 2.0
        # calcula o raio da base intermediária (entre B e b)
        Bb = b + (B-b)*(h/H)
        # calcula o volume de coca de todos os copos com altura h
        coca = volume_tronco_cone(h, Bb, b) * pessoas
        if abs(vol_coca - coca) <= EPS:
            return h
        elif coca < vol_coca:
            first = h
        else:
            last = h


def main():
    C = int(input())
    for _ in range(C):
        N, L = map(int, input().split())
        b, B, H = map(int, input().split())
        h = bsearch(H, b, B, N, L)
        print('{:.2f}'.format(h))
        

if __name__ == '__main__':
    main()
