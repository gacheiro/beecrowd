// 1764 - Itinerário do Papai Noel (Kruskal)
//https://www.urionlinejudge.com.br/judge/pt/problems/view/1764

#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>

#define MAXN 40010
using namespace std;

struct link {
    int x, y, z;
};

bool cmp(const struct link *A, const struct link *B) {
    // ordena de forma decrescente
    return A->z > B->z;
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
        rootu = root(parent, link->x);
        rootv = root(parent, link->y);
        if (rootu != rootv) {
            cost += link->z;
            parent[rootu] = rootv;
        }
        links.pop_back();
    }
    return cost;
}

int main() {
    int N, M;
    int x, y, z;
    vector<struct link*> links;
    struct link * link;

    while (1) {
        cin >> N >> M;
        if (N == 0 && M == 0) {
            break;
        }
        for (int i=0; i<M; i++) {
            link = new struct link;
            cin >> link->x >> link->y >> link->z;
            links.push_back(link);
        }
        cout << kruskal(links) << endl;
        links.clear();
    }
}
