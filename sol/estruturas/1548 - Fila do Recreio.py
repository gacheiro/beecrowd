# 1548 - Fila do Recreio
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1548


def notas_iguais(notas_a, notas_b):
    'Retorna o número de notas iguais na mesma posição.'
    return sum(1 for a, b in zip(notas_a, notas_b) if a == b)


def main():
    n = int(input())
    for _ in range(n):
        _ = input()
        notas = [int(x) for x in input().split(' ')]
        sorted_notas = sorted(notas, reverse=True)
        print(notas_iguais(notas, sorted_notas))

main()
