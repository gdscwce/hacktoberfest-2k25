class Solution {
public:
    string reverseVowels(string s) {
        int i = 0, j = s.size() - 1;
        string v = "aeiouAEIOU";
        while (i < j) {
            while (i < j && v.find(s[i]) == string::npos) i++;
            while (i < j && v.find(s[j]) == string::npos) j--;
            swap(s[i++], s[j--]);
        }
        return s;
    }
};
