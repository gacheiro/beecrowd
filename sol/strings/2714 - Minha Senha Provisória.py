# 2714 - Minha Senha Provisória
# https://www.urionlinejudge.com.br/judge/pt/problems/view/2714

def is_valid(s):
    return (s.startswith('RA') and len(s) == 20)


def main():
    n = int(input())
    for _ in range(n):
        pwrd = input()
        if is_valid(pwrd):
            print(int(pwrd[2:]))
        else:
            print('INVALID DATA')


if __name__ == '__main__':
    main()
