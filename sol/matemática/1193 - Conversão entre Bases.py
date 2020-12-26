# 1193 - Conversão entre Bases
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1193


def main():
    n = int(input())
    for i in range (1, n+1):
        x, base = input().split()

        print(f"Case {i}:")
        if base == "dec":
            x = int(x)
            h = hex(x)[2:]
            b = bin(x)[2:]
            print(f"{h} hex\n{b} bin\n")

        elif base == "hex":
            d = x = int(x, base=16)
            b = bin(x)[2:]
            print(f"{d} dec\n{b} bin\n")

        else:
            d = x = int(x, base=2)
            h = hex(x)[2:]
            print(f"{d} dec\n{h} hex\n")
        

main()
