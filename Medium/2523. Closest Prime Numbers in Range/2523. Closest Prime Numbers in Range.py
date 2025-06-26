class Solution(object):
    def closestPrimes(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        MAX_N = 10**6
        is_prime = [True] * (MAX_N + 1)
        is_prime [0] = is_prime[1] = False
        for i in range(2, int(MAX_N ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, MAX_N + 1, i):
                    is_prime[j] = False
        primes = [num for num in range(left, right + 1) if is_prime[num]]
        if len(primes) < 2:
            return [ -1, -1]
        min_diff = float('inf')
        result = [-1, -1]
        for i in range(len(primes) - 1):
            diff = primes[i + 1] - primes[i]
            if diff < min_diff:
                min_diff = diff
                result = [primes[i], primes[i + 1]]
        return result