class Solution(object):
    def concatenatedBinary(self, n):
        MOD = 10**9 + 7
        result = 0
        bit_length = 0

        for i in range(1, n + 1):
            # i power of two ise bit sayısı artar
            if i & (i - 1) == 0:
                bit_length += 1

            result = ((result << bit_length) | i) % MOD

        return result