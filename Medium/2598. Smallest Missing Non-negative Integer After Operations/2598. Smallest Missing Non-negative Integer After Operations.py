class Solution(object):
    def findSmallestInteger(self, nums, value):
        """
        :type nums: List[int]
        :type value: int
        :rtype: int
        """
        from collections import Counter
        
        # Her sayıyı 'value' ile mod al (negatifler için normalize et)
        count = Counter(x % value for x in nums)
        
        # MEX hesapla
        mex = 0
        while True:
            remainder = mex % value
            if count[remainder] > 0:
                count[remainder] -= 1
                mex += 1
            else:
                return mex