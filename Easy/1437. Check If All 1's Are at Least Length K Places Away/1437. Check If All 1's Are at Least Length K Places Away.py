class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        prev = -1  # previous 1's index

        for i, val in enumerate(nums):
            if val == 1:
                if prev != -1 and i - prev - 1 < k:
                    return False
                prev = i

        return True