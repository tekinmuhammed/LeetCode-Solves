class Solution(object):
    def maxCount(self, banned, n, maxSum):
        """
        :type banned: List[int]
        :type n: int
        :type maxSum: int
        :rtype: int
        """
        banned_set = set(banned)
        current_sum = 0
        count = 0
        for num in range(1, n + 1):
            if num not in banned_set and current_sum + num <= maxSum:
                current_sum += num
                count += 1
        return count