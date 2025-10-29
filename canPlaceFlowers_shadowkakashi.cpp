class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        for (int i = 0; i < flowerbed.size() && n > 0; ++i) {
            if (flowerbed[i] == 0) {
                bool left = (i == 0) || (flowerbed[i-1] == 0);
                bool right = (i == flowerbed.size()-1) || (flowerbed[i+1] == 0);
                if (left && right) {
                    flowerbed[i] = 1;
                    --n;
                }
            }
        }
        return n == 0;
    }
};
