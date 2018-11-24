# 2694 - Problema com a Calculadora
# https://www.urionlinejudge.com.br/judge/pt/problems/view/2694


# def digits(c: str) -> str
def digits(c):
    return c if c.isdigit() else ' '


# def parse_values(s: str) -> Iterable[int]
def parse_values(s):
    ds = ''.join(digits(c) for c in s)
    return map(int, ds.split())
    

def main():
    n = int(input())
    for _ in range(n):
        values = parse_values(input())
        print(sum(values))


if __name__ == "__main__":
    main()
