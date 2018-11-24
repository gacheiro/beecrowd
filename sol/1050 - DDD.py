# 1050 - DDD
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1050


def city(ddd, default='DDD nao cadastrado'):
    return {
        61: 'Brasilia',
        71: 'Salvador',
        11: 'Sao Paulo',
        21: 'Rio de Janeiro',
        32: 'Juiz de Fora',
        19: 'Campinas',
        27: 'Vitoria',
        31: 'Belo Horizonte',
    }.get(ddd, default)


def main():
    ddd = int(input())
    print(city(ddd))


if __name__ == '__main__':
    main()
