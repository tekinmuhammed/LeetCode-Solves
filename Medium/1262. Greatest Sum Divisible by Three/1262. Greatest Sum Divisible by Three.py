class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)

        # smallest numbers with remainder 1 and 2
        r1 = []
        r2 = []

        for x in nums:
            if x % 3 == 1:
                r1.append(x)
            elif x % 3 == 2:
                r2.append(x)

        r1.sort()
        r2.sort()

        if total % 3 == 0:
            return total

        # Case remainder 1
        if total % 3 == 1:
            option1 = r1[0] if len(r1) >= 1 else float('inf')
            option2 = sum(r2[:2]) if len(r2) >= 2 else float('inf')
            return total - min(option1, option2)

        # Case remainder 2
        if total % 3 == 2:
            option1 = r2[0] if len(r2) >= 1 else float('inf')
            option2 = sum(r1[:2]) if len(r1) >= 2 else float('inf')
            return total - min(option1, option2)