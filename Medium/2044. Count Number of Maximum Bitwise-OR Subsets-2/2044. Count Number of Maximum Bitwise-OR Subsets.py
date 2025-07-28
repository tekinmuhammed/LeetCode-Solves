class Solution(object):
    def countMaxOrSubsets(self, nums):
        self.max_or = 0
        self.count = 0

        def dfs(i, cur_or):
            if i == len(nums):
                if cur_or > self.max_or:
                    self.max_or = cur_or
                    self.count = 1
                elif cur_or == self.max_or:
                    self.count += 1
                return
            # Dahil et
            dfs(i + 1, cur_or | nums[i])
            # Dahil etme
            dfs(i + 1, cur_or)

        dfs(0, 0)
        return self.count