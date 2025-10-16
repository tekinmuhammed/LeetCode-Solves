# 3005. Count Elements With Maximum Frequency

# **Difficulty:** Easy  
# **Link:** [LeetCode 3005](https://leetcode.com/problems/count-elements-with-maximum-frequency/description/)  

# 🧠 Problem Description 
# [Github LeetCode 3005. Count Elements With Maximum Frequency](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/3005.%20Count%20Elements%20With%20Maximum%20Frequency)

from collections import Counter

class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = Counter(nums)                # her elemanın frekansını bul
        max_freq = max(freq.values())       # en yüksek frekansı bul
        return sum(v for v in freq.values() if v == max_freq)