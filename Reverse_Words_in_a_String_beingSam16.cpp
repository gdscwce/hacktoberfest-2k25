#include <bits/stdc++.h>
using namespace std;
int main(){
    string s;
    getline(cin,s);
    stringstream ss(s);
    vector<string>w;
    string word;
    while(ss>>word) w.push_back(word);
    reverse(w.begin(),w.end());
    for(int i=0;i<w.size();i++){
        cout<<w[i];
        if(i<w.size()-1) cout<<" ";
    }
}
