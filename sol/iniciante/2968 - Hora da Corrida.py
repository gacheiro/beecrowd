# 2968 - Hora da Corrida
# https://www.urionlinejudge.com.br/judge/pt/problems/view/2968

from math import ceil

P = (0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9)


def main():
  V, N = map(int, input().split())
  total_placas = V * N
  porcentagens = (ceil(total_placas * p) for p in P)
  print(' '.join(str(p) for p in porcentagens))


if __name__ == '__main__':
  main()
