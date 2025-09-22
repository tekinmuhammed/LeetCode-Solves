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