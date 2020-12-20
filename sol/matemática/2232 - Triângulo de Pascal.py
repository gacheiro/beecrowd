# 2232 - Triângulo de Pascal
# https://www.urionlinejudge.com.br/judge/pt/problems/view/2232


def main():
    n = int(input())
    for _ in range(n):
        i = int(input())
        print(2**i - 1)


if __name__ == "__main__":
    main()
