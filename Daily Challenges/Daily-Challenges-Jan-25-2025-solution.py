# 🔄 LeetCode 2948 - Make Lexicographically Smallest Array by Swapping Elements

# **Difficulty:** Hard  
# **Problem Link:** [LeetCode 2948](https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements)

# 🧠 Problem Description 
# [Github LeetCode 2948 - Make Lexicographically Smallest Array by Swapping Elements](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/2948.%20Make%20Lexicographically%20Smallest%20Array%20by%20Swapping%20Elements)

class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: List[int]
        """
        n = len(nums)
        parent = list(range(n))
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py
        indexed_nums = [(val, idx) for idx, val in enumerate(nums)]
        indexed_nums.sort()
        for i in range(n - 1):
            if abs(indexed_nums[i][0] - indexed_nums[i + 1][0]) <= limit:
                union(indexed_nums[i][1], indexed_nums[i + 1][1])
        groups = {}
        for i in range(n):
            root = find(i)
            if root not in groups:
                groups[root] = []
            groups[root].append(nums[i])
        for key in groups:
            groups[key].sort()
        result = []
        indices = {key: 0 for key in groups}
        for i in range(n):
            root = find(i)
            result.append(groups[root][indices[root]])
            indices[root] += 1
        return result