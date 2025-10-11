#include <iostream>
using namespace std;

struct Node{
    int val;
    Node* left;
    Node* right;
    Node(int x){val=x;left=right=nullptr;}
};

bool check(Node* root){
    if(!root||(!root->left&&!root->right))return true;
    int leftVal=root->left?root->left->val:0;
    int rightVal=root->right?root->right->val:0;
    return (root->val==leftVal+rightVal)&&check(root->left)&&check(root->right);
}

int main(){
    Node* root=new Node(10);
    root->left=new Node(4);
    root->right=new Node(6);
    cout<<(check(root)?"True":"False")<<endl;
    return 0;
}
