/**
 * LeetCode 75: Min Cost Climbing Stairs
 * 
 * Problem Statement:
 * You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
 * Once you pay the cost, you can either climb one or two steps.
 * You can either start from the step with index 0, or the step with index 1.
 * Return the minimum cost to reach the top of the floor.
 * 
 * Example:
 * Input: cost = [10,15,20]
 * Output: 15
 * Explanation: You will start at index 1. Pay 15 and climb two steps to reach the top.
 * 
 * Time Complexity: O(n)
 * Space Complexity: O(1) - optimized space
 * 
 * Approach:
 * 1. Use dynamic programming with space optimization
 * 2. At each step, choose minimum cost between one step back or two steps back
 * 3. The answer is minimum of last two steps (since we can start from step 0 or 1)
 * 
 * @author TechnoBlogger14o3
 * @date 2025
 */

class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int n = cost.size();
        
        // Base cases
        if (n <= 1) return 0;
        if (n == 2) return min(cost[0], cost[1]);
        
        // Space-optimized DP approach
        int prev2 = cost[0];  // cost to reach step 0
        int prev1 = cost[1];  // cost to reach step 1
        
        for (int i = 2; i < n; i++) {
            int current = cost[i] + min(prev1, prev2);
            prev2 = prev1;
            prev1 = current;
        }
        
        // Can reach top from either last step or second last step
        return min(prev1, prev2);
    }
};

/*
Alternative approaches:

1. Top-down DP with Memoization:
   - Recursive function with memoization
   - Time: O(n), Space: O(n)

2. Bottom-up DP Array:
   - Create dp array of size n+1
   - dp[i] = cost[i] + min(dp[i-1], dp[i-2])
   - Time: O(n), Space: O(n)

3. Modified Input Array:
   - Modify the input array in-place
   - Space: O(1) but modifies input

Key Insights:
- We can start from step 0 or step 1 (both are free)
- At each step, we choose the minimum cost path
- The final answer is min of reaching last step or second last step

Test Cases:
- [10,15,20] → 15
- [1,100,1,1,1,100,1,1,100,1] → 6
- [0,0,0,0] → 0
- [1,2] → 1
*/
