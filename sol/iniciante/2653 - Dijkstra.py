# 2653 - Dijkstra
# https://www.urionlinejudge.com.br/judge/pt/problems/view/2653


def main():
  joias = set()
  while True:
    try:
      joias.add(input())
    except EOFError:
      print(len(joias))
      return

if __name__ == '__main__':
  main()
