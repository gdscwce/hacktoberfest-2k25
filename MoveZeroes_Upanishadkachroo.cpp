/*
 * Description:
 * Given an integer array nums, move all 0's to the end of it
 * while maintaining the relative order of the non-zero elements.
 * The operation must be done in-place without making a copy of the array.
 *
 * Approach:
 * - Use a two-pointer technique.
 * - One pointer (insertPos) keeps track of the position to place the next non-zero element.
 * - Traverse the array; whenever a non-zero element is found, move it to nums[insertPos] and increment insertPos.
 * - After placing all non-zero elements, fill the rest of the array with zeros.
 *
 * Time Complexity: O(n)   // Single traversal of the array
 * Space Complexity: O(1)  // In-place operation, no extra array used
 */

#include <iostream>
#include <vector>
using namespace std;

void moveZeroes(vector<int> &nums)
{
    int insertPos = 0;

    // move all non-zero elements to the front
    for (int num : nums)
    {
        if (num != 0)
        {
            nums[insertPos++] = num;
        }
    }

    // fill remaining positions with zeros
    while (insertPos < nums.size())
    {
        nums[insertPos++] = 0;
    }
}

int main()
{
    vector<int> nums = {0, 1, 0, 3, 12};
    moveZeroes(nums);

    cout << "After moving zeroes: ";
    for (int num : nums)
    {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}

