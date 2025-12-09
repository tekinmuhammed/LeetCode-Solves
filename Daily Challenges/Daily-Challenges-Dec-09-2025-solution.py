# 3583. Count Special Triplets

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 3583](https://leetcode.com/problems/count-special-triplets/description/)

# 🧠 Problem Description
# [Github LeetCode 3583. Count Special Triplets](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/3583.%20Count%20Special%20Triplets)

class Solution(object):
    def specialTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        
        from collections import Counter
        
        # Count of each number to the right of the current index
        right = Counter(nums)
        left = Counter()
        
        ans = 0
        
        for j, val in enumerate(nums):
            right[val] -= 1
            if right[val] == 0:
                del right[val]
            
            target = val * 2
            
            # Count how many i < j satisfy nums[i] = 2 * nums[j]
            count_i = left.get(target, 0)
            
            # Count how many k > j satisfy nums[k] = 2 * nums[j]
            count_k = right.get(target, 0)
            
            ans = (ans + count_i * count_k) % MOD
            
            left[val] += 1
        
        return ans