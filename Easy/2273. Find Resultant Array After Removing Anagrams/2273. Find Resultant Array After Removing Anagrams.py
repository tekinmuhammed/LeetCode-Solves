class Solution(object):
    def removeAnagrams(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result = [words[0]]
        
        for i in range(1, len(words)):
            # Eğer mevcut kelime öncekiyle anagram değilse ekle
            if sorted(words[i]) != sorted(result[-1]):
                result.append(words[i])
        
        return result