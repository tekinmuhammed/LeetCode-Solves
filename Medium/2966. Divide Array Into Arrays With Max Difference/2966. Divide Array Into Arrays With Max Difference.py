class Solution(object):
    def divideArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        for i in range(0, len(nums), 3):
            group = nums[i:i+3]
            if len(group) < 3 or group[-1] - group[0] > k:
                return []
            result.append(group)
        return result