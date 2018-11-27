# 2815 - Digitador Gago
# https://www.urionlinejudge.com.br/judge/pt/problems/view/2815


# def translate(w: str) -> str
def translate(w):
    if w[:2] == w[2:4]:
        return w[2:]
    return w


def main():
    msg = input()
    print(' '.join(map(translate, msg.split())))


if __name__ == '__main__':
    main()
