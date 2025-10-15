# 1493. Longest Subarray of 1's After Deleting One Element

# **Difficulty:** Medium
# **Link:** [LeetCode 1493](https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/)  

# 🧠 Problem Description
# [Github LeetCode 1493. Longest Subarray of 1's After Deleting One Element](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/1493.%20Longest%20Subarray%20of%201's%20After%20Deleting%20One%20Element)

class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        zero_count = 0
        max_len = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            # Eğer 0 sayısı 1’den fazlaysa sol pointer kaydır
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            # (right - left) çünkü bir eleman silmek zorundayız
            max_len = max(max_len, right - left)

        return max_len