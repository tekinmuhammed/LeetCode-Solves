# 🟨 LeetCode 2593 - Find Score of an Array After Marking All Elements

#  **Difficulty:** Medium  
#  **Problem Link:** [LeetCode 2593](https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/)

# 🧠 Problem Description 
# [Github LeetCode 2593 - Find Score of an Array After Marking All Elements](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/2593.%20Find%20Score%20of%20an%20Array%20After%20Marking%20All%20Elements)

class Solution(object):
    def findScore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        score = 0
        n = len(nums)
        marked = [False] * n
        indexed_nums = [(nums[i], i) for i in range(n)]
        indexed_nums.sort()
        for value, index in indexed_nums:
            if not marked[index]:
                score += value
                marked[index] = True
                if index > 0:
                    marked[index - 1] = True
                if index <n - 1:
                    marked[index + 1] = True
        return score