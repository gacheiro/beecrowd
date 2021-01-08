# 1371 - Fechem as Portas!
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1371

from math import sqrt
from itertools import takewhile


def main():

    numeros_com_impar_divisores = {1} # Uma porta so fica aberta se tiver
                                        # uma quantidade de divisores impar :)
    for x in range(2, int(sqrt(25_000_000)) + 1):
        exp = 2                     # Um numero possui uma quantidade impar de divisores
                                    # se ele for uma potência de expoente par (ou exp 0)
        while x**exp <= 25_000_000:
            numeros_com_impar_divisores.add(x**exp)
            exp += 2
    
    # Deixa tudo pronto para a saida
    results = list(sorted(numeros_com_impar_divisores))

    while True:
        n = int(input())
        if n == 0:
            break
        
        # Seleciona e imprime apenas as portas no intervalo [1..n]
        output = takewhile(lambda x: x <= n, results)
        print(" ".join(str(x) for x in output))


if __name__ == "__main__":
    main()
