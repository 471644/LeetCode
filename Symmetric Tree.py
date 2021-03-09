Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100
 

Follow up: Could you solve it both recursively and iteratively?

####################################################################
##################### Recursive Solution ###########################
'''Recursive Method'''
class Solution:
    def isMirror(self,root1,root2):
        if (root1 is None) and (root2 is None):
            return True
        if (root1 is not None) and (root2 is not None):
            if root1.val==root2.val:
                return ((self.isMirror(root1.left,root2.right)) and (self.isMirror(root1.right,root2.left)))
        return False
    
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root,root)


###################################################################
################ Iterative Solution ###############################
'''Iterative Method'''
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None :
            return True 
        if not root.left and not root.right:
            return True
        stack = []
        stack.append(root)
        stack.append(root)
        leftNode = 0
        rightNode = 0
        
        while (not len(stack)):
            leftNode = stack[0]
            stack.pop(0)
            rightNode = stack[0]
            stack.pop(0)
            
            if leftNode.val != rightNode.val:
                return False
            if leftNode.left and rightNode.right:
                stack.append(leftNode.left)
                stack.append(rightNode.right)
            elif leftNode.left or rightNode.right:
                return False
            if leftNode.right and rightNode.left:
                stack.append(leftnode.right)
                stack.append(rightNode.left)
            elif leftNode.right or rightNode.left:
                return False            
        
        return True
