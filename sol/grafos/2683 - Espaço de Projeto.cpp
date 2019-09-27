// 2683 - Espaço de Projeto (Kruskal)
// https://www.urionlinejudge.com.br/judge/pt/problems/view/2683

#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cstring>

#define MAXN 1100
using namespace std;

struct link {
    int u, v, w;
};

bool cmp(const struct link *A, const struct link *B) {
    // ordena de forma decrescente
    return A->w > B->w;
}

int root(int parent[MAXN], int i) {
    while(parent[i] != -1) {
        i = parent[i];
    }
    return i;
}

void kruskal_min_max(vector<struct link*> links) {
    int parent[MAXN];
    int max_cost = 0, min_cost = 0;
    vector<struct link*>::iterator it;
    vector<struct link*>::reverse_iterator rit;
    int rootu, rootv;
    struct link * link;

    // nenhum nó possui pai inicialmente
    memset(parent, -1, sizeof(int) * MAXN);
    for (it=links.begin(); it!=links.end(); ++it) {
        link = *it;
        rootu = root(parent, link->u);
        rootv = root(parent, link->v);
        if (rootu != rootv) {
            max_cost += link->w;
            parent[rootu] = rootv;
        }
    }

    memset(parent, -1, sizeof(int) * MAXN);
    for (rit=links.rbegin(); rit!=links.rend(); ++rit) {
        link = *rit;
        rootu = root(parent, link->u);
        rootv = root(parent, link->v);
        if (rootu != rootv) {
            min_cost += link->w;
            parent[rootu] = rootv;
        }
    }
    cout << max_cost << endl << min_cost << endl;
}

int main() {
    int N;
    int u, v, w;
    vector<struct link*> links;
    struct link * link;

    cin >> N;
    for (int i=0; i<N; i++) {
        link = new struct link;
        cin >> link->u >> link->v >> link->w;
        links.push_back(link);
    }
    sort(links.begin(), links.end(), cmp);
    kruskal_min_max(links);
    return 0;
}
