# 1900. The Earliest and Latest Rounds Where Players Compete

# **Difficulty:** Hard  
# **Link:** [LeetCode 1900](https://leetcode.com/problems/the-earliest-and-latest-rounds-where-players-compete)

# 🧠 Problem Description 
# [Github LeetCode 1900. The Earliest and Latest Rounds Where Players Compete](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Hard/1900.%20The%20Earliest%20and%20Latest%20Rounds%20Where%20Players%20Compete)

class Solution:
    def earliestAndLatest(
        self, n: int, firstPlayer: int, secondPlayer: int
    ) -> List[int]:
        @cache
        def dp(n: int, f: int, s: int) -> (int, int):
            if f + s == n + 1:
                return (1, 1)

            if f + s > n + 1:
                return dp(n, n + 1 - s, n + 1 - f)

            earliest, latest = float("inf"), float("-inf")
            n_half = (n + 1) // 2

            if s <= n_half:
                for i in range(f):
                    for j in range(s - f):
                        x, y = dp(n_half, i + 1, i + j + 2)
                        earliest = min(earliest, x)
                        latest = max(latest, y)
            else:
                s_prime = n + 1 - s
                mid = (n - 2 * s_prime + 1) // 2
                for i in range(f):
                    for j in range(s_prime - f):
                        x, y = dp(n_half, i + 1, i + j + mid + 2)
                        earliest = min(earliest, x)
                        latest = max(latest, y)

            return (earliest + 1, latest + 1)

        if firstPlayer > secondPlayer:
            firstPlayer, secondPlayer = secondPlayer, firstPlayer

        earliest, latest = dp(n, firstPlayer, secondPlayer)
        dp.cache_clear()
        return [earliest, latest]