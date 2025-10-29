class Solution {
public:
    string reverseWords(string s) {
        stringstream ss(s);
        string word, res;
        vector<string> words;
        while (ss >> word) words.push_back(word);
        reverse(words.begin(), words.end());
        for (int i = 0; i < words.size(); i++) {
            if (i) res += " ";
            res += words[i];
        }
        return res;
    }
};
