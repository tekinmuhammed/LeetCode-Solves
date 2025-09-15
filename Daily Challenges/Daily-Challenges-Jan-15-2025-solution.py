# 🔁 LeetCode 2657 - Find the Prefix Common Array of Two Arrays

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 2657](https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/)

# 🧠 Problem Description 
# [Github LeetCode 2657 - Find the Prefix Common Array of Two Arrays](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/2657.%20Find%20the%20Prefix%20Common%20Array%20of%20Two%20Arrays)

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        prefix_common = []
        seen = set()
        count = 0
        for i in range(n):
            if A[i] in seen:
                count += 1
            else:
                seen.add(A[i])
            if B[i] in seen:
                count += 1
            else:
                seen.add(B[i])
            prefix_common.append(count)
        return prefix_common