
#include <bits/stdc++.h>
using namespace std;
int main() {
    int n; cin >> n;
    vector<int> deck(n);
    for (int i = 0; i < n; i++) cin >> deck[i];
    sort(deck.begin(), deck.end());
    queue<int> q;
    for (int i = 0; i < n; i++) q.push(i);
    vector<int> ans(n);
    for (int i = 0; i < n; i++) {
        ans[q.front()] = deck[i];
        q.pop();
        if (!q.empty()) {
            q.push(q.front());
            q.pop();
        }
    }
    for (int x : ans) cout << x << " ";
}
