class Solution(object):
    def canMakeSubsequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: bool
        """
        n, m = len(str1), len(str2)
        j = 0
        for i in range(n):
            if str1[i] == str2[j] or (chr(ord(str1[i]) + 1) if str1[i] != 'z' else 'a') == str2[j]:
                j += 1
            if j == m:
                return True
        return False
        