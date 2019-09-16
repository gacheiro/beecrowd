# 2017 - Seis Strings
# https://www.urionlinejudge.com.br/judge/pt/problems/view/2017


def hamming_distance(str1, str2):
    return sum(1 for a, b in zip(str1, str2) if a != b)
    

def main():
    x = input()
    k = int(input())
    dists = {}
    for i in range(1, 6):
        y = input()
        dists[i] = hamming_distance(x, y)

    i, dist = min(dists.items(), key=lambda item: item[1])
    if dist > k:
        print(-1)
    else:
        print('{}\n{}'.format(i, dist))


if __name__ == '__main__':
    main()
