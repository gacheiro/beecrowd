# 2864 - Qual é a Altura?
# https://www.urionlinejudge.com.br/judge/pt/problems/view/2864


def delta(a, b, c):
    return b*b - 4*a*c


def main():
    n = int(input())
    for _ in range(n):
        a, b, c = [int(x) for x in input().split()]
        max_y = -delta(a, b, c) / (4*a)
        print(f"{max_y:.2f}")


if __name__ == "__main__":
    main()
