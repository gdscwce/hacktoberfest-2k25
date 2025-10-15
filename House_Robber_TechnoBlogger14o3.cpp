/**
 * LeetCode 75: House Robber
 * 
 * Problem Statement:
 * You are a professional robber planning to rob houses along a street.
 * Each house has a certain amount of money stashed, the only constraint stopping you
 * from robbing each of them is that adjacent houses have security systems connected
 * and it will automatically contact the police if two adjacent houses were broken into
 * on the same night.
 * 
 * Given an integer array nums representing the amount of money of each house,
 * return the maximum amount of money you can rob tonight without alerting the police.
 * 
 * Example:
 * Input: nums = [1,2,3,1]
 * Output: 4
 * Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
 * Total amount you can rob = 1 + 3 = 4.
 * 
 * Time Complexity: O(n)
 * Space Complexity: O(1) - optimized space
 * 
 * Approach:
 * 1. Use dynamic programming with space optimization
 * 2. At each house, choose maximum between robbing current house + max from 2 houses back
 *    or not robbing current house (max from 1 house back)
 * 3. Keep track of only previous two values
 * 
 * @author TechnoBlogger14o3
 * @date 2025
 */

class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        
        // Base cases
        if (n == 0) return 0;
        if (n == 1) return nums[0];
        if (n == 2) return max(nums[0], nums[1]);
        
        // Space-optimized DP approach
        int prev2 = nums[0];  // max money robbed up to house 0
        int prev1 = max(nums[0], nums[1]);  // max money robbed up to house 1
        
        for (int i = 2; i < n; i++) {
            // Current max = max(rob current house + prev2, don't rob current house)
            int current = max(nums[i] + prev2, prev1);
            prev2 = prev1;
            prev1 = current;
        }
        
        return prev1;
    }
};

/*
Alternative approaches:

1. Recursive with Memoization:
   - rob(i) = max(nums[i] + rob(i-2), rob(i-1))
   - Time: O(n), Space: O(n)

2. Bottom-up DP Array:
   - dp[i] = max(nums[i] + dp[i-2], dp[i-1])
   - Time: O(n), Space: O(n)

3. Two Variables Approach (current implementation):
   - Only keep track of previous two values
   - Time: O(n), Space: O(1)

Key Insights:
- Cannot rob adjacent houses
- At each house, decide whether to rob it or not
- If we rob current house, we can't rob previous house
- If we don't rob current house, we can rob previous house

Test Cases:
- [1,2,3,1] → 4
- [2,7,9,3,1] → 12
- [2,1,1,2] → 4
- [1] → 1
- [1,2] → 2
*/
