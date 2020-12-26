# 1306 - Numerando Estradas
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1306

from math import ceil


def main():
    c = 1
    while True:
        R, N = map(int, input().split())
        if R == N == 0:
            break
        
        # Cada numero + letra faz 27 combinações
        if N*27 < R: 
            print(f"Case {c}: impossible")
        else:
            print(f"Case {c}: {ceil(R/N - 1)}")
        c += 1


if __name__ == "__main__":
    main()
