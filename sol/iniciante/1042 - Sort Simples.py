# 1042 - Sort Simples
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1042


def main():
    values = input().split()

    print('\n'.join(sorted(values, key=int)), end='\n\n')
    print('\n'.join(values))


if __name__ == '__main__':
    main()
    