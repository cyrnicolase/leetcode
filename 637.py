import queue


class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 使用层次遍历，针对每一层进行平均数计算
    def averageOfLevels(self, root):
        level = 0
        result = {}
        q = queue.Queue()
        q.put((root, level))
        while not q.empty():
            node, level = q.get()
            if level in result:
                result[level].append(node.val)
            else:
                result[level] = [node.val]

            if node.left:
                q.put((node.left, level + 1))
            if node.right:
                q.put((node.right, level + 1))


        data = []
        for item in result.values():
            total = sum(item)
            data.append(total / len(item))

        return data


n1 = Node(3)
n2 = Node(9)
n3 = Node(20)
n4 = Node(15)
n5 = Node(7)

n1.left = n2
n1.right = n3
n3.left = n4
n3.right = n5

solution = Solution()
result = solution.averageOfLevels(n1)
print(result)