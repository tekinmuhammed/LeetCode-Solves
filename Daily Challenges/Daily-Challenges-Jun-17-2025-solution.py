# 3405. Count the Number of Arrays with K Matching Adjacent Elements

# **Difficulty:** Hard  
# **Problem Link:** [LeetCode 3405](https://leetcode.com/problems/count-the-number-of-arrays-with-k-matching-adjacent-elements/)

# 🧠 Problem Description 
# [Github LeetCode 3405. Count the Number of Arrays with K Matching Adjacent Elements](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Hard/3405.%20Count%20the%20Number%20of%20Arrays%20with%20K%20Matching%20Adjacent%20Elements)

MOD = 10**9 + 7
MX = 10**5

fact = [0] * MX
inv_fact = [0] * MX


def qpow(x, n):
    res = 1
    while n:
        if n & 1:
            res = res * x % MOD
        x = x * x % MOD
        n >>= 1
    return res


def init():
    if fact[0] != 0:
        return
    fact[0] = 1
    for i in range(1, MX):
        fact[i] = fact[i - 1] * i % MOD
    inv_fact[MX - 1] = qpow(fact[MX - 1], MOD - 2)
    for i in range(MX - 1, 0, -1):
        inv_fact[i - 1] = inv_fact[i] * i % MOD


def comb(n, m):
    return fact[n] * inv_fact[m] % MOD * inv_fact[n - m] % MOD


class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        init()
        return comb(n - 1, k) * m % MOD * qpow(m - 1, n - k - 1) % MOD