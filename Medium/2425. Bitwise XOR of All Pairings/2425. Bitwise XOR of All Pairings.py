class Solution(object):
    def xorAllNums(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        xor1, xor2 = 0, 0
        for num in nums1:
            xor1 ^= num
        for num in nums2:
            xor2 ^= num
        len1, len2 = len(nums1), len (nums2)

        result = 0
        if len2 % 2 == 1:
            result ^= xor1
        if len1 % 2 == 1:
            result ^= xor2
        return result
