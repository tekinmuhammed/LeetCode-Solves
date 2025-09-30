# 2616. Minimize the Maximum Difference of Pairs

# **Problem Link:** [LeetCode 2616](https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/)  
# **Difficulty:** Medium

# 🧠 Problem Description 
# [Github  2616. Minimize the Maximum Difference of Pairs](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/2616.%20Minimize%20the%20Maximum%20Difference%20of%20Pairs)

class Solution(object):
    def minimizeMax(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        nums.sort()
        
        def can_form_pairs(threshold):
            count = 0
            i = 1
            while i < len(nums):
                if nums[i] - nums[i - 1] <= threshold:
                    count += 1
                    i += 2  # skip both used elements
                else:
                    i += 1
            return count >= p
        
        left, right = 0, nums[-1] - nums[0]
        
        while left < right:
            mid = (left + right) // 2
            if can_form_pairs(mid):
                right = mid
            else:
                left = mid + 1
        
        return left