class Solution(object):
    def minCapability(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def canRob(mid):
            count = 0
            i = 0
            while i < len(nums):
                if nums[i] <= mid:
                    count += 1
                    i += 1
                i += 1
            return count >= k
        left, right = min(nums), max(nums)
        while left < right:
            mid = (left + right) // 2
            if canRob(mid):
                right = mid
            else:
                left = mid + 1
        return left