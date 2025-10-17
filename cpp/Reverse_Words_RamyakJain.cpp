// Reverse_Words_RamyakJain.cpp
// Time Complexity: O(n)  where n = s.length()
// Space Complexity: O(n)  for storing words



#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    getline(cin, s);

    vector<string> v;
    int n = s.size();
    for (int i = 0; i < n; ++i) {
        if (s[i] == ' ') continue;
        int j = i;
        while (j < n && s[j] != ' ') ++j;
        v.push_back(s.substr(i, j - i));
        i = j - 1;
    }

    string out;
    for (int k = (int)v.size() - 1; k >= 0; --k) {
        out += v[k];
        if (k > 0) out += ' ';
    }

    cout << out << '\n';
    return 0;
}