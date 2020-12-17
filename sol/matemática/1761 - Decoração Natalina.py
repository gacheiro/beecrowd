# 1761 - Decoração Natalina
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1761

from math import tan, radians


def main():
    while True:
        try:
            A, B, C = map(float, input().split())
        except EOFError:
            break
        
        D = (tan(radians(A)) * B + C) * 5
        print(f"{D:.2f}")


if __name__ == "__main__":
    main()
