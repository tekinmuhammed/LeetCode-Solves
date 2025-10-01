# 2138. Divide a String Into Groups of Size k

# **Difficulty:** Easy  
# **Problem Link:** [LeetCode 2138](https://leetcode.com/problems/divide-a-string-into-groups-of-size-k)

# 🧠 Problem Description 
# [Github LeetCode 2138. Divide a String Into Groups of Size k](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/2138.%20Divide%20a%20String%20Into%20Groups%20of%20Size%20k)

class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        res = []
        i = 0
        while i < len(s):
            group = s[i:i+k]
            if len(group) < k:
                group += fill * (k - len(group))
            res.append(group)
            i += k
        return res