class Solution(object):
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        """
        :type words: List[str]
        :type groups: List[int]
        :rtype: List[str]
        """
        def hammingValid(word1, word2):
            if len(word1) != len(word2):
                return False
            diff = 0
            for w1, w2 in zip(word1, word2):
                if w1!=w2:
                    diff+=1
            return diff ==1

        n = len(words)
        dp = [1] * n
        parent = [-1] * n

        for i in range(1, n):
            for j in range(i):
                if hammingValid(words[i], words[j]) and dp[j]+1 > dp[i] and groups[i] != groups[j]:
                    dp[i] = dp[j] + 1
                    parent[i] = j
            
        idx = dp.index(max(dp))

        res = []

        while idx != -1:
            res.append(words[idx])
            idx = parent[idx]
        res.reverse()

        return res