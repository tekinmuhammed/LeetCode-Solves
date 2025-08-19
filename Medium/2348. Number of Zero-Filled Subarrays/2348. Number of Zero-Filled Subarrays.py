class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        result = 0

        for n in nums:
            if n == 0:
                count += 1
                result += count
            else:
                count = 0
        return result