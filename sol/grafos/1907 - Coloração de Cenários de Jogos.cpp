// 1907 - Coloração de Cenários de Jogos
// https://www.urionlinejudge.com.br/judge/pt/problems/view/1907

#include <iostream>
#include <vector>
#include <utility>

#define MAXN 1050
#define WHITE 0
#define BLACK 1

int img[MAXN][MAXN];

using namespace std;

void dfs(int n, int m, pair<int, int> pos, int color) {
    vector<pair<int,int>> lifo;
    lifo.push_back(pos);
    while(!lifo.empty()) {
        auto p = lifo.back();
        auto i = p.first;
        auto j = p.second;
        if (i-1 >= 0 && img[i-1][j] == WHITE)  {
            lifo.push_back(make_pair(i-1, j));
        }
        else if (i+1 < n && img[i+1][j] == WHITE)  {
            lifo.push_back(make_pair(i+1, j));
        }
        else if (j-1 >= 0 && img[i][j-1] == WHITE)  {
            lifo.push_back(make_pair(i, j-1));
        }
        else if (j+1 < m && img[i][j+1] == WHITE)  {
            lifo.push_back(make_pair(i, j+1));
        }
        else {
            lifo.pop_back();
        }
        img[i][j] = color;
    }
}

int coloring(int n, int m) {
    vector<pair<int, int>> lifo;
    int color = BLACK;
    for (int i=0; i<n; i++) {
        for (int j=0; j<m; j++) {
            if (img[i][j] == WHITE) {
                auto pos = make_pair(i, j);
                dfs(n, m, pos, ++color);
            }
        }
    }
    return color - BLACK;
}

int main() {
    int M, N;
    char linha[MAXN];

    cin >> N >> M;
    for (int i=0; i<N; i++) {
        cin >> linha;
        for (int j=0; j<M; j++) {
            img[i][j] = linha[j] == '.' ? WHITE : BLACK;
        }
    }
    cout << coloring(N, M) << endl;
    return 0;
}
