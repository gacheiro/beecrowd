# 3257 - Plantando Árvores
# https://www.urionlinejudge.com.br/judge/pt/problems/view/3257


def main():
    _ = input()
    list_of_days_to_grow = [int(d) for d in input().split()]
    list_of_days_to_grow.sort(reverse=True)

    makespan = \
        1 + max(d + g for d, g in enumerate(list_of_days_to_grow, start=1))

    print(makespan)


if __name__ == "__main__":
    main()
