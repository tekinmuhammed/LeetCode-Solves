class Solution(object):
    def productQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        MOD = 10**9 + 7
        powers = []
        bit = 0

        while n > 0:
            if n & 1:
                powers.append(1 << bit)
            bit += 1
            n >>= 1

        result = []
        for left, right in queries:
            prod = 1
            for i in range(left, right + 1):
                prod = (prod * powers[i]) % MOD
            result.append(prod)
        return result