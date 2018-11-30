# 1610 - Dudu Faz Serviço (BFS)
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1610

from collections import defaultdict


NEW = 0
PENDING = 1
NOLOOP = 2


def hasloop(dependencies):
    status = defaultdict(lambda: NEW)

    def checkloop(doc):

        lifo = [doc]
        while lifo:

            doc = lifo[-1]
            status[doc] = PENDING
            
            for d in dependencies[doc]:
                if status[d] == NEW:
                    lifo.append(d)
                    break
                elif status[d] == PENDING:
                    # found another pending file. It is a loop.
                    return True
            else:
                # nothing was added to the lifo, pop the doc
                lifo.pop()
                status[doc] = NOLOOP
            
        return False

    docs = list(dependencies.keys())
    for doc in docs:
        if status[doc] == NEW:
            if checkloop(doc):
                return True
    return False


def main():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        dependencies = defaultdict(set)

        for _ in range(b):
            doc1, doc2 = map(int, input().split())
            dependencies[doc1].add(doc2)
        
        print('SIM' if hasloop(dependencies) else 'NAO')


if __name__ == '__main__':
    main()
