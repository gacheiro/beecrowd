# 2963 - Bobo da Corte
# https://www.urionlinejudge.com.br/judge/pt/problems/view/2963


def main():
  n = int(input())
  votos_carlos = int(input())
  for _ in range(n - 1):
      if votos_carlos < int(input()):
          print('N')
          break
  else:
    print('S')


if __name__ == '__main__':
  main()
