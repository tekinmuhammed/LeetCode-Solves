class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        left = [num for num in nums if num < pivot]
        middle = [num for num in nums if num == pivot]
        right = [num for num in nums if num > pivot]
        return left + middle + right