class Solution {
public:
    int rob(vector<int>& nums) {
        if(nums.size()==0)
            return -1;
        if(nums.size()==1)
            return nums[0];
        vector<int> dp(nums.size());
        dp[0]=nums[0];
        dp[1]=max(dp[0],nums[1]);
        for(int i=2;i<nums.size();i++){
            dp[i]=max(dp[i-1],nums[i]+dp[i-2]);
        }
        int maxi= dp[nums.size()-1];
        return maxi;
    }
};

//sample input and output
/*Input: nums = [1,2,3,1]
Output: 4

Input: nums = [2,7,9,3,1]
Output: 12*/