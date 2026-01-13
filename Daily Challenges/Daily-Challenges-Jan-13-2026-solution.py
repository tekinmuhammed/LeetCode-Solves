# 3453. Separate Squares I

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 3443](https://leetcode.com/problems/separate-squares-i/description/)

# 🧠 Problem Description
# [Github LeetCode 3453. Separate Squares I](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/3453.%20Separate%20Squares%20I)

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        max_y, total_area = 0, 0
        for x, y, l in squares:
            total_area += l**2
            max_y = max(max_y, y + l)

        def check(limit_y):
            area = 0
            for x, y, l in squares:
                if y < limit_y:
                    area += l * min(limit_y - y, l)
            return area >= total_area / 2

        lo, hi = 0, max_y
        eps = 1e-5
        while abs(hi - lo) > eps:
            mid = (hi + lo) / 2
            if check(mid):
                hi = mid
            else:
                lo = mid

        return hi