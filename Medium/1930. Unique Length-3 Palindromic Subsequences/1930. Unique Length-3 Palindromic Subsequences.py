class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        unique_palindromes = set()
        for char in set(s):
            first_index = s.find(char)
            last_index = s.rfind(char)
            if last_index - first_index > 1:
                middle_characters = set(s[first_index + 1:last_index])
                for mid_char in middle_characters:
                    unique_palindromes.add(char + mid_char + char)
        return len(unique_palindromes)