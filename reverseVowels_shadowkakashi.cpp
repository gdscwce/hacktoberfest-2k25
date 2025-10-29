class Solution {
public:
    string reverseVowels(string s) {
        int l = 0, r = s.size() - 1;
        string vowels = "aeiouAEIOU";
        while (l < r) {
            while (l < r && vowels.find(s[l]) == string::npos) l++;
            while (l < r && vowels.find(s[r]) == string::npos) r--;
            if (l < r) swap(s[l++], s[r--]);
        }
        return s;
    }
};
