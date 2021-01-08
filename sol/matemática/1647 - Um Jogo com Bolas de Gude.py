# 1647 - Um Jogo com Bolas de Gude
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1647


def main():
    while True:
        n = int(input())
        if n == 0:
            break
        balls = [int(x) for x in input().split()]
        for i in range(len(balls)-1, 0, -1):
            for j in range(i):
                balls[j] += balls[i]

        print(sum(balls))


if __name__ == "__main__":
    main()
