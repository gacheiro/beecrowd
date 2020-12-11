# 1367 - Ajude!
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1367

from collections import defaultdict


def main():
    while True:
        n = int(input())
        if n == 0:
            break

        incorrect = defaultdict(lambda: 0) # conta quantas respostas incorretas
        correct = defaultdict(lambda: 0)   # guarda o tempo da resposta correta
        
        for _ in range(n):
            id, time, status = input().split()

            if status == "incorrect":
                incorrect[id] += 1
            else:
                correct[id] = int(time) + incorrect[id]*20

        print(len(correct), sum(correct.values()))


if __name__ == "__main__":
    main()
