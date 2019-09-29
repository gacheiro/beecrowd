// 1855 - Mapa do Meistre
// https://www.urionlinejudge.com.br/judge/pt/problems/view/1855

#include <iostream>
#include <utility>

#define MAXN 105
#define OUT_OF_BOUNDS -1
#define WHITE 0

using namespace std;

int map[MAXN][MAXN];
int colored[MAXN][MAXN];
int X, Y;

pair<int, int> move(pair<int, int> pos, char dir) {
    int i = pos.first;
    int j = pos.second;
    switch (dir)
    {
    case '>':
        j++;
        break;
    case '<':
        j--;
        break;
    case '^':
        i--;
        break;
    case 'v':
        i++;
        break;
    }
    if (j < 0 || j >= X) {
        j = OUT_OF_BOUNDS;
    }
    if (i < 0 || i >= Y) {
        i = OUT_OF_BOUNDS;
    }
    return make_pair(i, j);
}

char explore_map() {
    char dir = map[0][0];
    auto pos = make_pair(0, 0);

    while (1) {
        pos = move(pos, dir);
        if (pos.first == OUT_OF_BOUNDS || pos.second == OUT_OF_BOUNDS) {
            return '!';
        }
        else if (map[pos.first][pos.second] == '*') {
            return '*';
        }
        else if (colored[pos.first][pos.second] != WHITE) {
            // andando em círculos
            return '!';
        }
        else if (map[pos.first][pos.second] != '.') {
            // só pinta os caracteres '>', '<', '^', 'v'
            dir = map[pos.first][pos.second];
            colored[pos.first][pos.second]++;
        }
    }
}

int main() {
    char row[MAXN];
    
    cin >> X >> Y;
    for (int i=0; i<Y; i++) {
        cin >> row;
        for (int j=0; j<X; j++) {
            map[i][j] = row[j];
            colored[i][j] = WHITE;
        }
    }
    cout << explore_map() << endl;
    return 0;
}
