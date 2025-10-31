#include <bits/stdc++.h>
using namespace std;
int main(){
    int n,m;
    cin>>n>>m;
    vector<int>a(n);
    for(int i=0;i<n;i++) cin>>a[i];
    int c=0;
    for(int i=0;i<n;i++){
        if(a[i]==0){
            int left=(i==0)?0:a[i-1];
            int right=(i==n-1)?0:a[i+1];
            if(left==0 && right==0){
                a[i]=1;
                c++;
            }
        }
    }
    if(c>=m) cout<<"true";
    else cout<<"false";
}
