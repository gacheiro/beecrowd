# 2650 - Constrindo Muralhas
# https://www.urionlinejudge.com.br/judge/pt/problems/view/2650


def main():
    n, w = map(int, input().split())
    
    for _ in range(n):
        titan_stats = input().split()
        if int(titan_stats[-1]) > w:
            print(' '.join(titan_stats[:-1]))


if __name__ == '__main__':
    main()
