A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any path.

 

Example 1:


Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
Example 2:


Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
 

Constraints:

The number of nodes in the tree is in the range [1, 3 * 104].
-1000 <= Node.val <= 1000

###############################################
###############################################
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if root.left is None and root.right is None:
            return root.val
               
        def maxPathSumUtil(root):
            if root is None:
                return 0
            ls = maxPathSumUtil(root.left)
            rs = maxPathSumUtil(root.right)
            max_single = max(max(ls,rs)+root.val,root.val)
            max_top = max(max_single,ls+rs+root.val)
            maxPathSumUtil.val = max(maxPathSumUtil.val,max_top)
            return max_single
        maxPathSumUtil.val = -999999    
        maxPathSumUtil(root)
        return maxPathSumUtil.val