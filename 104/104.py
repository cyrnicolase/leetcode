#!/usr/bin/python


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    depths = []
    
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 初始化一下全局变量
	# 这是这个题比较坑的地方,他可能会由一个对象多次调用本方法.所以全家变量需要在函数内初始化
        self.depths = []
        if None == root:
            return 0
        
        # 遍历后将所有的层数都写入到表中
        self.recu(root, 1)
        
        return max(self.depths)
        
    def recu(self, root, depth):
        if None == root:
            return
        
        self.depths.append(depth)
        self.recu(root.left, depth + 1)
        self.recu(root.right, depth + 1)
        
        
        
