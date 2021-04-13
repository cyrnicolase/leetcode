
# https://leetcode.com/problems/merge-two-binary-trees/description/


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """ 

        if None == t1:
            return t2
        if None == t2:
            return t1
        
        t1.val += t2.val
        
        if t1.left and t2.left:
            self.mergeTrees(t1.left, t2.left)
        if t1.right and t2.right:
            self.mergeTrees(t1.right, t2.right)
        if t2.left and t1.left == None:
            t1.left = t2.left
        if t2.right and t1.right == None: 
            t1.right = t2.right
        
        return t1
