class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        N, res, current_num = len(s), s.count('0'), 0
        for i in range(N):
            if s[N - 1 - i] == '1':
                current_num |= 1 << i
                if current_num > k: break
                res += 1
        return res