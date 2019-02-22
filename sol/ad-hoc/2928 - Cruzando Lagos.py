# 2928 - Cruzando Lagos
# https://www.urionlinejudge.com.br/judge/pt/problems/view/2928


def thin_ice(ice):
    length = 0
    for i in ice:
        if i.startswith('.'):
            length += 1
        elif length:
            yield length
            length = 0
    if length:
        yield length


def main():
    n = int(input())

    ice = []
    for _ in range(n):
        ice.append(input()[0])
    
    jumps = list(thin_ice(ice))
    if all(j <= 2 for j in jumps):
        print(len(jumps))
    else:
        print('N')
        

if __name__ == '__main__':
    main()
