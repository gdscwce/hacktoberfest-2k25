**1. Number of Provinces (LeetCode 547)**

```cpp
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
```

---

**2. Reorder Routes to Make All Paths Lead to the City Zero (LeetCode 1466)**

```cpp
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
```

---

**3. Evaluate Division (LeetCode 399)**

```cpp
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
```

---

**4. Nearest Exit from Entrance in Maze (LeetCode 1926)**

```cpp
#include <bits/stdc++.h>
using namespace std;

int nearestExit(vector<vector<char>>& maze, vector<int>& e) {
    int m=maze.size(),n=maze[0].size();
    queue<pair<int,int>> q;
    q.push({e[0],e[1]});
    vector<vector<int>> d(m,vector<int>(n,-1));
    d[e[0]][e[1]]=0;
    int dirs[4][2]={{1,0},{-1,0},{0,1},{0,-1}};
    while(!q.empty()){
        auto [x,y]=q.front();q.pop();
        for(auto& dir:dirs){
            int nx=x+dir[0],ny=y+dir[1];
            if(nx<0||ny<0||nx>=m||ny>=n||maze[nx][ny]=='+')continue;
            if(d[nx][ny]==-1){
                d[nx][ny]=d[x][y]+1;
                if(nx==0||ny==0||nx==m-1||ny==n-1) return d[nx][ny];
                q.push({nx,ny});
            }
        }
    }
    return -1;
}

int main(){
    int m,n;cin>>m>>n;
    vector<vector<char>> maze(m,vector<char>(n));
    for(int i=0;i<m;++i)for(int j=0;j<n;++j)cin>>maze[i][j];
    vector<int> e(2);cin>>e[0]>>e[1];
    cout<<nearestExit(maze,e)<<'\n';
}
```
