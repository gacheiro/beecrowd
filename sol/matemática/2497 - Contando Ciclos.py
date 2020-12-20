# 2497 - Contando Ciclos
# https://www.urionlinejudge.com.br/judge/pt/problems/view/2497


def main():
    i = 1
    while True:
        n = int(input())
        if n == -1:
            break

        print(f"Experiment {i}: {n//2} full cycle(s)")
        i += 1


if __name__ == "__main__":
    main()
