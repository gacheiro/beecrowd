// 2854 - Árvore Genealógica
// https://www.urionlinejudge.com.br/judge/pt/problems/view/2854

#include <iostream>
#include <map>
#include <set>

#define MAXN 500

using namespace std;

int root(int family[MAXN], int p) {
    while (family[p] != -1) {
        p = family[p];
    }
    return p;
}

int main() {
    int M, N, k = 1;
    string p1, p2, r;
    map<string,int> people;
    int family[MAXN];
    set<int> unique_families;

    cin >> M >> N;
    for (int i=0; i<=M; i++)
        family[i] = -1;

    for (int i=0; i<N; i++) {
        cin >> p1 >> r >> p2;

        if (!people[p1]) {
            people[p1] = k++;
        }
        if (!people[p2]) {
            people[p2] = k++;
        }

        // verifica o ancestral mais antigo de cada pessoa
        auto f1 = root(family, people[p1]);
        auto f2 = root(family, people[p2]);
        if (f1 != f2) {
            // une as duas familias
            family[f2] = f1;
        }
    }

    // calcula o numero de familias
    for (auto &x: people)
        unique_families.insert(root(family, x.second));    
    cout << unique_families.size() << endl;

    return 0;
}
