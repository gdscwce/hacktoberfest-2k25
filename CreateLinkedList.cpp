#include<bits/stdc++.h>
using namespace std;

struct Node
{
    int data;
    Node* next;

    Node(int val)
    {
        data = val;
        next = NULL;
    }
};

Node* createLL(vector<int>& nums)
{
    if (nums.empty()) return NULL;

    Node* head = new Node(nums[0]);
    Node* current = head;

    for (size_t i = 1; i < nums.size(); ++i)
    {
        current->next = new Node(nums[i]);
        current = current->next;
    }

    return head;
}

void printLL(Node* head){
    Node* current = head;
    while(current != NULL){
        cout<<current->data<<" ";
        current = current->next;
    }
    cout<<endl;
}

int main(){
    vector<int> nums = {1,2,3,4,5};
    Node* head = createLL(nums);
    printLL(head);
    return 0;
}