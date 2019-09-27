// 2959 - Credo com ParaTudo!
// https://www.urionlinejudge.com.br/judge/pt/problems/view/2959

#include<iostream>

#define MAXN 405
#define INF 999999

using namespace std;

void floyd_warshall(int n, int d[MAXN][MAXN]) {
    for(int k=0; k<=n; k++) {
        for(int i=0; i<=n; i++) {
            for(int j=0; j<=n; j++) {
                if (d[i][k] + d[k][j] < d[i][j]) {
                    d[i][j] = d[i][k] + d[k][j];
                }
            }
        }
    }
}

int main() {
    int N, M, P;
    int d[MAXN][MAXN];
    int i, j;

    cin >> N >> M >> P;

    for(i=0; i<=N; i++) {
        for(j=0; j<=N; j++) {
            d[i][j] = INF;
        }
    }

    for(int m=0; m<M; m++) {
        cin >> i >> j;
        d[i][j] = 1;
        d[j][i] = 1;
    }

    floyd_warshall(N, d);

    for(int p=0; p<P; p++) {
        cin >> i >> j;
        if (d[i][j] < INF)
            cout << "Lets que lets" << endl;
        else
            cout << "Deu ruim" << endl;
    }
    return 0;
}
