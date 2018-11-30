# 2872 - Protocolo TCP/IP
# https://www.urionlinejudge.com.br/judge/pt/problems/view/2872


def receive_pkgs():
    pkgs = []

    while True:
        pkg = input()

        try:        
            _, pkgid = pkg.split()
        except ValueError: # got a '0', cannot unpack
            break
            
        pkgs.append(pkgid)

    return pkgs


def main():
    while True:
        try:
            input()
            pkgs = receive_pkgs()
            for pkg in sorted(pkgs, key=int):
                print('Package {}'.format(pkg))
            print('')

        except EOFError:
            return


if __name__ == '__main__':
    main()
