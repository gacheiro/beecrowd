# 1986 - Perdido em Marte
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1986


def main():
    
    _ = input()
    msg_int = [int(x, 16) for x in input().split()]

    print(''.join(chr(x) for x in msg_int))


if __name__ == '__main__':
    main()
