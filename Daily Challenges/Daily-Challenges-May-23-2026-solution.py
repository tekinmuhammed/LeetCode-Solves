# 1752. Check if Array Is Sorted and Rotated

# **Difficulty:** Easy
# **Problem Link:** [LeetCode 1752](https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/)

# 🧠 Problem Description
# [Github LeetCode 1752. Check if Array Is Sorted and Rotated](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/1752.%20Check%20if%20Array%20Is%20Sorted%20and%20Rotated-2) 

class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)

        # Iterate through all possible rotation offsets
        for rotation_offset in range(n):
            check_sorted = []

            # Create the rotated array
            for index in range(rotation_offset, n):
                check_sorted.append(nums[index])
            for index in range(rotation_offset):
                check_sorted.append(nums[index])

            # Check if the constructed array is sorted
            is_sorted = True
            for index in range(n - 1):
                if check_sorted[index] > check_sorted[index + 1]:
                    is_sorted = False
                    break

            # If sorted, return true
            if is_sorted:
                return True

        # If no rotation makes the array sorted, return false
        return False