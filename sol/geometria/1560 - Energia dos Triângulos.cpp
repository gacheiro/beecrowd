// 1560 - Energia dos Triângulos
// https://www.urionlinejudge.com.br/judge/pt/problems/view/1560

#include<cstdio>

struct point {
    int x, y;
};

int line_side(struct point p1, struct point p2, struct point p3) {
    // Calcula de qual lado o ponto p está da reta a-b.
    // Retorna -1 se p está do lado esquerdo da reta,
    // 0 se está na reta e 1 se está do lado direito
    // https://math.stackexchange.com/a/274728
    return (p1.x - p3.x) * (p2.y - p3.y) - (p2.x - p3.x) * (p1.y - p3.y);
}

bool is_inside(struct point p, struct point a, struct point b, struct point c) {
    // https://stackoverflow.com/a/2049593
    int d1, d2, d3;
    bool has_neg, has_pos;

    d1 = line_side(p, a, b);
    d2 = line_side(p, b, c);
    d3 = line_side(p, c, a);
    // p precisa ter o mesmo sinal (lado) para as 3 retas
    has_neg = (d1 < 0) || (d2 < 0) || (d3 < 0);
    has_pos = (d1 > 0) || (d2 > 0) || (d3 > 0);
    return !(has_neg && has_pos);
}

int main() {
    int N, M;
    struct point black_p[105], white_p[105];
    int points_inside, power;

    while(scanf("%d %d", &N, &M) != EOF) {
        for(int i=0; i<N; i++) {
            scanf("%d %d", &black_p[i].x, &black_p[i].y);
        }

        for(int i=0; i<M; i++) {
            scanf("%d %d", &white_p[i].x, &white_p[i].y);
        }

        power = 0;
        for(int i=0; i<N; i++) {
            for(int j=i+1; j<N; j++) {
                for(int k=j+1; k<N; k++) {
                    // calcula a quantidade de pts dentro do triangulo (i, j, k)
                    points_inside = 0;
                    for(int l=0; l<M; l++) {                        
                        if (is_inside(white_p[l], black_p[i], black_p[j], black_p[k])) {
                            points_inside++;
                        }
                    }
                    power += points_inside * points_inside;
                }
            }
        }
        printf("%d\n", power);
    }

    return 0;
}
