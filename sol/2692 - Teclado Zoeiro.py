# 2651 - Teclado Zoeiro
# https://www.urionlinejudge.com.br/judge/pt/problems/view/2692


# kb_map(keys_map: Dict[str, str]) -> Callable[[str], str]
def kb_map(keys_map):

    kb_dict = dict(keys_map)

    # str -> str
    def kb_key(k):
        return kb_dict.get(k, k)

    return kb_key
        

def main():
    n, m = map(int, input().split())
    kvs = []

    for _ in range(n):
        kv = input().split()
        kvs.append(kv)
        kvs.append(list(reversed(kv)))

    kmap = kb_map(kvs)

    for _ in range(m):
        line = input()
        print( "".join(map(kmap, line)) )


if __name__ == "__main__":
    main()
