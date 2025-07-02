from collections import Counter

class Solution(object):

    def maxDifference(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = Counter(s)
        max_diff = float('-inf')

        odd_freq = []
        even_freq = []

        for count in freq.values():
            if count % 2 == 0:
                even_freq.append(count)
            else:
                odd_freq.append(count)

        for odd in odd_freq:
            for even in even_freq:
                max_diff = max(max_diff, odd - even)
        return max_diff