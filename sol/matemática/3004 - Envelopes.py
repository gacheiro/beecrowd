# 3004 - Envelopes
# https://www.urionlinejudge.com.br/judge/pt/problems/view/3004


def main():
    n = int(input())
    for _ in range(n):
        a, b, c, d = [int(x) for x in input().split()]
        if (a < c and b < d) or (a < d and b < c):
            print("S")
        else:
            print("N")


if __name__ == "__main__":
    main()
