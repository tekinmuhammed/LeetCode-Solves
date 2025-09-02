# LeetCode 2044 - Count Number of Maximum Bitwise-OR Subsets

# 🔗 Problem Link
#[LeetCode 2044 - Count Number of Maximum Bitwise-OR Subsets](https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/)

# 🧠 Problem Description 
#[Github LeetCode 2044](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/2044.%20Count%20Number%20of%20Maximum%20Bitwise-OR%20Subsets)

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