class Solution {
public:
    int compress(vector<char>& chars) {
        int i = 0, ans = 0;
        while (i < chars.size()) {
            int j = i;
            while (j < chars.size() && chars[j] == chars[i]) j++;
            chars[ans++] = chars[i];
            if (j - i > 1) {
                string cnt = to_string(j - i);
                for (char c : cnt) chars[ans++] = c;
            }
            i = j;
        }
        return ans;
    }
};
