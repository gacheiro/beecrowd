# 1277 - Pouca Frequência
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1277


def main():
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        names = input().split()
        freqs = input().split()

        output = ""
        for name, f in zip(names, freqs):
            if f.count("A") / (f.count("P") + f.count("A")) > 0.25:
                output += name + " "
        print(output.rstrip()) # remove o espaço em branco apos o ultimo nome


if __name__ == "__main__":
    main()
