# 1550 - Inversão
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1550


def main():
    n = int(input())
    for _ in range(n):
        a, b = map(int, input().split())

        # busca em largura
        # gera a arvore sob demanda (cada no gera até 2 filhos)
        fifo = [a]
        press = {a: 0}
        while fifo:
            c = fifo.pop(0)
            if c == b:
                break
            elif c > 10_000:
                continue

            if c + 1 not in press:
                fifo.append(c + 1)
                press[c+1] = press[c] + 1
            
            rc = int(str(c)[::-1])
            if rc not in press:
                fifo.append(rc)
                press[rc] = press[c] + 1

        print(press[b])


if __name__ == "__main__":
    main()
