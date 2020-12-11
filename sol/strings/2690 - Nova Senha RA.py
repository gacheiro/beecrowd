# 2690 - Nova Senha RA
# https://www.urionlinejudge.com.br/judge/pt/problems/view/2690


def decode(letter):
    if letter in "GQaku":
        return "0"
    elif letter in "ISblv":
        return "1"
    elif letter in "EOYcmw":
        return "2"
    elif letter in "FPZdnx":
        return "3"
    elif letter in "JTeoy":
        return "4"
    elif letter in "DNXfpz":
        return "5"
    elif letter in "AKUgq":
        return "6"
    elif letter in "CMWhr":
        return "7"
    elif letter in "BLVis":
        return "8"
    elif letter in "HRjt":
        return "9"
    return ""


def main():
    n = int(input())
    for _ in range(n):
        password = input()
        decoded_password = "".join(decode(x) for x in password)
        print(decoded_password[:12])


if __name__ == "__main__":
    main()
