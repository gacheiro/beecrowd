# 1737 - Etaoin Shrdlu
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1737

from collections import Counter


def main():
    while True:
        n = int(input())
        if n == 0:
            break

        phrase = ""
        for _ in range(n):
            phrase += input()

        # Monta e conta as combinações de digrafos
        digrams = [a+b for a, b in zip(phrase, phrase[1:])]
        total = len(digrams)
        counter = Counter(digrams)
        
        # Primeiro ordena em ordem alfabética
        most_common = sorted(counter.most_common(), key=lambda x: x[0])
        # Depois ordena em ordem de ocorrência
        most_common.sort(key=lambda x: x[1], reverse=True)
        for di, count in most_common[:5]:
            print("{} {} {:.6f}".format(di, count, count/float(total)))
        print()


if __name__ == "__main__":
    main()
