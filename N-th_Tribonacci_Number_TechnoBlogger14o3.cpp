/**
 * LeetCode 75: N-th Tribonacci Number
 * 
 * Problem Statement:
 * The Tribonacci sequence Tn is defined as follows:
 * T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
 * Given n, return the value of Tn.
 * 
 * Example:
 * Input: n = 4
 * Output: 4
 * Explanation: T_3 = 0 + 1 + 1 = 2, T_4 = 1 + 1 + 2 = 4
 * 
 * Time Complexity: O(n)
 * Space Complexity: O(1) - optimized space
 * 
 * Approach:
 * 1. Handle base cases (n = 0, 1, 2)
 * 2. Use dynamic programming with space optimization
 * 3. Only keep track of the last 3 values instead of entire array
 * 
 * @author TechnoBlogger14o3
 * @date 2025
 */

class Solution {
public:
    int tribonacci(int n) {
        // Base cases
        if (n == 0) return 0;
        if (n == 1 || n == 2) return 1;
        
        // Space-optimized DP approach
        int a = 0, b = 1, c = 1;  // T0, T1, T2
        
        for (int i = 3; i <= n; i++) {
            int next = a + b + c;
            a = b;
            b = c;
            c = next;
        }
        
        return c;
    }
};

/*
Alternative approaches:

1. Recursive with Memoization (O(n) time, O(n) space):
   - Use unordered_map to store computed values
   - Avoid recomputing same subproblems

2. Bottom-up DP Array (O(n) time, O(n) space):
   - Create array of size n+1
   - Fill array iteratively

3. Matrix Exponentiation (O(log n) time, O(1) space):
   - For very large n values
   - More complex but extremely efficient

Test Cases:
- n = 0 → 0
- n = 1 → 1  
- n = 2 → 1
- n = 4 → 4
- n = 25 → 1389537
*/
