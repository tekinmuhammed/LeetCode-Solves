class Solution(object):
    def longestPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        from collections import Counter

        count = Counter(words)
        length = 0
        central_used = False

        for word in count:
            rev = word[::-1]
            if word == rev:
                pairs = count[word] // 2
                length += pairs * 4
                if count[word] % 2 == 1 and not central_used:
                    length += 2
                    central_used = True
            else:
                if rev in count:
                    pair_count = min(count[word], count[rev])
                    length += pair_count * 4
                    count[word] = 0
                    count[rev] = 0
        return length