# 2667 - Jogo de Boca
# https://www.urionlinejudge.com.br/judge/pt/problems/view/2667


def mod_3(str_n):
    return sum(int(d) for d in str_n) % 3


def main():
    str_n = input()
    r = mod_3(str_n)
    print(r)


if __name__ == "__main__":
    main()
