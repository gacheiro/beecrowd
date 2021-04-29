# 3093 - Truco da Galera 1.0
# https://www.urionlinejudge.com.br/judge/pt/problems/view/3093


def main():
    num_tests = int(input())
    
    for _ in range(num_tests):
        remaining_cards = set(input())

        if remaining_cards.issuperset({"Q", "J", "K", "A"}):
            print("Aaah muleke")
        else:
            print("Ooo raca viu")


if __name__ == "__main__":
    main()
