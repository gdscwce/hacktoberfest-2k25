#include <bits/stdc++.h>
using namespace std;

int minReorder(int n, vector<vector<int>>& con) {
    vector<vector<pair<int,int>>> g(n);
    for (auto& e : con) {
        g[e[0]].push_back({e[1],1});
        g[e[1]].push_back({e[0],0});
    }
    int ans = 0;
    vector<int> v(n,0);
    queue<int> q;
    q.push(0); v[0]=1;
    while(!q.empty()){
        int u=q.front();q.pop();
        for(auto [x,c]:g[u])
            if(!v[x]){ans+=c;v[x]=1;q.push(x);}
    }
    return ans;
}

int main(){
    int n,m;cin>>n>>m;
    vector<vector<int>> con(m,vector<int>(2));
    for(auto& e:con)cin>>e[0]>>e[1];
    cout<<minReorder(n,con)<<'\n';
}
