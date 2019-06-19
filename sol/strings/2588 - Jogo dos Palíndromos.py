# 2588 - Jogo dos Palíndromos
# https://www.urionlinejudge.com.br/judge/pt/problems/view/2588

from collections import Counter


def npal(word):
    # conta a ocorrencia de cada letra
    counter = Counter(word)
    
    # conta quantas ocorrencias sao impares
    n_odds = sum(n%2 for n in counter.values())    
    if n_odds == 0 or n_odds == 1:
        return 0
    return n_odds - 1


def main():
    while True:
        try:
            word = input()
            print(npal(word))
        except EOFError:
            return


if __name__ == '__main__':
    main()
