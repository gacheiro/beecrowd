# 1175 - Troca em Vetor I
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1175


def main():
    vec = []
    for _ in range(20):
        vec.append(input())

    for i, item in enumerate(reversed(vec)):
        print('N[{}] = {}'.format(i, item))
        

if __name__ == '__main__':
    main()
