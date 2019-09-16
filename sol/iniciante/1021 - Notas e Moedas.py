# 1021 - Notas e Moedas
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1021

NOTAS = (100, 50, 20, 10, 5, 2)
MOEDAS = (1, 0.50, 0.25, 0.10, 0.05, 0.01)


def main():
  valor = float(input())

  print("NOTAS:")
  for nota in NOTAS:
      quantidade_notas = int(valor / nota)
      print("{} nota(s) de R$ {:.2f}".format(quantidade_notas, nota))
      valor -= quantidade_notas * nota

  print("MOEDAS:")
  for moeda in MOEDAS:
      quantidade_moedas = int(round(valor,2) / moeda)
      print("{} moeda(s) de R$ {:.2f}".format(quantidade_moedas, moeda))
      valor -= round(quantidade_moedas * moeda, 2)

if __name__ == '__main__':
  main()
