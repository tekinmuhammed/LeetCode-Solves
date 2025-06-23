import heapq
class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heapq.heapify(nums)
        operations = 0
        while len(nums) > 1 and nums[0] < k:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            new_value = x * 2 + y
            heapq.heappush(nums, new_value)
            operations += 1
        if nums[0] < k:
            return -1
        return operations