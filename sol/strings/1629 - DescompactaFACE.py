# 1629 - DescompactaFACE
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1629


def dig_verificador(compact):
    # soma os indices pares
    # e os indices impares
    n_zeros = sum(int(z) for z in compact[0::2])
    n_uns = sum(int(u) for u in compact[1::2])

    concat_zeros_uns = str(n_zeros) + str(n_uns)
    return sum(int(d) for d in concat_zeros_uns)


def main():
    while True:
        n = int(input())
        if n == 0:
            break
            
        for _ in range(n):
            compact = input()
            print(dig_verificador(compact))


if __name__ == '__main__':
    main()
