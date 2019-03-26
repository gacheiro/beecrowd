# 1260 - Espécies de Madeira
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1260

from collections import Counter


def main():
    n = int(input())
    input() #empty line
    
    for i in range(n):
        counter = Counter()
        
        while True:
            try:
                species = input()
                if species == '':
                    break
            except EOFError:
                break
                
            counter[species] += 1
            
        # calcs the total of trees
        total = sum(counter.values())
        # prints the ocurrency of each species div by the total of trees
        for species in sorted(counter.keys()):
            print('{} {:.4f}'.format(species, 100 * counter[species]/total))
            
        if i + 1 < n:
            print()
        

if __name__ == '__main__':
    main()
