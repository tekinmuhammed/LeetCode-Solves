# 2161. Partition Array According to Given Pivot

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 2161](https://leetcode.com/problems/partition-array-according-to-given-pivot/description/)

# 🧠 Problem Description  
# [Github LeetCode 2161. Partition Array According to Given Pivot](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/2161.%20Partition%20Array%20According%20to%20Given%20Pivot-2) 

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        equal = []
        greater = []

        for num in nums:
            if num < pivot:
                less.append(num)
            elif num > pivot:
                greater.append(num)
            else:
                equal.append(num)

        less.extend(equal)
        less.extend(greater)

        return less