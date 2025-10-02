# 2040. Kth Smallest Product of Two Sorted Arrays

# **Difficulty:** Hard  
# **Link:** [LeetCode 2040](https://leetcode.com/problems/kth-smallest-product-of-two-sorted-arrays)

# 🧠 Problem Description 
# [Github 2040. Kth Smallest Product of Two Sorted Arrays](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Hard/2040.%20Kth%20Smallest%20Product%20of%20Two%20Sorted%20Arrays)

class Solution:
    def f(self, nums2: List[int], x1: int, v: int) -> int:
        if x1 > 0:
            return bisect_right(nums2, v // x1)
        elif x1 < 0:
            return len(nums2) - bisect_left(nums2, -(-v // x1))
        else:
            return len(nums2) if v >= 0 else 0

    def kthSmallestProduct(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> int:
        n1 = len(nums1)
        left, right = -(10**10), 10**10
        while left <= right:
            mid = (left + right) // 2
            count = 0
            for i in range(n1):
                count += self.f(nums2, nums1[i], mid)
            if count < k:
                left = mid + 1
            else:
                right = mid - 1
        return left