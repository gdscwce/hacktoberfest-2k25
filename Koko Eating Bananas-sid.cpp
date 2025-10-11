
class Solution {
public:
    int minimumRateToEatBananas(vector<int>& nums, int h) {
        int low = 1;
        int high = *max_element(nums.begin(), nums.end());
        int ans = high;

        auto canEatAll = [&](int k) {
            long long hours = 0;
            for (int pile : nums) {
                hours += (pile + k - 1) / k; 
            }
            return hours <= h;
        };

        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (canEatAll(mid)) {
                ans = mid;
                high = mid - 1;  
            } else {
                low = mid + 1;  
            }
        }

        return ans;
    }
};
