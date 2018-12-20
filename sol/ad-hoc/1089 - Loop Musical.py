# 1089 - Loop Musical
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1089


def peaks(sample):
    # add the last in the beginning and the first in the end
    magnitudes = sample[-1:] + sample + sample[:1]
    # loop through a magn, its previous magn, and the next one
    for prev, magn, nxt in zip(magnitudes, magnitudes[1:], magnitudes[2:]):
        # local max, local min
        if (prev < magn > nxt) or (prev > magn < nxt):
            yield magn


def main():
    while True:
        n = int(input())
        if n == 0:
            return

        sample = [int(note) for note in input().split()]
        print(len([p for p in peaks(sample)]))


if __name__ == '__main__':
    main()
