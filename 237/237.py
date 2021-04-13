#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
DocString
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        # 将当前节点变为下一个节点
        node.val = node.next.val
        node.next = node.next.next

