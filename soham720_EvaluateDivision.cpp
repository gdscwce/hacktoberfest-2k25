#include <bits/stdc++.h>
using namespace std;

vector<double> calcEquation(vector<vector<string>>& eq, vector<double>& val, vector<vector<string>>& q) {
    unordered_map<string, vector<pair<string,double>>> g;
    for (int i=0;i<eq.size();++i){
        g[eq[i][0]].push_back({eq[i][1],val[i]});
        g[eq[i][1]].push_back({eq[i][0],1.0/val[i]});
    }
    vector<double> ans;
    for (auto& x:q){
        string a=x[0],b=x[1];
        if(!g.count(a)||!g.count(b)){ans.push_back(-1.0);continue;}
        queue<pair<string,double>> que;
        unordered_set<string> vis;
        que.push({a,1.0});
        double res=-1.0;
        while(!que.empty()){
            auto [cur,prod]=que.front();que.pop();
            if(cur==b){res=prod;break;}
            vis.insert(cur);
            for(auto& [nei,w]:g[cur])
                if(!vis.count(nei))que.push({nei,prod*w});
        }
        ans.push_back(res);
    }
    return ans;
}

int main(){
    int n;cin>>n;
    vector<vector<string>> eq(n,vector<string>(2));
    vector<double> val(n);
    for(int i=0;i<n;++i)cin>>eq[i][0]>>eq[i][1]>>val[i];
    int qn;cin>>qn;
    vector<vector<string>> q(qn,vector<string>(2));
    for(int i=0;i<qn;++i)cin>>q[i][0]>>q[i][1];
    auto res=calcEquation(eq,val,q);
    for(double x:res) cout<<fixed<<setprecision(5)<<x<<' ';
}
