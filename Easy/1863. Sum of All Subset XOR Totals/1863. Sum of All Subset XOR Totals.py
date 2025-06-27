class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.total = 0
        def dfs(index, current_xor):
            if index == len(nums):
                self.total += current_xor
                return
            dfs(index + 1, current_xor)
            dfs(index + 1, current_xor ^ nums[index])
        dfs(0, 0)
        return self.total