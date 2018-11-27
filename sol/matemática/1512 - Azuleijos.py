# 1512 - Azuleijos
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1512


def mdc(a, b):
    'Greatest Common Divisor'
    if b == 0:
        return a
    return mdc(b, a%b)


def mmc(a, b):
    'Least Common Multiple'
    return a*b//mdc(a, b)


def main():
    while True:
        
        N, A, B = map(int, input().split())
        if N == A == B == 0:
            return
            
        print(N//A + N//B - N//mmc(A, B))


if __name__ == '__main__':
    main()
