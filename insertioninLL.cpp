#include <bits/stdc++.h>
using namespace std;

struct Node
{
    int data;
    Node *next;
    Node(int val)
    {
        data = val;
        next = nullptr;
    }
};

Node *createLL(vector<int> &nums)
{
    if (nums.empty())
        return nullptr;

    Node *head = new Node(nums[0]);
    Node *current = head;

    for (int i = 1; i < nums.size(); i++)
    {
        current->next = new Node(nums[i]);
        current = current->next;
    }
    return head;
}

void PrintLL(Node *head)
{
    while (head != nullptr)
    {
        cout << head->data << " " << head->next << endl;
        head = head->next;
    }
    cout << endl;
}

Node *InsertAtHead(Node *head, int val)
{
    Node *temp = new Node(val);
    temp->next = head;
    return temp;
}

Node *InsertAtKthPosition(Node *head, int k, int val)
{
    if (k <= 0 || head == nullptr)
        return head;
    if (k == 1)
    {
        Node *temp = new Node(val);
        temp->next = head;
        return temp;
    }

    Node *curr = head;
    for (int i = 1; i < k - 1 && curr != nullptr; i++)
    {
        curr = curr->next;
    }
    Node *temp = new Node(val);
    temp->next = curr->next;
    curr->next = temp;
    return head;
}

Node *insertatkthvalueelem(Node *head, int k, int val)
{
    if (head == nullptr)
        return head;

    Node *curr = head;
    while (curr != nullptr && curr->data != k)
    {
        curr = curr->next;
    }
    if (curr == nullptr)
    {
        return head;
    }

    Node *temp = new Node(val);
    temp->next = curr->next;
    curr->next = temp;
    return head;
}

Node *InsertAtTail(Node *head, int val)
{
    Node *temp = new Node(val);

    if (head == nullptr)
    {
        return temp;
    }
    Node *curr = head;
    while (curr->next != nullptr)
    {
        curr = curr->next;
    }
    curr->next = temp;
    return head;
}

int main()
{
    vector<int> nums = {1, 2, 3, 4, 5};
    Node *head = createLL(nums);
    PrintLL(head);
    head = InsertAtHead(head, 0);
    head= InsertAtTail(head, 6);
    head= InsertAtKthPosition(head, 4, 8);
    head = insertatkthvalueelem(head, 3, 9);
    PrintLL(head);
    return 0;
}
