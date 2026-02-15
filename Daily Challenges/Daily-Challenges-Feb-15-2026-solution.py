# 67. Add Binary

# **Difficulty:** Easy  
# **Problem Link:** [LeetCode 67. Add Binary](https://leetcode.com/problems/add-binary/description/)

# 🧠 Problem Description
# [Github LeetCode 67. Add Binary](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/67.%20Add%20Binary)

class Solution(object):
    def addBinary(self, a, b):
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            total = carry

            if i >= 0:
                total += int(a[i])
                i -= 1

            if j >= 0:
                total += int(b[j])
                j -= 1

            result.append(str(total % 2))
            carry = total // 2

        return ''.join(reversed(result))