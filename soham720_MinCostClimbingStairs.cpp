#include <bits/stdc++.h>
using namespace std;

int minCostClimbingStairs(vector<int>& cost) {
    int n = cost.size();
    int a = 0, b = 0;
    for (int i = 2; i <= n; ++i) {
        int c = min(a + cost[i - 2], b + cost[i - 1]);
        a = b; b = c;
    }
    return b;
}

int main() {
    int n; cin >> n;
    vector<int> cost(n);
    for (int i = 0; i < n; ++i) cin >> cost[i];
    cout << minCostClimbingStairs(cost) << '\n';
}
