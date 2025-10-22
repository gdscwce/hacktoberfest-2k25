// Move_Zeroes_RamyakJain.cpp
// Given an integer array nums, move all 0's to the end while maintaining the relative order of non-zero elements.
// Example: nums = [0,1,0,3,12] → output [1,3,12,0,0]
//
// Time Complexity: O(n)
// Space Complexity: O(1)

#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;  // Input size of array
    vector<int> nums(n);
    for (int i = 0; i < n; ++i) cin >> nums[i];

    int pos = 0;  // position to place non-zero
    for (int i = 0; i < n; ++i) {
        if (nums[i] != 0) swap(nums[i], nums[pos++]);
    }

    for (int i = 0; i < n; ++i) cout << nums[i] << " ";
    cout << '\n';
    return 0;
}
