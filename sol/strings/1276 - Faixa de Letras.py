# 1276 - Faixa de Letras
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1276


def main():
    while True:
        try:
            string = input()
        except EOFError:
            break
        
        ranges = {}
        letter_range = {}

        chars = list(sorted(string))

        for c in chars:
            if c == " ":
                continue

            prev_alp_letter = chr(ord(c) - 1)
            if prev_alp_letter in letter_range:
                start, end = letter_range[prev_alp_letter], c
                letter_range[c] = start
                ranges[start] = end

            else:
                letter_range[c] = c
                ranges[c] = c

        print(", ".join(f"{start}:{end}" for start, end in ranges.items()))


if __name__ == "__main__":
    main()
