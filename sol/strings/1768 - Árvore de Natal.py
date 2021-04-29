# 1768 - Árvore de Natal
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1768


def tree(base_length):
    for i in range(1, base_length + 1, 2):
        yield ("*" * i).center(base_length).rstrip()
    yield "*".center(base_length).rstrip()
    yield "***".center(base_length).rstrip()


def main():
    while True:
        try:
            base_length = int(input())
        except EOFError:
            break
        
        print("\n".join(tree(base_length)))
        print()


if __name__ == "__main__":
    main()
