class Solution {
public:
    int compress(vector<char>& chars) {
        int idx = 0;
        for (int i = 0; i < chars.size();) {
            char ch = chars[i];
            int count = 0;
            while (i < chars.size() && chars[i] == ch) {
                i++;
                count++;
            }
            chars[idx++] = ch;
            if (count > 1) {
                string cnt = to_string(count);
                for (char c : cnt) chars[idx++] = c;
            }
        }
        return idx;
    }
};
