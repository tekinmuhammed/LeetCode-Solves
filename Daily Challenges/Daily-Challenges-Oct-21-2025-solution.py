# 3346. Maximum Frequency of an Element After Performing Operations I

# **Difficulty:** Medium
# **Problem Link:** [LeetCode 3346](https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-i/description/)

# 🧠 Problem Description
# [Github LeetCode 3346. Maximum Frequency of an Element After Performing Operations I](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/3346.%20Maximum%20Frequency%20of%20an%20Element%20After%20Performing%20Operations%20I)

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        ans = 0
        num_count = {}
        last_num_index = 0
        for i in range(len(nums)):
            if nums[i] != nums[last_num_index]:
                num_count[nums[last_num_index]] = i - last_num_index
                ans = max(ans, i - last_num_index)
                last_num_index = i

        num_count[nums[last_num_index]] = len(nums) - last_num_index
        ans = max(ans, len(nums) - last_num_index)

        for i in range(nums[0], nums[-1] + 1):
            l = bisect.bisect_left(nums, i - k)
            r = bisect.bisect_right(nums, i + k) - 1
            if i in num_count:
                temp_ans = min(r - l + 1, num_count[i] + numOperations)
            else:
                temp_ans = min(r - l + 1, numOperations)
            ans = max(ans, temp_ans)

        return ans