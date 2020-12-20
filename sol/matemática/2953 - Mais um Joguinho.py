# 2953 - Mais um Joguinho
# https://www.urionlinejudge.com.br/judge/pt/problems/view/2953


def main():
    n = int(input())
    comb = [0]*100_001
    # começa a partir da casa 1
    comb[3] = 1    # movimento de 2
    comb[4] = 1    # movimento de 3

    for i in range(0, n):
        for s in (2, 3):
            if i + s > n: # passa do fim
                break
            comb[i+s] += comb[i]
            comb[i+s] %= (10**9+7)
    print(comb[n])


if __name__ == "__main__":
    main()
