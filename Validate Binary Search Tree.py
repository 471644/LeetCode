Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [2,1,3]
Output: true
Example 2:


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
###########################################################
###########################################################
https://www.youtube.com/watch?v=yEwSGhSsT0U&ab_channel=mycodeschool
class Solution:
    def isValidBST(self,root,l=None,r=None):
        '''Base Condition'''
        if root == None:
            return True
        '''Left Node Should be Less than Root'''
        if (l!=None and root.val <= l.val):
            return False
        '''Right Node Should be grater than Root'''
        if (r!=None and root.val >= r.val):
            return False
        return self.isValidBST(root.left,l,root) and self.isValidBST(root.right,root,r)
        
########################################################
############### In-Order Solution ######################

https://www.geeksforgeeks.org/a-program-to-check-if-a-binary-tree-is-bst-or-not/
# Python implementation to check if  
# given Binary tree is a BST or not 
  
# A binary tree node containing data 
# field, left and right pointers 
class Node: 
    # constructor to create new node 
    def __init__(self, val): 
        self.data = val 
        self.left = None
        self.right = None
  
# global variable prev - to keep track 
# of previous node during Inorder  
# traversal 
prev = None
  
# function to check if given binary 
# tree is BST 
def isbst(root): 
      
    # prev is a global variable 
    global prev 
    prev = None
    return isbst_rec(root) 
  
  
# Helper function to test if binary 
# tree is BST 
# Traverse the tree in inorder fashion  
# and keep track of previous node 
# return true if tree is Binary  
# search tree otherwise false 
def isbst_rec(root): 
      
    # prev is a global variable 
    global prev  
  
    # if tree is empty return true 
    if root is None: 
        return True
  
    if isbst_rec(root.left) is False: 
        return False
  
    # if previous node'data is found  
    # greater than the current node's 
    # data return fals 
    if prev is not None and prev.data > root.data: 
        return False
  
    # store the current node in prev 
    prev = root 
    return isbst_rec(root.right) 
  
  
# driver code to test above function 
root = Node(4) 
root.left = Node(2) 
root.right = Node(5) 
root.left.left = Node(1) 
root.left.right = Node(3) 
  
if isbst(root): 
    print("is BST") 
else: 
    print("not a BST") 