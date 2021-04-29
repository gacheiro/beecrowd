# 2840 - Balão++
# https://www.urionlinejudge.com.br/judge/pt/problems/view/2840

PI = 3.1415


def main():
    R, L = [int(x) for x in input().split()]
    vol = 4/3 * PI*R**3
    print(f"{L//vol:.0f}")


if __name__ == "__main__":
    main()
