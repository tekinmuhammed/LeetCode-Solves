class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        result = []
        current = 0
        
        for bit in nums:
            # keep prefix mod 5 only
            current = (current * 2 + bit) % 5
            result.append(current == 0)
        
        return result