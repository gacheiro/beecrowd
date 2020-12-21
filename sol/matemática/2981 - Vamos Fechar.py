# 2981 - Vamos Fechar
# https://www.urionlinejudge.com.br/judge/pt/problems/view/2981


def main():
    c, g = map(int, input().split())
    days = c//g

    if days < 10:
        print(f"A UFSC fecha dia {21 + days} de setembro.")
    else:
        print(f"A UFSC fecha dia {days - 9} de outubro.")


if __name__ == "__main__":
    main()
