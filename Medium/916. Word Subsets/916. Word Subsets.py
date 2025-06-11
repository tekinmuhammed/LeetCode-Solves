from collections import Counter

class Solution(object):
    def wordSubsets(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: List[str]
        """
        combined_counter = Counter()
        for word in words2:
            word_counter = Counter(word)
            for char, count in word_counter.items():
                combined_counter[char] = max(combined_counter[char], count)
        result = []
        for word in words1:
            word_counter = Counter(word)
            if all(word_counter[char] >= combined_counter[char] for char in combined_counter):
                result.append(word)
        return result