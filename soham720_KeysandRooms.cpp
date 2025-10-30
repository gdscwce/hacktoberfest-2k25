#include <bits/stdc++.h>
using namespace std;

bool canVisitAllRooms(vector<vector<int>>& rooms) {
    int n = rooms.size();
    vector<bool> visited(n, false);
    stack<int> st;
    st.push(0);
    visited[0] = true;
    int count = 1;
    while (!st.empty()) {
        int room = st.top();
        st.pop();
        for (int key : rooms[room]) {
            if (!visited[key]) {
                visited[key] = true;
                st.push(key);
                count++;
            }
        }
    }
    return count == n;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<vector<int>> rooms(n);
    for (int i = 0; i < n; ++i) {
        int k;
        cin >> k;
        rooms[i].resize(k);
        for (int j = 0; j < k; ++j) cin >> rooms[i][j];
    }
    cout << (canVisitAllRooms(rooms) ? "true" : "false") << '\n';
}
