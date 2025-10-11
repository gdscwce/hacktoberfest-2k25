#include <bits/stdc++.h>
using namespace std;

string removeStars(const string& s){
    string res;
    res.reserve(s.size());
    for(char c:s){
        if(c=='*'){
            if (!res.empty())res.pop_back();
        } else{
            res.push_back(c);
        }
    }
    return res;
}

int main() {
    cin.tie(nullptr);
    string s;
    if(!(cin>>s)) return 0;
    cout<<removeStars(s)<<endl;
    return 0;
}
