
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution:
    count = 0
    result = {}

    def middleNode(self, head):
        if None != head:
            current = head
            self.result[self.count] = current
            self.count += 1
            head = head.next
            return self.middleNode(head)
        else:
            return self.result[self.count // 2]

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n6 = ListNode(6)
n7 = ListNode(7)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
# n6.next = n7

solution = Solution()
solution.middleNode(n1)