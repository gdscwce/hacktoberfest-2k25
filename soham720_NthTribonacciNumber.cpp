#include <bits/stdc++.h>
using namespace std;

int tribonacci(int n) {
    if (n < 3) return n == 0 ? 0 : 1;
    int a = 0, b = 1, c = 1, d;
    for (int i = 3; i <= n; ++i) {
        d = a + b + c;
        a = b; b = c; c = d;
    }
    return c;
}

int main() {
    int n; cin >> n;
    cout << tribonacci(n) << '\n';
}
