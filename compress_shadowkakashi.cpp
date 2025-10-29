class Solution {
public:
    int compress(vector<char>& chars) {
        int i = 0, idx = 0;
        while (i < chars.size()) {
            char curr = chars[i];
            int count = 0;
            while (i < chars.size() && chars[i] == curr) {
                i++;
                count++;
            }
            chars[idx++] = curr;
            if (count > 1) {
                for (char c : to_string(count)) {
                    chars[idx++] = c;
                }
            }
        }
        return idx;
    }
};
