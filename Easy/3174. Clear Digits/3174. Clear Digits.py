class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for char in s:
            if char.isdigit():
                if stack and stack[-1].isalpha():
                    stack.pop()
            else:
                stack.append(char)
        return "".join(stack)