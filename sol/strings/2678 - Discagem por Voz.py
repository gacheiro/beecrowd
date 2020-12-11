# 2678 - Discagem por Voz
# https://www.urionlinejudge.com.br/judge/pt/problems/view/2678


def decode(x):
    if x.isdigit() or x in "*#":
        return x
    elif x in "ABC":
        return "2"
    elif x in "DEF":
        return "3"
    elif x in "GHI":
        return "4"
    elif x in "DEF":
        return "3"
    elif x in "GHI":
        return "4"
    elif x in "JKL":
        return "5"
    elif x in "MNO":
        return "6"
    elif x in "PQRS":
        return "7"
    elif x in "TUV":
        return "8"
    elif x in "WXYZ":
        return "9"
    return ""


def main():
    while True:
        try:
            telephone = input().upper()
        except EOFError:
            break

        print("".join(decode(x) for x in telephone))


if __name__ == "__main__":
    main()
