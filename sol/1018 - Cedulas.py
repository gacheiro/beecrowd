# 1018 - Cédulas
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1018


# count_banknotes(Tuple[int, ...], int) -> Iterator[Tuple(int, int)]
def count_banknotes(banknotes, value):
    counter = {}
    for bkn in banknotes:
        counter[bkn] = value // bkn
        value %= bkn
    return sorted(counter.items(), key=lambda x: x[0], reverse=True)


def main():
    value = int(input())
    banknotes = (100, 50, 20, 10, 5, 2, 1)

    print(value)
    for bkn, count in count_banknotes(banknotes, value):
        print('{} nota(s) de R$ {},00'.format(count, bkn))


if __name__ == '__main__':
    main()
