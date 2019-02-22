# 2930 - Presentes Suspeitos
# https://www.urionlinejudge.com.br/judge/pt/problems/view/2931


def main():
    while True:
        try:
            c, k = map(int, input().split())
        except EOFError:
            return

        suspect_comb = {}
        for _ in range(c):
            p, suspects = input(), set()

            for __ in range( int(input()) ):
                suspects.add(input())

            suspect_comb[p] = suspects

        for _ in range(k):
            wished, received = input().split(';')
            print('Y' if received in suspect_comb.get(wished, {}) else 'N')


if __name__ == '__main__':
    main()
