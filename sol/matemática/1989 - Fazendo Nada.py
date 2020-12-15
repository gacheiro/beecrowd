# 1989 - Fazendo Nada
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1989


def main():
    while True:
        N, M = map(int, input().split())
        if N == M == -1:
            break

        episodes = map(int, input().split())
        # Duração do ep * sum(quantidade de episodios e * numero de vezes que ira assitir t)
        total_time = M * sum(e*t for e, t in zip(episodes, range(N, 0, -1)))
        print(total_time)


if __name__ == '__main__':
    main()
