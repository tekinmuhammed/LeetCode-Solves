# 2913. Subarrays Distinct Element Sum of Squares I

# **Difficulty:** Easy 
# **Problem Link:** [LeetCode 2913](https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/description/)

# 🧠 Problem Description 
# [Github LeetCode 2913. Subarrays Distinct Element Sum of Squares I](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/2913.%20Subarrays%20Distinct%20Element%20Sum%20of%20Squares%20I)

class BIT:
    def __init__(self, n: int):
        self.size = n
        self._tree1 = defaultdict(int)
        self._tree2 = defaultdict(int)

    def _lowbit(self, index: int) -> int:
        return index & -index

    def add(self, left: int, right: int, delta: int) -> None:
        self._add(left, delta)
        self._add(right + 1, -delta)

    def query(self, left: int, right: int) -> int:
        return self._query(right) - self._query(left - 1)

    def _add(self, index: int, delta: int) -> None:
        index += 1
        if index < 0:
            raise ValueError("index must be a positive integer")

        rawIndex = index
        while index <= self.size:
            self._tree1[index] += delta
            self._tree2[index] += (rawIndex - 1) * delta
            index += self._lowbit(index)

    def _query(self, index: int) -> int:
        index += 1
        if index > self.size:
            index = self.size

        rawIndex = index
        res = 0
        while index > 0:
            res += rawIndex * self._tree1[index] - self._tree2[index]
            index -= self._lowbit(index)
        return res


class Solution:
    def sumCounts(self, A: List[int]) -> int:
        n = len(A)
        res = cur = 0
        bit = BIT(n + 10)
        seen = {}
        mod = 10**9 + 7
        for i, a in enumerate(A):
            j = seen.get(a, -1) + 1
            cur += bit.query(j, i) * 2 + i - j + 1
            res += cur
            bit.add(j, i, 1)
            seen[a] = i
        return res % mod