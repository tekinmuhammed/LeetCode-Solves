## 744. Find Smallest Letter Greater Than Target

# **Difficulty:** Easy  
# **Link:** [LeetCode 744](https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/)

# 🧠 Problem Description
# [Github LeetCode 744. Find Smallest Letter Greater Than Target](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/744.%20Find%20Smallest%20Letter%20Greater%20Than%20Target)

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