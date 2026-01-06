# 1161. Maximum Level Sum of a Binary Tree

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 1123](https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/)

# 🧠 Problem Description
# [Github LeetCode 1161. Maximum Level Sum of a Binary Tree](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/1161.%20Maximum%20Level%20Sum%20of%20a%20Binary%20Tree)

from collections import deque

class Solution(object):
    def maxLevelSum(self, root):
        queue = deque([root])
        level = 1
        max_sum = float('-inf')
        answer = 1
        
        while queue:
            level_sum = 0
            size = len(queue)
            
            for _ in range(size):
                node = queue.popleft()
                level_sum += node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if level_sum > max_sum:
                max_sum = level_sum
                answer = level
            
            level += 1
        
        return answer