#!/usr/bin/python

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
	    
    rests = []

    def __init__(self):
	self.rests = []
    
    def findTarget(self, root, k):
        result = self.doFind(root, k)

        return False if None == result else result
    
    def doFind(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        # print root.val, self.rests
        if root.val in self.rests:
            return True
        
        self.rests.append(k - root.val)
        if None != root.left:
            result = self.doFind(root.left, k)
            if None != result:
                return result
        if None != root.right:
            result = self.doFind(root.right, k)
            if None != result:
                return result
            
        return None


# input = [ 5, 3, 6, 2, 4, null, 7]
node1 = TreeNode(5)
node2 = TreeNode(3)
node3 = TreeNode(6)
node4 = TreeNode(2)
node5 = TreeNode(4)
node6 = TreeNode(7)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.right = node6

k = 28
s = Solution()
print s.findTarget(node1, k)

