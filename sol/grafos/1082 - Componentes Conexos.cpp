// 1082 - Componentes Conexos
// https://www.urionlinejudge.com.br/judge/pt/problems/view/1082

#include <iostream>
#include <list>

#define MAXN 30
#define WHITE 0
#define GREY 1
#define BLACK 2

using namespace std;

int connected_components(int adj[MAXN][MAXN], int n) {
    list<int> fifo;
    int components[MAXN]; // para imprimir os nós em ordem
    int colored[MAXN];
    int n_components = 0;

    for (int i=0; i<n; i++) {
        colored[i] = WHITE;
        components[i] = -1;
    }

    for (int k=0; k<n; k++) {
        if (colored[k] == WHITE) {
            fifo.push_back(k);
            colored[k] = GREY;
            n_components++;
            // bfs
            while(!fifo.empty()) {
                auto it = fifo.front();
                for (int i=0; i<n; i++) {
                    if (adj[it][i] == 1 && colored[i] == WHITE) {
                        // se eh adj e ainda não está na fila
                        fifo.push_back(i);
                        colored[i] = GREY;
                    }
                }
                colored[it] = BLACK;
                // este nó pertence ao componente da vez
                components[it] = n_components;
                fifo.pop_front();
            }
            // imprime o componente recém formado
            for (int i=0; i<n; i++) {
                if (components[i] == n_components) {
                    cout << (char) (i + 'a') << ",";
                }
            }
            cout << endl;
        }
    }
    return n_components;    
}

int main() {
    int N, V, E;
    int adj[MAXN][MAXN];
    char u, v;
    int test_case = 1;

    cin >> N;
    for (int i=0; i<N; i++) {
        cin >> V >> E;

        for (int i=0; i<V; i++) {
            for (int j=0; j<V; j++) {
                adj[i][j] = -1;
            }
        }

        for (int j=0; j<E; j++) {
            cin >> u >> v;
            adj[u-'a'][v-'a'] = 1;
            adj[v-'a'][u-'a'] = 1;
        }

        cout << "Case #" << test_case++ << ":" << endl;
        cout << connected_components(adj, V) << " connected components" << endl << endl;
    }
    return 0;
}
