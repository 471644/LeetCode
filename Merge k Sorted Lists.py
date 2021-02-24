You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length won't exceed 10^4.

#################################################################
################## My Solution ##################################
######## Fails 1 Test Case where len(list[ListNode]) is huge ####

class Solution:
    
    def merge(self,list_1,list_2):
        merge = ListNode(-9999999999)
        head = merge
        while (list_1 is not None) and (list_2 is not None):
            if list_1.val>list_2.val:
                merge.next = ListNode(list_2.val)
                merge = merge.next
                list_2 = list_2.next
            elif list_1.val<list_2.val:
                merge.next = ListNode(list_1.val)
                merge = merge.next
                list_1 = list_1.next
            else:
                merge.next = ListNode(list_1.val)
                merge.next.next =ListNode(list_2.val)
                list_1=list_1.next
                list_2=list_2.next
                merge = merge.next.next
        if list_1 is not None:
            merge.next = list_1
        if list_2 is not None:
            merge.next = list_2
        return head.next
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists)<1 or (not lists):
            return None
        if len(lists)==1 and lists[0] is None:
            return None
        list_ = ListNode(-9999999)
        for i in range(len(lists)):
            if lists[i] is not None:
                list_ = self.merge(list_,lists[i])
        return list_.next
        
###########################################################
#################### Brute Force  #########################
###########################################################

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists)<1 or (not lists):
            return None
        if len(lists)==1 and lists[0] is None:
            return None
        node = []
        for i in lists:
            while i:
                node.append(i.val)
                i = i.next
        merged_ = ListNode(-9999)
        head = merged_
        for i in sorted(node):
            merged_.next = ListNode(i)
            merged_ = merged_.next
        return head.next

###########################################################
#################### Priority Queue #######################
###########################################################
from Queue import PriorityQueue

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = point = ListNode(0)
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put((l.val, l))
        while not q.empty():
            val, node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put((node.val, node))
        return head.next
        
        
###########################################################
#################### Divide & Conquer  ####################
###########################################################

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else None

    def merge2Lists(self, l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l1
                l1 = point.next.next
            point = point.next
        if not l1:
            point.next=l2
        else:
            point.next=l1
        return head.next