# 1943 - Top N
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1943

from itertools import dropwhile

def main():
    tops = (1, 3, 5, 10, 25, 50, 100)
    n = int(input())
    # I like using dropwhile here instead of several if's or a loop
    # because it feels more functional
    top = next(dropwhile(lambda x: x < n, tops)) # get the fst elem x | x >= n

    print('Top {}'.format(top))


if __name__ == '__main__':
    main()
