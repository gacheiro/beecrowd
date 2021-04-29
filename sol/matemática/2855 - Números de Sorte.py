# 2855 - Números de Sorte
# https://www.urionlinejudge.com.br/judge/pt/problems/view/2855

from bisect import bisect_left


def index(a, x):
    "Locate the index of x, starting from 1"
    return bisect_left(a, x) + 1


def main():
    while True:
        try:
            _ = int(input())
            seq = [int(x) for x in input().split()]
            number = int(input())
        except EOFError:
            break

        drop_every_nth = 2
        number_index = index(seq, number)
        n_dropped_numbers = 0

        while drop_every_nth <= number_index:

            n_dropped_numbers += number_index // drop_every_nth

            if number_index % drop_every_nth == 0:
                print("N")
                break

            number_index = index(seq, number) - n_dropped_numbers
            drop_every_nth += 1

        else:
            print("Y")


if __name__ == "__main__":
    main()
