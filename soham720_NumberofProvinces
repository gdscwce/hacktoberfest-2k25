#include <bits/stdc++.h>
using namespace std;

void dfs(int i, vector<vector<int>>& g, vector<int>& v) {
    v[i] = 1;
    for (int j = 0; j < g.size(); ++j)
        if (g[i][j] && !v[j]) dfs(j, g, v);
}

int findCircleNum(vector<vector<int>>& g) {
    int n = g.size(), c = 0;
    vector<int> v(n, 0);
    for (int i = 0; i < n; ++i)
        if (!v[i]) { dfs(i, g, v); c++; }
    return c;
}

int main() {
    int n; cin >> n;
    vector<vector<int>> g(n, vector<int>(n));
    for (auto& r : g) for (auto& x : r) cin >> x;
    cout << findCircleNum(g) << '\n';
}
