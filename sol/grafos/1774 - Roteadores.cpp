// 1774 - Roteadores (Kruskal)
// https://www.urionlinejudge.com.br/judge/pt/problems/view/1774

#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>

#define MAXN 65
using namespace std;

struct link {
    int u, v, p;
};

bool cmp(const struct link *A, const struct link *B) {
    // ordena de forma decrescente
    return A->p > B->p;
}

int root(int parent[MAXN], int i) {
    if(parent[i] == -1)
        return i;
    return root(parent, parent[i]);
}

int kruskal(vector<struct link*> links) {
    int parent[MAXN];
    int cost = 0;
    int rootu, rootv;
    struct link * link;

    sort(links.begin(), links.end(), cmp);
    // nenhum nó possui pai inicialmente
    memset(parent, -1, sizeof(int) * MAXN);

    while (!links.empty()) {
        link = links.back();
        rootu = root(parent, link->u);
        rootv = root(parent, link->v);
        if (rootu != rootv) {
            cost += link->p;
            parent[rootu] = rootv;
        }
        links.pop_back();
    }
    return cost;
}

int main() {
    int R, C;
    int u, v, p;
    vector<struct link*> links;
    struct link * link;

    cin >> R >> C;
    for (int i=0; i<C; i++) {
        link = new struct link;
        cin >> link->u >> link->v >> link->p;
        links.push_back(link);
    }
    cout << kruskal(links) << endl;
}
