# 1641 - Restaurante e Pizzaria do Alfredo
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1641

from math import sqrt


def main():
    p = 1
    while True:
        try:
            R, W, L = map(int, input().split())
        except ValueError:
            break
        
        if 2*R >= sqrt(W**2 + L**2):
            print(f"Pizza {p} fits on the table.")
        else:
            print(f"Pizza {p} does not fit on the table.")
        p += 1


if __name__ == "__main__":
    main()
