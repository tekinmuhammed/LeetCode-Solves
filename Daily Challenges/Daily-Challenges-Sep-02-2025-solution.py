# 3025. Find the Number of Ways to Place People I

# **Difficulty:** Medium
# **Link:** [LeetCode 3025](https://leetcode.com/problems/find-the-number-of-ways-to-place-people-i/)

# 🧠 Problem Description
# [Github LeetCode 3025. Find the Number of Ways to Place People I](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/3025.%20Find%20the%20Number%20of%20Ways%20to%20Place%20People%20I)

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        ans = 0
        n = len(points)

        for i in range(n):
            pointA = points[i]
            for j in range(n):
                pointB = points[j]
                if i == j or not (
                    pointA[0] <= pointB[0] and pointA[1] >= pointB[1]
                ):
                    continue
                if n == 2:
                    ans += 1
                    continue

                illegal = False
                for k in range(n):
                    if k == i or k == j:
                        continue

                    pointTmp = points[k]
                    isXContained = (
                        pointTmp[0] >= pointA[0] and pointTmp[0] <= pointB[0]
                    )
                    isYContained = (
                        pointTmp[1] <= pointA[1] and pointTmp[1] >= pointB[1]
                    )
                    if isXContained and isYContained:
                        illegal = True
                        break
                if not illegal:
                    ans += 1
        return ans