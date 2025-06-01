class Solution(object):
    def findScore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        score = 0
        n = len(nums)
        marked = [False] * n
        indexed_nums = [(nums[i], i) for i in range(n)]
        indexed_nums.sort()
        for value, index in indexed_nums:
            if not marked[index]:
                score += value
                marked[index] = True
                if index > 0:
                    marked[index - 1] = True
                if index <n - 1:
                    marked[index + 1] = True
        return score