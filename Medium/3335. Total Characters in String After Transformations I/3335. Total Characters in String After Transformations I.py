class Solution(object):
    def lengthAfterTransformations(self, s, t):
        """
        :type s: str
        :type t: int
        :rtype: int
        """
        MOD = 10**9 + 7
        dp = [0] * 26
        for i in range(26):
            dp[i] = 1
        for _ in range(t):
            new_dp = [0] * 26
            for i in range(26):
                if i == 25:
                    new_dp[i] = (dp[0] + dp[1]) % MOD
                else:
                    new_dp[i] = dp[i + 1]
            dp = new_dp
        total = 0
        for ch in s:
            idx = ord(ch) - ord('a')
            total = (total + dp[idx]) % MOD
        return total