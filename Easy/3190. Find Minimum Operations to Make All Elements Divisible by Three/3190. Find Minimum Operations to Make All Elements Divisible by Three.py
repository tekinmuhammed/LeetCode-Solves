class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        operations = 0
        for x in nums:
            if x % 3 != 0:
                operations += 1
        return operations