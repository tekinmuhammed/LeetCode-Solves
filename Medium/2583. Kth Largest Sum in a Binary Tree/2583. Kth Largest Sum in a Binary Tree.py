from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def buildTree(self, values):
        if not values:
            return None
        root = TreeNode(values[0])
        queue = deque([root])
        i = 1
        while i< len(values):
            node = queue.popleft()
            if i < len(values):
                node.left = TreeNode(values[i])
                queue.append(node.left)
                i += 1
            if i < len(values):
                node.right = TreeNode(values[i])
                queue.append(node.right)
                i += 1
        return root
    def kthLargestLevelSum(self, root, k):
        if not root:
            return -1
        level_sums = []
        queue = deque([root])
        while queue:
            level_sum = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level_sums.append(level_sum)
        level_sums.sort(reverse=True)
        if len(level_sums) < k:
            return -1
        return level_sums[k-1]

root_values = [5, 8, 9, 2, 1, 3, 7, 4, 6]
k = 2

solution = Solution()
root = solution.buildTree(root_values)
result = solution.kthLargestLevelSum(root, k)
print(result)