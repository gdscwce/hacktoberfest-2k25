
#include <bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin>>n;
    vector<int>h(n);
    for(int i=0;i<n;i++) cin>>h[i];
    int i=0,j=n-1;
    long long ans=0;
    while(i<j){
        ans=max(ans,(long long)min(h[i],h[j])*(j-i));
        if(h[i]<h[j]) i++;
        else j--;
    }
    cout<<ans;
}
