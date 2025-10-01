# 1432. Max Difference You Can Get From Changing an Integer

# **Link:** [LeetCode 1432](https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/)  
# **Difficulty:** Medium

# 🧠 Problem Description 
# [Github  LeetCode 1432. Max Difference You Can Get From Changing an Integer](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/1432.%20Max%20Difference%20You%20Can%20Get%20From%20Changing%20an%20Integer)

class Solution(object):
    def maxDiff(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = str(num)

        for ch in s:
            if ch != '9':
                a = int(s.replace(ch, '9'))
                break
        else:
            a = num

        first = s[0]
        if first != '1':
            b = int(s.replace(first, '1'))
        else:
            found = False
            b_s = s
            for i in range(1, len(s)):
                if s[i] != '0' and s[i] != '1':
                    b_s = s.replace(s[i], '0')
                    found = True
                    break
            b = int(b_s)
        return a - b