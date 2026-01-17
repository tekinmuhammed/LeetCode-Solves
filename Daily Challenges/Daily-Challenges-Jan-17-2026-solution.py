# 🧩 3047. Find the Largest Area of Square Inside Two Rectangles

**Difficulty:** Medium
**Link:** [LeetCode 3047](https://leetcode.com/problems/find-the-largest-area-of-square-inside-two-rectangles/description/)

# 🧠 Problem Description
# [Github LeetCode 2975. Maximum Square Area by Removing Fences From a Field](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/2975.%20Maximum%20Square%20Area%20by%20Removing%20Fences%20From%20a%20Field)

class Solution:
    def largestSquareArea(
        self, bottomLeft: List[List[int]], topRight: List[List[int]]
    ) -> int:
        max_size = 0

        for (bottom_left_i, top_right_i), (
            bottom_left_j,
            top_right_j,
        ) in combinations(zip(bottomLeft, topRight), 2):
            w = min(top_right_i[0], top_right_j[0]) - max(
                bottom_left_i[0], bottom_left_j[0]
            )
            h = min(top_right_i[1], top_right_j[1]) - max(
                bottom_left_i[1], bottom_left_j[1]
            )

            max_size = max(max_size, min(w, h))

        return max_size * max_size