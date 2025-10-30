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
