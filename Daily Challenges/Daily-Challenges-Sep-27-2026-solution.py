# 1190. Reverse Substrings Between Each Pair of Parentheses 

# **Difficulty:** Medium
# **Problem Link:** [LeetCode 1190](https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/description/)

# 🧠 Problem Description 
# [Github LeetCode 1190. Reverse Substrings Between Each Pair of Parentheses](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/1190.%20Reverse%20Substrings%20Between%20Each%20Pair%20of%20Parentheses)

class Solution:
    def reverseParentheses(self, s: str) -> str:
        open_parentheses_indices = deque()
        result = []

        for current_char in s:
            if current_char == "(":
                # Store the current length as the start index 
                # for future reversal 
                open_parentheses_indices.append(len(result))
            elif current_char == ")":
                start = open_parentheses_indices.pop()
                # Reverse the substring between the matching parentheses 
                result[start:] = result[start:][::-1]
            else:
                # Append non-parenthesis characters to the processed list 
                result.append(current_char)
        return "".join(result)