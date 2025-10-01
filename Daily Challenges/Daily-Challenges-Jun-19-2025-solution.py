# 2294. Partition Array Such That Maximum Difference Is K

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 2294](https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k)

# 🧠 Problem Description 
# [Github LeetCode 2294. Partition Array Such That Maximum Difference Is K](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/2294.%20Partition%20Array%20Such%20That%20Maximum%20Difference%20Is%20K)

class Solution(object):
    def partitionArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        count = 1
        start = nums[0]

        for num in nums:
            if num - start > k:
                count += 1
                start = num
        return count