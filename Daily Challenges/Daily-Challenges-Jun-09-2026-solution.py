
# 🧠 Problem Description  
# [Github LeetCode 2161. Partition Array According to Given Pivot](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/2161.%20Partition%20Array%20According%20to%20Given%20Pivot-2) 
class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        m1 = min(nums)
        m2 = max(nums)
        return (m2 - m1) * k