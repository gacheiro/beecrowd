# 1287 - Processador Amigável de Inteiros
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1287


def digit(d):
    return {
        'O': '0',
        'o': '0',
        'l': '1',
        ',': '',
        ' ': '',
    }.get(d, d)


def main():
    while True:
        try:
            n = int( ''.join(digit(d) for d in input()) )
            if n < 0 or n > 2147483647:
                raise ValueError
            print(n)

        except EOFError:
            return
        except (TypeError, ValueError):
            print('error')

        
if __name__ == '__main__':
    main()
