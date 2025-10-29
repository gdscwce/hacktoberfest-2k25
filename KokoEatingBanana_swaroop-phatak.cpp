#include <bits/stdc++.h>
using namespace std;

int CalHrs(vector<int> arr,int mid, int n){
    int HrsPile = 0;
    for(int i = 0 ;i<n;i++){
        HrsPile += (arr[i]+mid-1)/mid;
    }
    return HrsPile;
}

int kokoFuncn(vector<int> arr, int h){
    int low = 1;
    int high = *max_element(arr.begin(), arr.end());
    while(low<=high){
        int mid = (low+high)/2;
        int totalHrs = CalHrs(arr,mid, arr.size());
        if(totalHrs<=h){
            high = mid-1;
        }else{
            low = mid +1;
        }
    }
    return low;

}
int main() {
     vector<int> v = {7, 11, 6, 3};
     int h = 8;
    int ans = kokoFuncn(v, h);
    cout << "Koko should eat atleast " << ans << " bananas/hr.\n";
    return 0;

return 0;
}
