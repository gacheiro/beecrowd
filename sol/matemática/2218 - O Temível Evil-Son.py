# 2218 - O Temível Evil-Son
# https://www.urionlinejudge.com.br/judge/pt/problems/view/2218


def f(n):
    # a ideia é que cada reta n adicionada corta todas as
    # outras retas em **algum ponto** no plano
    # gerando n novas regiões
    # infelizmente essa função recursiva não passa no uri.

    # casos bases f(0) = 0; f(1) == 2
    if n == 0:
        return 0
    elif n == 1:
        return 2
    return f(n-1) + n


def f_iterativa(n):
    if n == 0:
        return 0
    return sum(range(2, n+1), start=2)


def main():
    n = int(input())
    for _ in range(n):
        i = int(input())
        print(f_iterativa(i))


if __name__ == "__main__":
    main()
