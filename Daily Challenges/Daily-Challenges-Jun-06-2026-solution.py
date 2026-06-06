
# 🧠 Problem Description  
# [Github LeetCode 3753. Total Waviness of Numbers in Range II](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Hard/3753.%20Total%20Waviness%20of%20Numbers%20in%20Range%20II) 

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n

        left_sum = 0
        for i in range(n):
            ans[i] = left_sum
            left_sum += nums[i]

        right_sum = 0
        for i in range(n - 1, -1, -1):
            ans[i] = abs(ans[i] - right_sum)
            right_sum += nums[i]

        return ans