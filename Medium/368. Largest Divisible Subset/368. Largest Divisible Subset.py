class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        nums.sort()
        n = len(nums)
        dp = [1] * n
        prev = [-1] * n
        max_index = 0
        
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev[i] = j
            if dp[i] > dp[max_index]:
                max_index = i
        result = []
        while max_index != -1:
            result.append(nums[max_index])
            max_index = prev[max_index]
        return result[::-1]