Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
########################################################
################## Itrative Solution ###################
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        if (not head) or (not head.next):
            return head
        curr_ = head
        prev_ = None
        next_ = None
        while curr_:
            next_ = curr_.next
            curr_.next= prev_
            prev_ = curr_
            curr_ = next_
        return prev_
        
######################################################
################ Recursive Solution ##################
class Solution:
    def reverse(self,curr_):
        if curr_ == None or curr_.next == None:
            return curr_
         
        tail = self.reverse(curr_.next)
        curr_.next.next = curr_
        curr_.next = None
        return tail
    def reverseList(self, head: ListNode) -> ListNode:
        return self.reverse(head) 