from collections import Counter

class Solution(object):
    def canConstruct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        if k > len(s):
            return False
        
        char_counts = Counter(s)
        odd_count = sum(1 for count in char_counts.values() if count % 2 != 0)
        return odd_count <= k