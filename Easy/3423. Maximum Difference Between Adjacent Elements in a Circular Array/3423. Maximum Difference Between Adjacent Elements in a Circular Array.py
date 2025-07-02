class Solution(object):
    def maxAdjacentDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_diff = 0
        n = len(nums)

        for i in range(n):
            j = (i + 1) % n
            diff = abs(nums[i] - nums[j])
            max_diff = max(max_diff, diff)
        return max_diff