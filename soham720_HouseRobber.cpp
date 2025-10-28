#include <bits/stdc++.h>
using namespace std;

int rob(vector<int>& nums) {
    int n = nums.size();
    if (n == 1) return nums[0];
    int a = 0, b = nums[0];
    for (int i = 1; i < n; ++i) {
        int c = max(b, a + nums[i]);
        a = b; b = c;
    }
    return b;
}

int main() {
    int n; cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; ++i) cin >> nums[i];
    cout << rob(nums) << '\n';
}
