# 2927 - Imprevistos Natalinos
# https://www.urionlinejudge.com.br/judge/pt/problems/view/2927

def main():
    a, c, x, y = map(int, input().split())

    if (c - x - y) < a + 1 and x > y/2.0:
        print('Caio, a culpa eh sua!')
    elif (c - x - y) < a + 1:
        print('Igor bolado!')
    else:
        print('Igor feliz!')


if __name__ == '__main__':
    main()
