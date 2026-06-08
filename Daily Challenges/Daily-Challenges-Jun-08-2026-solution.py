
# 🧠 Problem Description  
# [Github LeetCode 2574. Left and Right Sum Differences](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/2574.%20Left%20and%20Right%20Sum%20Differences) 
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        equal = []
        greater = []

        for num in nums:
            if num < pivot:
                less.append(num)
            elif num > pivot:
                greater.append(num)
            else:
                equal.append(num)

        less.extend(equal)
        less.extend(greater)

        return less