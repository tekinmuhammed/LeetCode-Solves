# 🧩 1292. Maximum Side Length of a Square with Sum to Threshold

# **Difficulty:** Medium  
# **Link:** [LeetCode 1292](https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/description/)  

# 🧠 Problem Description
# [Github LeetCode 1292. Maximum Side Length of a Square with Sum to Threshold](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/1292.%20Maximum%20Side%20Length%20of%20a%20Square%20with%20Sum%20Less%20than%20or%20Equal%20to%20Threshold)

class Solution(object):
    def maxSideLength(self, mat, threshold):
        m, n = len(mat), len(mat[0])

        # Prefix sum matrix
        ps = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                ps[i + 1][j + 1] = (
                    ps[i][j + 1]
                    + ps[i + 1][j]
                    - ps[i][j]
                    + mat[i][j]
                )

        def exists_square(k):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    total = (
                        ps[i + k][j + k]
                        - ps[i][j + k]
                        - ps[i + k][j]
                        + ps[i][j]
                    )
                    if total <= threshold:
                        return True
            return False

        left, right = 1, min(m, n)
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            if exists_square(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans