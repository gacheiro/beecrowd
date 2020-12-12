# 2044 - Em Dívida
# https://www.urionlinejudge.com.br/judge/pt/problems/view/2044


def main():
    while True:
        n = int(input())
        if n == -1:
            break

        prices = [int(p) for p in input().split()]
        visits, amount = 0, 0
        for p in prices:
            amount += p
            if amount % 100 == 0:
                amount = 0
                visits += 1
        print(visits)


if __name__ == "__main__":
    main()
