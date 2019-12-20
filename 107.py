import queue

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root):
        if None == root:
            return None
        
        result = {}
        q = queue.Queue()
        level = 0
        q.put((root, level))
        while not q.empty():
            (node, level) = q.get()
            if level in result:
                result[level].append(node.val)
            else:
                result[level] = [node.val]

            if None != node.left:
                q.put((node.left, level + 1))
            if None != node.right:
                q.put((node.right, level + 1))

        output = []
        keys = sorted(result, reverse=True)
        for k in keys:
            output.append(result[k])

        return output


n1 = TreeNode(3)
n2 = TreeNode(9)
n3 = TreeNode(20)
n4 = TreeNode(15)
n5 = TreeNode(7)

n1.left = n2
n1.right = n3
n3.left = n4
n3.right = n5

solution = Solution()
result = solution.levelOrderBottom(n1)

print(result)
