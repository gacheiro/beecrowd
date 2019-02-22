# 2930 - TCC da Depressão Natalino
# https://www.urionlinejudge.com.br/judge/pt/problems/view/2930

def main():
    e, d = map(int, input().split())

    if e > d:
        print('Eu odeio a professora!')

    elif e + 3 <= d:
        print('Muito bem! Apresenta antes do Natal!')
    
    else:
        print("Parece o trabalho do meu filho!")

        if e + 2 < 24:
            print('TCC Apresentado!')
        else:
            print('Fail! Entao eh nataaaaal!')


if __name__ == '__main__':
    main()
