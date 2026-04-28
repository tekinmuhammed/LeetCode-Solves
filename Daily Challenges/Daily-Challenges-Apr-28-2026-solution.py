# 2033. Minimum Operations to Make a Uni-Value Grid

# **Difficulty:** Medium 
# **Problem Link:** [LeetCode 2033](https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/description/)

# 🧠 Problem Description
# [Github LeetCode 2033. Minimum Operations to Make a Uni-Value Grid ](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/2033.%20Minimum%20Operations%20to%20Make%20a%20Uni-Value%20Grid) 

class Solution:
    def minOperations(self, grid, x):
        # Create a list to store all the numbers from the grid
        nums_array = []
        result = 0

        # Flatten the grid into nums_array
        for row in grid:
            for num in row:
                nums_array.append(num)

        # Sort nums_array in non-decreasing order to easily find the median
        nums_array.sort()

        length = len(nums_array)
        # Store the median element as the final common value
        final_common_number = nums_array[length // 2]

        # Iterate through each number in nums_array
        for number in nums_array:
            # If the remainder when divided by x is different, return -1
            if number % x != final_common_number % x:
                return -1
            # Add the number of operations required to make the current number equal to final_common_number
            result += abs(final_common_number - number) // x

        return result