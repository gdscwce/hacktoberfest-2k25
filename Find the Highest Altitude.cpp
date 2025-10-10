#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int sum = 0, maxi = 0;
        for (int x : gain) {
            sum += x;
            maxi = max(maxi, sum);
        }
        return maxi;
    }
};
