
# https://leetcode.com/problems/add-two-numbers/description/

# 需要注意的是，节点指针需要不断的向后移动，不然，就只能是两位数，不断的覆盖第二个节点

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    
    up = 0
    result = None
    root = None
   
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        
        n1 = None
        n2 = None
        newNode = None

            
        if None == l1 and None == l2 and 0 == self.up:
            return self.root
        
        if None != l1 or None != l2 or self.up > 0:
            newNode = ListNode(0)
        
        
        if self.up > 0:
            newNode.val += self.up
            self.up = 0
            
        if None != l1:
            newNode.val += l1.val
            n1 = l1.next
        
        if None != l2:
            newNode.val += l2.val
            n2 = l2.next
            
        if newNode.val > 9:
            self.up = 1
            newNode.val = newNode.val % 10
            
        # print newNode.val
        if self.result:
            self.result.next = newNode
            self.result = self.result.next
        else:
            self.root = self.result = newNode
            
        return self.addTwoNumbers(n1, n2)
            
        
            
