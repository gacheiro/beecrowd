# 1785 - Kaprekar
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1785


def kaprekar(x):
    cnt = 0
    while x != 6174:
        x_str = f"{x:0>4}"
        maior = "".join(sorted(x_str, reverse=True))
        menor = "".join(sorted(x_str))

        x = int(maior) - int(menor)
        cnt += 1
    return cnt


def main():
    n = int(input())
    for i in range(1, n+1):
        x = int(input())
        print(f"Caso #{i}: ", end="")
        if len(set(f"{x:0>4}")) < 2:
            print(-1)
        else:
            x = int(x)
            print(kaprekar(x))
    

if __name__ == "__main__":
    main()
