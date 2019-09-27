// 2404 - Reduzindo Detalhes em um Mapa
// https://www.urionlinejudge.com.br/judge/pt/problems/view/2404

#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>

#define MAXN 505
using namespace std;

struct link {
    int u, v, w;
};

bool cmp(const struct link A, const struct link B) {
    // ordena de forma crescente
    return A.w < B.w;
}

int root(int parent[MAXN], int i) {
    while(parent[i] != -1) {
        i = parent[i];
    }
    return i;
}


int kruskal(vector<struct link> links) {
    int parent[MAXN];
    int cost;
    vector<struct link>::iterator it;
    int rootu, rootv;
    // nenhum nó possui pai inicialmente
    memset(parent, -1, sizeof(int) * MAXN);
    for (it=links.begin(); it!=links.end(); ++it) {
        rootu = root(parent, (*it).u);
        rootv = root(parent, (*it).v);
        if (rootu != rootv) {
            cost += (*it).w;
            parent[rootu] = rootv;
        }
    }
    return cost;
}


int main() {
    int N, M;
    int u, v, w;
    vector<struct link> links;
    struct link link;

    cin >> N >> M;
    for (int i=0; i<M; i++) {
        cin >> link.u >> link.v >> link.w;
        links.push_back(link);
    }
    sort(links.begin(), links.end(), cmp);
    cout << kruskal(links) << endl;
    return 0;
}
