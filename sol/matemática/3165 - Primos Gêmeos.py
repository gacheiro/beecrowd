# 3165 - Primos Gêmeos
# https://www.urionlinejudge.com.br/judge/pt/problems/view/3165

from math import sqrt, ceil


def is_prime(x):
    for n in range(2, ceil(sqrt(x)) + 1):
        if x % n == 0:
            return False
    return True


def main():
    x = int(input())
    for y in range(x, 4, -1): # from x to 5
        if is_prime(y - 2) and is_prime(y):
            print(y - 2, y)
            break


if __name__ == "__main__":
    main()
