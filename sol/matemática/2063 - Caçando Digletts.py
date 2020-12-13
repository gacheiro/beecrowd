# 2063 - Caçando Digletts
# https://www.urionlinejudge.com.br/judge/pt/problems/view/2063

from functools import reduce


def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a%b)


def mmc(a, b):
    return a*b//mdc(a, b)


def main():
    n = int(input())
    holes = [int(x) for x in input().split()]
    
    loops = set()
    for i in range(n):
        # Conta quanto tempo cada diglett leva pra sair e voltar pro seu buraco
        p = i
        t = 1
        while holes[p] - 1 != i: # -1 pois a lista começa no indice 0
            p = holes[p] - 1
            t += 1
        loops.add(t)

    print(reduce(mmc, loops, 1))


if __name__ == '__main__':
    main()
