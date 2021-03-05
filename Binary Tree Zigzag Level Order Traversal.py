Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
##########################################################
######### My Solution Using 2 Queues #####################
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        if (root is not None) and (root.left is None and root.right is None):
            return [[root.val]]
        
        q1=[]
        q2=[]
        q1.append(root)
        level_order_zigzag_traversal = []
        while q1 or q2:
            t=[]
            while q1:
                temp = q1.pop(0)
                t.append(temp.val)
                if temp.left:
                    q2.append(temp.left)
                if temp.right:
                    q2.append(temp.right)
            level_order_zigzag_traversal.append(t)
            t=[]
            while q2:
                temp=q2.pop(0)
                t.append(temp.val)
                if temp.left:
                    q1.append(temp.left)
                if temp.right:
                    q1.append(temp.right)
            if t:
                level_order_zigzag_traversal.append(t[::-1])
        return  level_order_zigzag_traversal 

#####################################################################
############ Using 1 Queue & 1 counter ##############################
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        if (root is not None) and (root.left is None and root.right is None):
            return [[root.val]]
        
        q1=[]
        q1.append(root)
        level_order_zigzag_traversal = []
        alternate = 0
        while q1 :
            c = len(q1)
            t = []
            while c>0:
                temp = q1.pop(0)
                t.append(temp.val)
                if temp.left:
                    q1.append(temp.left)
                if temp.right:
                    q1.append(temp.right)
                c-=1
            
            if alternate>0:
                level_order_zigzag_traversal.append(t[::-1])
                alternate-=1
            else :
                level_order_zigzag_traversal.append(t)
                alternate+=1
        return  level_order_zigzag_traversal    