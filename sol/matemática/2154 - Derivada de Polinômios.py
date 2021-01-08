# 2154 - Derivada de Polinômios
# https://www.urionlinejudge.com.br/judge/pt/problems/view/2154


def deriv(p):
    """Calcula a derivada do polinomio CxE."""
    coef, exp = (int(i) for i in p.split("x"))
    coef, exp = coef*exp, exp-1
    if exp > 1:
        return f"{coef}x{exp}"
    return f"{coef}x"
    

def main():
    while True:
        try:
            _ = int(input())
        except EOFError:
            break
        
        pol = input().split(" + ")
        print(" + ".join(map(deriv, pol)))


if __name__ == "__main__":
    main()
