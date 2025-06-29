class Solution(object):
    def colorTheGrid(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7

        from itertools import product
        colors = [0, 1, 2]

        def is_valid(col):
            return all(col[i] != col[i + 1] for i in range(len(col) - 1))
        valid_cols = [col for col in product(colors, repeat=m) if is_valid(col)]

        neighbors = {}
        for col1 in valid_cols:
            neighbors[col1] = []
            for col2 in valid_cols:
                if all(a != b for a, b in zip(col1, col2)):
                    neighbors[col1].append(col2)
        dp = {col: 1 for col in valid_cols}

        for _ in range(n - 1):
            new_dp = {}
            for col in valid_cols:
                new_dp[col] = 0
                for prev in neighbors[col]:
                    new_dp[col] = (new_dp[col] + dp[prev]) % MOD
            dp = new_dp
        return sum(dp.values()) % MOD