# 1424 - Problema Fácil de Rujia Liu?
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1424

from collections import Counter


def main():
    while True:
        try:
            n, m = map(int, input().split())
            values = map(int, input().split())
        except EOFError:
            break
        
        counter = Counter()
        index_count = {}

        for i, value in enumerate(values, start=1):
            counter[value] += 1
            key = '{} {}'.format(counter[value], value)
            index_count[key] = i

        for _ in range(m):
            key = input()
            if key in index_count:
                print(index_count[key])
            else:
                print('0')


if __name__ == '__main__':
    main()
