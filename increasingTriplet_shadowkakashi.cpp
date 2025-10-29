class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        int first = INT_MAX, second = INT_MAX;
        for (int n : nums) {
            if (n <= first) first = n;
            else if (n <= second) second = n;
            else return true;
        }
        return false;
    }
};
