class Solution(object):
    def maxSubsequence(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        indexed = list(enumerate(nums))
        indexed.sort(key=lambda x: x[1], reverse=True)
        top_k = sorted(indexed[:k], key=lambda x: x[0])
        return [val for i, val in top_k]