from collections import defaultdict
class Solution(object):
    def tupleSameProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        product_map = defaultdict(int)
        result = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                product = nums[i] * nums[j]
                result += 8 * product_map[product]
                product_map[product] += 1
        return result