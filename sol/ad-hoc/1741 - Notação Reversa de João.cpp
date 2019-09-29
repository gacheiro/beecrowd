// 1741 - Notação Reversa de João
// https://www.urionlinejudge.com.br/judge/pt/problems/view/1741

#include <iostream>
#include <vector>

// global flags
bool DIV_BY_ZERO = false;
bool INVALID_EXPR = false;

using namespace std;

inline bool is_op(char op) {
    return (op == '+' || op == '-' || op == '*' || op == '/');
}

int result(char op, int a, int b) {
    if (op == '+')
        return b + a;
    else if (op == '-')
        return b - a;
    else if (op == '*')
        return b * a;
    else {
        if (a == 0) {
            DIV_BY_ZERO = true;
            return 0;
        }
        return b / a;
    }
}

int main() {
    string expr;
    vector<int> lifo;
    int a, b;

    while (getline(cin, expr)) {
        INVALID_EXPR = false;
        DIV_BY_ZERO = false;
        lifo.clear();
        for(auto it=expr.rbegin(); it!=expr.rend(); it++) {
            if (*it >= '0' && *it <= '9') {
                lifo.push_back(*it - '0');
            }
            else if (is_op(*it)) {
                if (lifo.size() >= 2) {
                    a = lifo.back(); lifo.pop_back();
                    b = lifo.back(); lifo.pop_back();
                    lifo.push_back(result(*it, a, b));
                }
                else {
                    INVALID_EXPR = true;
                    break;
                }
            }
        }

        if (INVALID_EXPR || lifo.size() != 1) {
            cout << "Invalid expression." << endl;
        }
        else if (DIV_BY_ZERO) {
            cout << "Division by zero." << endl;
        }
        else {
            cout << "The answer is " << lifo.back() << "." << endl;
        }
    }
    return 0;
}
