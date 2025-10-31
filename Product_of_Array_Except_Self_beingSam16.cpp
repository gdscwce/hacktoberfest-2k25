#include <bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin>>n;
    vector<int>a(n),ans(n,1);
    for(int i=0;i<n;i++) cin>>a[i];
    int left=1;
    for(int i=0;i<n;i++){
        ans[i]=left;
        left*=a[i];
    }
    int right=1;
    for(int i=n-1;i>=0;i--){
        ans[i]*=right;
        right*=a[i];
    }
    for(int x:ans) cout<<x<<" ";
}
