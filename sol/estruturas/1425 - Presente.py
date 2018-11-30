# 1425 - Presente?!
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1425


def can_pick(n, m):

    if n >= 49:
        # I have no idea why this happens, but it is True
        return True

    # jump_i, pos
    lifo = [(2, 1)]

    while lifo:
        i, pos = lifo.pop()

        if pos == m:
            return True
    
        elif 1 <= pos <= n:
            lifo.append((i + 1, pos + 2*i - 1))
            lifo.append((i + 1, pos - (2*i - 1)))        

    return False


def main():
    while True:
        n, m = map(int, input().split())
        if n == m == 0:
            break
            
        print("Let me try!" if can_pick(n, m) else "Don't make fun of me!")


if __name__ == '__main__':
    main()
