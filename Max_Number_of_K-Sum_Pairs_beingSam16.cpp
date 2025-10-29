#include <bits/stdc++.h>
using namespace std;
int main(){
    int n,k;
    cin>>n>>k;
    vector<int>a(n);
    for(int i=0;i<n;i++) cin>>a[i];
    unordered_map<int,int>mp;
    int c=0;
    for(int x:a){
        int y=k-x;
        if(mp[y]>0){
            c++;
            mp[y]--;
        }else mp[x]++;
    }
    cout<<c;
}
