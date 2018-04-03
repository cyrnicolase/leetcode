#!/usr/bin/python

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
    
        root = l3 = ListNode(0)
        while None != l1 and None != l2:
            while None != l1 and None != l2 and l1.val <= l2.val:
                tmp = l1.next
                l3.next = l1
                l1 = tmp
                l3 = l3.next

            while None != l1 and None != l2 and l1.val > l2.val:
                tmp = l2.next
                l3.next = l2
                l2 = tmp
                l3 = l3.next

        if None != l1:
            l3.next = l1

        if None != l2:
            l3.next = l2

        return root.next






node11 = ListNode(1)
node12 = ListNode(2)
node13 = ListNode(4)

node11.next = node12
node12.next = node13

l1 = node11

node21 = ListNode(1)
node22 = ListNode(3)
node23 = ListNode(4)

node21.next = node22
node22.next = node23

l2 =  node21


so = Solution()
l3 = so.mergeTwoLists(l1, l2)

while None != l3:
    print l3.val
    l3 = l3.next


