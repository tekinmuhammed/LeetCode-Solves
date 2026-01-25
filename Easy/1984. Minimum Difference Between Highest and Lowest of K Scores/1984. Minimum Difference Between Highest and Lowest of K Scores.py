class Solution(object):
    def minimumDifference(self, nums, k):
        if k == 1:
            return 0

        nums.sort()
        res = float('inf')

        for i in range(len(nums) - k + 1):
            res = min(res, nums[i + k - 1] - nums[i])

        return res