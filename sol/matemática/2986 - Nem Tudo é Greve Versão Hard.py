# 2968 - Nem Tudo é Greve Versão Hard
# https://www.urionlinejudge.com.br/judge/pt/problems/view/2986


def main():
    n = int(input())
    comb = [0]*100_001
    comb[1] = 1
    comb[2] = 1
    comb[3] = 1

    for i in range(0, n):
        for s in (1, 2, 3):
            if i + s > n: # passa da escada
                break
            comb[i+s] += comb[i]
            comb[i+s] %= (10**9+7)
    print(comb[n])


if __name__ == "__main__":
    main()
