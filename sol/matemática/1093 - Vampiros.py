# 1093 - Vampiros
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1093

from math import ceil


def prob_player2_lose(p, q, n1, n2):
    """Calcula a probabilidade do segundo vampiro perder.
       
       Fonte: https://en.wikipedia.org/wiki/Gambler's_ruin
    """
    if p == q:
        return n1 / (n1 + n2)
    return (1 - (q/p)**n1) / (1 - (q/p)**(n1+n2))
    


def main():
    while True:
        EV1, EV2, AT, D = (int(x) for x in input().split())
        if EV1 == EV2 == 0:
            break
        
        # Faz uma pequena adaptação do problema à formula
        # Calculando proporcionalmente quantas 'fichas' de 1 cada jogador teria
        p, q, n1, n2 = AT/6, (6 - AT)/6, ceil(EV1/D), ceil(EV2/D)

        chance_vamp1_win = prob_player2_lose(p, q, n1, n2) * 100
        print(f"{chance_vamp1_win:0.1f}")


if __name__ == "__main__":
    main()
