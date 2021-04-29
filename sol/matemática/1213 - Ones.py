# 1213 - Ones
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1213


def main():
    while True:
        try:
            n = int(input())
        except EOFError:
            break

        ones_number = 1
        digits_counter = 1

        while True:

            if ones_number % n == 0:
                print(digits_counter)
                break

            # Modular multiplication
            ones_number = (ones_number * 10 + 1) % n
            digits_counter += 1


if __name__ == "__main__":
    main()
