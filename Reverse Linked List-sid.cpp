
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* prev = nullptr;
        ListNode* curr = head;

        while (curr != nullptr) {
            ListNode* nextNode = curr->next;  
            curr->next = prev;                
            prev = curr;                      
            curr = nextNode;                 
        }

        return prev; // New head
    }
};
