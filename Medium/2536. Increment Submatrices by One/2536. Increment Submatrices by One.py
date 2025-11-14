class Solution(object):
    def rangeAddQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[List[int]]
        """

        # 2D difference matrix
        diff = [[0] * (n + 1) for _ in range(n + 1)]

        # Apply difference updates
        for r1, c1, r2, c2 in queries:
            diff[r1][c1] += 1
            diff[r1][c2 + 1] -= 1
            diff[r2 + 1][c1] -= 1
            diff[r2 + 1][c2 + 1] += 1

        # Build the actual matrix using prefix sums
        result = [[0] * n for _ in range(n)]

        for r in range(n):
            for c in range(n):
                above = result[r - 1][c] if r > 0 else 0
                left = result[r][c - 1] if c > 0 else 0
                diag = result[r - 1][c - 1] if r > 0 and c > 0 else 0

                result[r][c] = diff[r][c] + above + left - diag

        return result