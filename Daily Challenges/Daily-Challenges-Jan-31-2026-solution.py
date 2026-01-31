## 744. Find Smallest Letter Greater Than Target

# **Difficulty:** Easy  
# **Link:** [LeetCode 744](https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/)

# 🧠 Problem Description
# [Github LeetCode 2977. Minimum Cost to Convert String II](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Hard/2977.%20Minimum%20Cost%20to%20Convert%20String%20II)
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        left, right = 0, len(letters) - 1

        while left <= right:
            mid = (left + right) // 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

        # wrap-around case
        return letters[left] if left < len(letters) else letters[0]