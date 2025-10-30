#include <bits/stdc++.h>
using namespace std;

double findMaxAverage(const vector<int>& nums, int k) {
    long long sum = 0, maxSum = 0;
    for (int i = 0; i < k; ++i) sum += nums[i];
    maxSum = sum;
    for (int i = k; i < nums.size(); ++i) {
        sum += nums[i] - nums[i - k];
        maxSum = max(maxSum, sum);
    }
    return (double)maxSum / k;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, k;
    cin >> n >> k;
    vector<int> nums(n);
    for (int i = 0; i < n; ++i) cin >> nums[i];
    cout.setf(ios::fixed);
    cout << setprecision(6) << findMaxAverage(nums, k) << '\n';
}
