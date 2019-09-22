# 1124 - Elevador
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1124

from math import sqrt, pow
 

def cabe(L, C, R):
    return R*2 <= L and R*2 <= C


def dist(a, b):
    return sqrt(pow(b[0] - a[0], 2) + pow(b[1] - a[1], 2))


def main():
    while True:
        L, C, R1, R2 = map(int, input().split())
        if L == C == R1 == R2 == 0:
            break
        # coloca um cilindro no canto superior esquerdo (0, 0)
        centro_cilindro_1 = (R1, R1)
        # e o outro cilindro no canto inferior direito
        centro_cilindro_2 = (C - R2, L - R2)
        # então verifica se os dois NÃO se sobrepõem
        if (cabe(L, C, R1) and cabe(L, C, R2)
            and dist(centro_cilindro_1, centro_cilindro_2) >= R1 + R2):
                print('S')
        else:
            print('N')


if __name__ == '__main__':
    main()
