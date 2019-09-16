# 2557 - R+L=J
# https://www.urionlinejudge.com.br/judge/pt/problems/view/2557

import re


def main():
  while True:
    try:
      expr = input()
      R, L, J = re.match(r'([\w]+)\+([\w]+)=([\w]+)', expr).groups()            
      if R == 'R':
        print(int(J) - int(L))
      elif L == 'L':
        print(int(J) - int(R))
      elif J == 'J':
        print(int(R) + int(L))
    except EOFError:
      return


if __name__ == '__main__':
  main()
