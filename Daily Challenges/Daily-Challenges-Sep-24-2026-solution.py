# 3550. Smallest Index With Digit Sum Equal to Index

# **Difficulty:** Easy
# **Problem Link:** [LeetCode 3550](https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/description/)

# 🧠 Problem Description
# [Github LeetCode 3550. Smallest Index With Digit Sum Equal to Index](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/3550.%20Smallest%20Index%20With%20Digit%20Sum%20Equal%20to%20Index)

class Solution:
    def smallestIndex(self, nums: list[int]) -> int:
        def get_digit_sum(num: int) -> int:
            total = 0

            while num:
                num, digit = divmod(num, 10)
                total += digit

            return total

        for i, num in enumerate(nums):
            if get_digit_sum(num) == i:
                return i

        return -1