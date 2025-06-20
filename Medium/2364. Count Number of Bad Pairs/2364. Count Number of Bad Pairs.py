class Solution(object):
    def countBadPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total_pairs = n * (n - 1) // 2
        diff_map = {}
        good_pairs = 0
        for i, num in enumerate(nums):
            diff = i - num
            if diff in diff_map:
                good_pairs += diff_map[diff]
            diff_map[diff] = diff_map.get(diff, 0) + 1
        return total_pairs - good_pairs