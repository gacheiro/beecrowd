# 2958 - O Rolê Bad Vibes
# https://www.urionlinejudge.com.br/judge/pt/problems/view/2958


def main():
    n, m = map(int, input().split())
    life_problems = []
    school_problems = []

    for _ in range(n):
        problems = input().split()
        for p in problems:
            if p.endswith('V'):
                life_problems.append(p)
            else:
                school_problems.append(p)

    life_problems.sort(reverse=True)
    school_problems.sort(reverse=True)
    print('\n'.join(life_problems))
    print('\n'.join(school_problems))


if __name__ == '__main__':
    main()
