# 2591 - HameKameKa
# https://www.urionlinejudge.com.br/judge/pt/problems/view/2591


def main():
    c = int(input())
    
    for _ in range(c):
        fst, snd = [s.count('a') for s in input().split('k')]
        print('k{}'.format('a' * (fst * snd)))

        
if __name__ == '__main__':
    main()
