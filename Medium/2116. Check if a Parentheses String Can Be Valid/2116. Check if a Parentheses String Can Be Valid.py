class Solution(object):
    def canBeValid(self, s, locked):
        """
        :type s: str
        :type locked: str
        :rtype: bool
        """
        if len(s) % 2 != 0:
            return False

        open_count = 0
        for i in range(len(s)):
            if locked[i] == '0' or s[i] == '(':
                open_count += 1
            else:
                open_count -= 1
            if open_count < 0:
                return False
        close_count = 0
        for i in range(len(s) - 1, -1, -1):
            if locked[i] == '0' or s[i] == ')':
                close_count += 1
            else:
                close_count -= 1
            if close_count < 0:
                return False
        return True