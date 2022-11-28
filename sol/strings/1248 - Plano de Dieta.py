# 1248 - Plano de Dieta
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1248

from itertools import chain
from collections import Counter


def main():
    n = int(input())

    for _ in range(n):
        diet = Counter(input())
        eaten = Counter(chain(input(), input()))

        if any(f not in diet or eaten[f] > diet[f] for f in eaten):
            print("CHEATER")
            continue

        for f in sorted(diet):
            missing = diet[f] - eaten[f]
            print(f*missing, end="")
        print()


if __name__ == "__main__":
    main()
