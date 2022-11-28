# 2587 - Jetiqui
# https://www.urionlinejudge.com.br/judge/pt/problems/view/2587


def main():
    n = int(input())

    for _ in range(n):
        w1 = input()
        w2 = input()
        w3 = input()
        
        first_ = w3.find("_")
        second_ = w3.rfind("_")

        if w1[first_] == w2[second_] or w2[first_] == w1[second_]:
            print("Y")
        else:
            print("N")


if __name__ == "__main__":
    main()
