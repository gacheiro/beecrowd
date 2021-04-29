# 1667 - HTML
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1667

import sys


def parse_html(html):
    line_length = 0
    for token in html.split():

        if token == "<br>":
            yield "\n"
            line_length = 0

        elif token == "<hr>" and line_length == 0:
            yield "-" * 80 + "\n"

        elif token == "<hr>":
            yield "\n" + "-" * 80
            line_length = 80

        # First word of the line
        elif len(token) and line_length == 0:
            yield token
            line_length += len(token)

        elif len(token) + line_length + 1 <= 80:
            yield " " + token
            line_length += len(token) + 1

        # Line too long, add a break
        else:
            yield "\n" + token
            line_length = len(token)


def main():
    html = "".join(sys.stdin.readlines())
    print("".join(parse_html(html)))


if __name__ == "__main__":
    main()
