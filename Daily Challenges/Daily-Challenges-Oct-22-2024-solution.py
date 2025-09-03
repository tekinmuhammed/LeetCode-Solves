# LeetCode 1593. Split a String Into the Max Number of Unique Substrings

# 🔗 Problem Link
#[LeetCode 1593. Split a String Into the Max Number of Unique Substrings](https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings)

# 🧠 Problem Description
#[Github LeetCode 1593. Split a String Into the Max Number of Unique Substrings](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/1593.%20Split%20a%20String%20Into%20the%20Max%20Number%20of%20Unique%20Substrings)

class Solution(object):
    def maxUniqueSplit(self, s):
        def backtrack(start, seen):
            if start == len(s):
                return len(seen)
            max_split = 0
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if substring not in seen:
                    seen.add(substring)
                    max_split = max(max_split, backtrack(end, seen))
                    seen.remove(substring)
            return max_split
        return backtrack(0, set())

s = "ababccc"

solution = Solution()
result = solution.maxUniqueSplit(s)

print(result)