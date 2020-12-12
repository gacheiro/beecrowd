# 3049 - Nota Cortada
# https://www.urionlinejudge.com.br/judge/pt/problems/view/3049


def main():
    b = int(input())
    t = int(input())

    area_felix = (b + t) / 2 * 70
    area_marzia = (160 - b + 160 - t) / 2 * 70

    if area_felix > area_marzia:
        print(1)
    elif area_felix < area_marzia:
        print(2)
    else:
        print(0)


if __name__ == "__main__":
    main()
