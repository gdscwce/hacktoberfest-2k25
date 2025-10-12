#include <bits/stdc++.h>
using namespace std;

string mergeAlternately(const string &word1, const string &word2) {
    int n1 = word1.size(), n2 = word2.size();
    string res;
    res.reserve(n1 + n2);             

    int i = 0, j = 0;
    while (i < n1 || j < n2) {
        if (i < n1) res.push_back(word1[i++]);
        if (j < n2) res.push_back(word2[j++]);
    }
    return res;
}

int main() {
    
    vector<pair<string,string>> tests = {
        {"abc", "pqr"},
        {"ab", "pqrs"},
        {"abcd", "pq"},
        {"", "hello"},
        {"one", ""}
    };

    for (auto &t : tests) {
        cout << "mergeAlternately(\"" << t.first << "\", \"" << t.second << "\") = "
             << mergeAlternately(t.first, t.second) << '\n';
    }
    return 0;
}
