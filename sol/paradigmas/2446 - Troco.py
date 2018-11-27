# 2446 - Troco (Programação Dinâmica)
# https://www.urionlinejudge.com.br/judge/pt/problems/view/2446


def can_pay(value, coins):
    values = [False] * (value + 1)
    values[0] = True # we can always pay 0

    for c in coins:
        for i in range(value, c - 1, -1):
            # we can only pay value i if we can pay i - c already
    #        print('can pay {}, so we can pay {} if we add {}'.format(i-c, i, c))
            if values[i - c]:
                values[i] = True
                if i == value:
                    return True          

    return False


def main():
    v, _ = map(int, input().split())
    coins = map(int, input().split())

    print('S' if can_pay(v, coins) else 'N')


if __name__ == '__main__':
    main()
