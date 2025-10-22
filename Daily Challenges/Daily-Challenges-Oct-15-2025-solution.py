# 🧩 3350. Adjacent Increasing Subarrays Detection II

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 3350](https://leetcode.com/problems/adjacent-increasing-subarrays-detection-ii/description/)

# 🧠 Problem Description 
# [Github LeetCode 3350. Adjacent Increasing Subarrays Detection II](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/3350.%20Adjacent%20Increasing%20Subarrays%20Detection%20II)

class Solution(object):
    def maxIncreasingSubarrays(self, nums: list[int]) -> int:
        N = len(nums)
        if N < 2:
            return 0
        increase_len = [0] * N
        increase_len[N - 1] = 1
        
        for i in range(N - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                increase_len[i] = 1 + increase_len[i + 1]
            else:
                increase_len[i] = 1
        def can_find(k):
            if k == 0:
                return True
            if 2 * k > N:
                return False
            for a in range(N - 2 * k + 1):
                is_first_increasing = increase_len[a] >= k
                is_second_increasing = increase_len[a + k] >= k
                
                if is_first_increasing and is_second_increasing:
                    return True
            
            return False
        low = 0
        high = N // 2
        max_k = 0
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if can_find(mid):
                max_k = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return max_k