# 1415. The k-th Lexicographical String of All Happy Strings of Length n

**Difficulty:** Medium
**Problem Link:** [LeetCode 1415](https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/description/)
 
# 🧠 Problem Description
# [Github LeetCode 3296. Minimum Number of Seconds to Make Mountain Height Zero](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/1415.%20The%20k-th%20Lexicographical%20String%20of%20All%20Happy%20Strings%20of%20Length%20n)

class Solution(object):
    def getHappyString(self, n, k):
        res = []

        def dfs(path):
            if len(res) >= k:
                return
            if len(path) == n:
                res.append(path)
                return

            for c in ['a', 'b', 'c']:
                if not path or path[-1] != c:
                    dfs(path + c)

        dfs("")
        
        if len(res) < k:
            return ""
        return res[k-1]