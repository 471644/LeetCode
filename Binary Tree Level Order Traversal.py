Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000

#################################################
########### Using Counter & A  Queue ############

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        if (root is not None) and (root.left is None and root.right is None):
            return [[root.val]]
        
        queue = []
        level_order_traversal = []
        queue.append(root)
        while queue:
            t = []
            count = len(queue)
            while count>0:
                temp = queue.pop(0)
                t.append(temp.val)
                if temp.left is not None:
                    queue.append(temp.left)
                if temp.right is not None:
                    queue.append(temp.right)
                count-=1
            level_order_traversal.append(t)
        return level_order_traversal
        
###############################################
############## Using 2 Queues #################
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        if (root is not None) and (root.left is None and root.right is None):
            return [[root.val]]
        
        q1=[]
        q2=[]
        l_o_t =[]
        q1.append(root)
        while q1 or q2:
            t=[]
            while q1:
                temp = q1.pop(0)
                t.append(temp.val)
                if temp.left :
                    q2.append(temp.left)
                if temp.right :
                    q2.append(temp.right)
                
            l_o_t.append(t)
            t=[]
            while q2:
                temp=q2.pop(0)
                t.append(temp.val)
                if temp.left:
                    q1.append(temp.left)
                if temp.right:
                    q1.append(temp.right)
                    
            if t :
                l_o_t.append(t)
        return l_o_t