Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

Follow up:

Could you solve the problem in O(1) extra memory space?
You may not alter the values in the list's nodes, only nodes itself may be changed.
 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
Example 3:

Input: head = [1,2,3,4,5], k = 1
Output: [1,2,3,4,5]
Example 4:

Input: head = [1], k = 1
Output: [1]
 

Constraints:

The number of nodes in the list is in the range sz.
1 <= sz <= 5000
0 <= Node.val <= 1000
1 <= k <= sz

##################################################
############### Recursive Solution ###############

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        iter_ = head
        count = 0
        while iter_:
            count+=1
            if count==k:
                break
            iter_=iter_.next
        if count<k:
            return head
        
        post = self.reverseKGroup(iter_.next,k)
        prev_,curr_,next_=None,head,None
        
        for i in range(k):
            next_ = curr_.next
            curr_.next = prev_
            prev_ = curr_
            curr_ = next_
        
        head.next = post 
        return prev_
        
##################################################
############### Iterative Solution ###############

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        length = 0
        node = head
        
        while node:
            length += 1
            node = node.next
        
        startNode = ListNode()
        prevGroupTail = startNode
        node = head
        
        while node:
            if length >= k:
                tailNode = None
                curGroupTail = node
                curNode = node
                
                for _ in range(k):
                    nxtNode = curNode.next
                    curNode.next = tailNode
                    tailNode = curNode
                    curNode = nxtNode
                
                node = curNode
                prevGroupTail.next = tailNode
                length -= k
                prevGroupTail = curGroupTail
            
            else:
                prevGroupTail.next = node
                length = 0
                node = None
        
        return startNode.next

