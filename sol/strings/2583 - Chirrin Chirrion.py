# 2583 - Chirrin Chirrion
# https://www.urionlinejudge.com.br/judge/pt/problems/view/2583


def main():
    c = int(input())
    
    for _ in range(c):
        chirrin, chirrion = set(), set()
        n = int(input())
        
        for __ in range(n):
            tausfo_casts = input()
            obj, magic_word = tausfo_casts.split()
            
            if magic_word.lower().endswith('chirrin'):
                chirrin.add(obj)
            elif magic_word.lower().endswith('chirrion'):
                chirrion.add(obj)
            
        print('TOTAL')
        print('\n'.join(obj for obj in sorted(chirrin - chirrion)))
        
    
if __name__ == '__main__':
    main()
