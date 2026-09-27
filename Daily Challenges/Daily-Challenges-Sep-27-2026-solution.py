
# 🧠 Problem Description
# [Github LeetCode 1807. Evaluate the Bracket Pairs of a String](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/1807.%20Evaluate%20the%20Bracket%20Pairs%20of%20a%20String)
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