#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
DocString
'''

# 给定一个树，按中序遍历重新排列树，使树中最左边的结点现在是树的根，并且每个结点没有左子结点，只有一个右子结点。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    root1 = result = TreeNode(None)

    def increasingBST(self, root):
        if None != root.left:
            self.increasingBST(root.left)

        unit = TreeNode(root.val)
        print(unit.val)
        if None == self.result.val:
            self.result = unit
            self.root1 = self.result
        else:
            self.result.right = unit
            self.result.left = None
            self.result = self.result.right
        

        if None != root.right:
            self.increasingBST(root.right)
        
        return self.root1




n1 = TreeNode(5)
n2 = TreeNode(3)
n3 = TreeNode(6)
n4 = TreeNode(2)
n5 = TreeNode(4)
n6 = TreeNode(1)
n7 = TreeNode(8)
n8 = TreeNode(7)
n9 = TreeNode(9)

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n4.left = n6
n3.right = n7
n7.left = n8
n7.right = n9

solution = Solution()
nodes = solution.increasingBST(n1)

