class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> res(n, 1);
        int left = 1, right = 1;
        for (int i = 0; i < n; i++) {
            res[i] *= left;
            left *= nums[i];
            res[n - i - 1] *= right;
            right *= nums[n - i - 1];
        }
        return res;
    }
};
