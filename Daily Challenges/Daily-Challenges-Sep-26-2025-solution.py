# 611. Valid Triangle Number

# **Difficulty:** Easy  
# **Link:** [LeetCode 611](https://leetcode.com/problems/valid-triangle-number/description/)  

# 🧠 Problem Description 
# [Github LeetCode 611. Valid Triangle Number](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/611.%20Valid%20Triangle%20Number)

class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        count = 0
        n = len(nums)

        # En büyük kenarı sabit al, diğer iki kenarı kontrol et
        for k in range(n - 1, 1, -1):
            i, j = 0, k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    count += (j - i)
                    j -= 1
                else:
                    i += 1
        return count