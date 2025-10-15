/**
 * LeetCode 75: K Closest Points to Origin
 * 
 * Problem Statement:
 * Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane
 * and an integer k, return the k closest points to the origin (0, 0).
 * The distance between two points on the X-Y plane is the Euclidean distance.
 * You may return the answer in any order.
 * 
 * Example:
 * Input: points = [[1,1],[2,2],[3,3]], k = 1
 * Output: [[1,1]]
 * Explanation: The distance between (1, 1) and the origin is sqrt(2).
 * The distance between (2, 2) and the origin is sqrt(8).
 * The distance between (3, 3) and the origin is sqrt(18).
 * Since sqrt(2) < sqrt(8) < sqrt(18), the closest point is (1, 1).
 * 
 * Time Complexity: O(n log k) - using max heap
 * Space Complexity: O(k) - heap size
 * 
 * Approach:
 * 1. Use a max heap (priority queue) to maintain k closest points
 * 2. For each point, calculate distance squared (avoid sqrt for efficiency)
 * 3. If heap size < k, add point
 * 4. If heap size == k and current point is closer, replace farthest point
 * 5. Return all points from heap
 * 
 * @author TechnoBlogger14o3
 * @date 2025
 */

import java.util.*;

class Solution {
    public int[][] kClosest(int[][] points, int k) {
        // Max heap to keep k closest points
        // Comparator compares distances (larger distance has higher priority)
        PriorityQueue<int[]> maxHeap = new PriorityQueue<>(
            (a, b) -> Integer.compare(getDistanceSquared(b), getDistanceSquared(a))
        );
        
        for (int[] point : points) {
            if (maxHeap.size() < k) {
                // Heap not full, add point
                maxHeap.offer(point);
            } else {
                // Heap is full, check if current point is closer than farthest in heap
                int[] farthest = maxHeap.peek();
                if (getDistanceSquared(point) < getDistanceSquared(farthest)) {
                    maxHeap.poll(); // Remove farthest point
                    maxHeap.offer(point); // Add current point
                }
            }
        }
        
        // Convert heap to array
        int[][] result = new int[k][2];
        int index = 0;
        while (!maxHeap.isEmpty()) {
            result[index++] = maxHeap.poll();
        }
        
        return result;
    }
    
    /**
     * Calculate distance squared from origin to avoid sqrt operation
     * @param point The point [x, y]
     * @return Distance squared from origin
     */
    private int getDistanceSquared(int[] point) {
        return point[0] * point[0] + point[1] * point[1];
    }
}

/*
Alternative approaches:

1. Sorting Approach:
   - Sort all points by distance
   - Take first k points
   - Time: O(n log n), Space: O(1)

2. Quick Select (Partition):
   - Use quick select algorithm to find kth smallest distance
   - Time: O(n) average, O(n^2) worst case, Space: O(1)

3. Min Heap:
   - Add all points to min heap
   - Extract k smallest
   - Time: O(n log n), Space: O(n)

Key Insights:
- Use distance squared to avoid expensive sqrt operation
- Max heap maintains k closest points efficiently
- When heap is full, only add closer points
- Comparator for max heap: larger distance has higher priority

Test Cases:
- [[1,1],[2,2],[3,3]], k=1 → [[1,1]]
- [[3,3],[5,-1],[-2,4]], k=2 → [[3,3],[-2,4]]
- [[1,1]], k=1 → [[1,1]]

Performance Analysis:
- Max Heap: O(n log k) time, O(k) space - Best for k << n
- Sorting: O(n log n) time, O(1) space - Best for k ≈ n
- Quick Select: O(n) time, O(1) space - Best for large n
*/
