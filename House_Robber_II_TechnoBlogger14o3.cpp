/**
 * LeetCode 75: House Robber II
 * 
 * Problem Statement:
 * You are a professional robber planning to rob houses along a street.
 * Each house has a certain amount of money stashed. All houses at this place
 * are arranged in a circle. That means the first house is the neighbor of the last one.
 * Meanwhile, adjacent houses have a security system connected, and it will automatically
 * contact the police if two adjacent houses were broken into on the same night.
 * 
 * Given an integer array nums representing the amount of money of each house,
 * return the maximum amount of money you can rob tonight without alerting the police.
 * 
 * Example:
 * Input: nums = [2,3,2]
 * Output: 3
 * Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
 * because they are adjacent houses.
 * 
 * Time Complexity: O(n)
 * Space Complexity: O(1) - optimized space
 * 
 * Approach:
 * 1. Since houses are in a circle, first and last houses are adjacent
 * 2. We have two cases:
 *    - Rob houses 0 to n-2 (exclude last house)
 *    - Rob houses 1 to n-1 (exclude first house)
 * 3. Return maximum of these two cases
 * 4. Use the same DP approach as House Robber I for each case
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
        
        // Case 1: Rob houses 0 to n-2 (exclude last house)
        int case1 = robLinear(nums, 0, n - 2);
        
        // Case 2: Rob houses 1 to n-1 (exclude first house)
        int case2 = robLinear(nums, 1, n - 1);
        
        return max(case1, case2);
    }
    
private:
    // Helper function to solve linear house robber problem
    int robLinear(vector<int>& nums, int start, int end) {
        if (start > end) return 0;
        if (start == end) return nums[start];
        
        int prev2 = nums[start];
        int prev1 = max(nums[start], nums[start + 1]);
        
        for (int i = start + 2; i <= end; i++) {
            int current = max(nums[i] + prev2, prev1);
            prev2 = prev1;
            prev1 = current;
        }
        
        return prev1;
    }
};

/*
Alternative approaches:

1. Two Separate Arrays:
   - Create two arrays: one excluding first house, one excluding last house
   - Apply House Robber I algorithm to both
   - Time: O(n), Space: O(n)

2. In-place Modification:
   - Modify the input array for each case
   - Less memory efficient but simpler logic

Key Insights:
- Circular arrangement means first and last houses are adjacent
- We can't rob both first and last houses
- Break the problem into two linear subproblems
- Take maximum of both cases

Test Cases:
- [2,3,2] → 3
- [1,2,3,1] → 4
- [1,2,3] → 3
- [1] → 1
- [1,2] → 2
*/
