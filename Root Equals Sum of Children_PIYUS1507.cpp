#include <bits/stdc++.h>
using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

bool checkTree(TreeNode* root) {
    return root->val == (root->left->val + root->right->val);
}

int main() {
    // Example tree:
    //       10
    //      /  \
    //     4    6

    TreeNode* root = new TreeNode(10);
    root->left = new TreeNode(4);
    root->right = new TreeNode(6);

    cout << (checkTree(root) ? "true" : "false") << endl;

    // Output: true
    return 0;
}
