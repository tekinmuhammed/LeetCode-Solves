class Solution(object):
    def countMaxOrSubsets(self, nums):
        def dfs(index, current_or):
            if index == len(nums):
                if current_or > self.max_or:
                    self.max_or = current_or
                    self.count = 1
                elif current_or == self.max_or:
                    self.count += 1
                return
            
            dfs(index + 1, current_or | nums[index])
            dfs(index + 1, current_or)

        self.max_or = 0
        self.count = 0
        dfs(0, 0)
        return self.count

solution = Solution()
nums = [3, 1]
print(solution.countMaxOrSubsets(nums))