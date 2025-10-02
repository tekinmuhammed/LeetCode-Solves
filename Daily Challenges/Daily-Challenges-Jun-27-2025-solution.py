# 2014. Longest Subsequence Repeated k Times

# **Difficulty:** Hard  
# **Link:** [LeetCode 2014](https://leetcode.com/problems/longest-subsequence-repeated-k-times/)

# 🧠 Problem Description 
# [Github LeetCode 2014. Longest Subsequence Repeated k Times](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Hard/2014.%20Longest%20Subsequence%20Repeated%20k%20Times)

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        def isK(sub: str, t: str, k: int) -> bool:
            count = i = 0
            for ch in t:
                if i < len(sub) and ch == sub[i]:
                    i += 1
                    if i == len(sub):
                        i = 0
                        count += 1
                        if count == k:
                            return True
            return False

        res = ""
        q = deque([""])
        while q:
            curr = q.popleft()
            for ch in map(chr, range(ord('a'), ord('z') + 1)):
                nxt = curr + ch
                if isK(nxt, s, k):
                    res = nxt
                    q.append(nxt)
        return res