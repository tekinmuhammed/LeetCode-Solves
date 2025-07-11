class Solution(object):
    def triangleType(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        a, b, c = sorted(nums)

        if a + b <= c:
            return "none"
        
        if a == b == c:
            return "equilateral"

        if a == b or b == c or a == c:
            return "isosceles"
        
        return "scalene"