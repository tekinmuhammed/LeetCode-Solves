# ⚙️ LeetCode 3354. Make Array Elements Equal to Zero

# **Difficulty:** Easy
# **Link:** [LeetCode 3354](https://leetcode.com/problems/make-array-elements-equal-to-zero/description/)

# 🧠 Problem Description
# [Github LeetCode 3354. Make Array Elements Equal to Zero](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/3354.%20Make%20Array%20Elements%20Equal%20to%20Zero)

class Solution:
    def countValidSelections(self, nums: list[int]) -> int:
        """
        nums dizisindeki tüm elemanları sıfıra eşitleyen geçerli başlangıç (curr) 
        ve hareket yönü kombinasyonlarının sayısını döndürür.
        """
        n = len(nums)
        valid_selections = 0
        total_sum = sum(nums)
        suffix_sum = total_sum
        prefix_sum = 0
        
        for i in range(n):
            suffix_sum -= nums[i] 
            if nums[i] == 0:
                diff = abs(prefix_sum - suffix_sum)
                
                if diff <= 1:
                    if diff == 0:
                        valid_selections += 2
                    elif diff == 1:
                        valid_selections += 1
            prefix_sum += nums[i]

        return valid_selections