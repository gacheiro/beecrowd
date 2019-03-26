# Contando Caracters
# https://www.urionlinejudge.com.br/judge/pt/problems/view/2108


def main():
    longest = ''
    
    while True:
        line = input()
        if line == '0':
            break
        
        words = line.split()        
        print('-'.join(str(len(w)) for w in words))
        
        # reversed to consider latest words first
        longest_in_line = max(reversed(words), key=len)
        if len(longest_in_line) >= len(longest):
            longest = longest_in_line
    
    print('\nThe biggest word: {}'.format(longest))
    

if __name__ == '__main__':
    main()
