#include <bits/stdc++.h>
using namespace std;

int maxOperations(vector<int>& nums, int k) {
    unordered_map<int, int> freq;
    int count = 0;

    for (int num : nums) {
        int complement = k - num;

        // if complement already exists, form a pair
        if (freq[complement] > 0) {
            count++;
            freq[complement]--; // use up one complement
        } 
        else {
            freq[num]++; // store current num for future pairing
        }
    }

    return count;
}

int main() {
    vector<int> nums = {1, 2, 3, 4};
    int k = 5;

    cout << maxOperations(nums, k) << endl;
    return 0;
}
