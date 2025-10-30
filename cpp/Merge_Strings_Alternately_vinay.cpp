#include <iostream>
#include <string>
using namespace std;

string mergeAlternately(string word1, string word2) {
    string result = "";
    int i = 0, j = 0;

    while (i < word1.length() && j < word2.length()) {
        result += word1[i++];
        result += word2[j++];
    }

    while (i < word1.length()) result += word1[i++];
    while (j < word2.length()) result += word2[j++];

    return result;
}

int main() {
    string word1, word2;
    cout << "Enter first string: ";
    cin >> word1;
    cout << "Enter second string: ";
    cin >> word2;

    cout << "Merged String: " << mergeAlternately(word1, word2) << endl;
    return 0;
}
