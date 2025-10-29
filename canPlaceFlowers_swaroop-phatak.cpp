class Solution {
public:
    bool canPlaceFlowers(vector<int>& f, int n) {
        for (int i = 0; i < f.size() && n > 0; i++) {
            if (f[i] == 0) {
                int prev = (i == 0) ? 0 : f[i - 1];
                int next = (i == f.size() - 1) ? 0 : f[i + 1];
                if (prev == 0 && next == 0) {
                    f[i] = 1;
                    n--;
                }
            }
        }
        return n == 0;
    }
};
