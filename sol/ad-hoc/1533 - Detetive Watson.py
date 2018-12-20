# 1533 - Detetive Watson
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1533


def main():
    while True:
        n = int(input())
        if n == 0:
            return

        suspects = map(int, input().split())
        sorted_suspects = sorted(
            # use enumerate here to pack the index together
            enumerate(suspects, 1), key=lambda s: s[1], reverse=True)
        print(sorted_suspects[1][0]) # print the index of the snd most suspect


if __name__ == '__main__':
    main()
