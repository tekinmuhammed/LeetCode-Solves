# 1855. Maximum Distance Between a Pair of Values

**Difficulty:** Medium  
**Problem Link:** [LeetCode 1855](https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/description/

# 🧠 Problem Description
# [Github LeetCode 3783. Mirror Distance of an Integer](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/3783.%20Mirror%20Distance%20of%20an%20Integer) 

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i=0
        j=0
        mat=0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<=nums2[j]:
                mat=max(mat,abs(j-i))
                j+=1
            else:
                i+=1
            if j<i:
                j=i
        return mat