# 1309 - Formatação Monetária
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1309


def main():
    while True:
        try:
            v = input()
            c = input()
        except EOFError:
            break

        print("$", end="")
        # Separa as partes da string em bilhão, milhão, etc
        f = v[-12:-9], v[-9:-6], v[-6:-3], v[-3:]
        print(",".join(x for x in f if x != ""), end=".")
        print(f"{c:0>2}")


if __name__ == '__main__':
    main()
