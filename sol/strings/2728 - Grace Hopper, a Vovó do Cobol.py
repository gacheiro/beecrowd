# 2728 - Grace Hopper, a Vovó do Cobol
# https://www.urionlinejudge.com.br/judge/pt/problems/view/2728
    

def has_COBOL(words):
    it = iter(words)    
    for letter in 'COBOL':
        try:
            w = next(it)
            while w[0] != letter and w[-1] != letter:
                w = next(it)
                
        except StopIteration:
            return False            
    return True

    
def main():
    while True:
        try:
            words = map(str.upper, input().split('-'))
        except EOFError:
            break
            
        print('GRACE HOPPER' if has_COBOL(words) else 'BUG')
        
            
if __name__ == '__main__':
    main()
