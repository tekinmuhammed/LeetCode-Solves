# 🧙‍♂️ 3539. Find Sum of Array Product of Magical Sequences

# **Difficulty:** Hard
# **Link:** [LeetCode 3539](https://leetcode.com/problems/find-sum-of-array-product-of-magical-sequences/description)

# 🧠 Problem Description
# [Github LeetCode 3539. Find Sum of Array Product of Magical Sequences](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Hard/3539.%20Find%20Sum%20of%20Array%20Product%20of%20Magical%20Sequences)

import functools
import math

class Solution:
    def magicalSum(self, m: int, k: int, nums: list[int]) -> int:
        MOD = 1_000_000_007
        N = len(nums)
        def mod_pow(base, exp):
            res = 1
            base %= MOD
            while exp > 0:
                if exp % 2 == 1:
                    res = (res * base) % MOD
                base = (base * base) % MOD
                exp //= 2
            return res
        MAX_M = 30
        comb = [[0] * (MAX_M + 1) for _ in range(MAX_M + 1)]
        for i in range(MAX_M + 1):
            comb[i][0] = 1
            for j in range(1, i + 1):
                comb[i][j] = (comb[i - 1][j - 1] + comb[i - 1][j]) % MOD
        @functools.lru_cache(None)
        def dp(i: int, j: int, carry: int) -> dict[int, int]:
            if i == N:
                if j == 0:
                    final_set_bits = carry.bit_count()
                    return {final_set_bits: 1}
                else:
                    return {}

            results = {} 
            for c in range(j + 1): 
                S = c + carry
                bit_val = S % 2      
                next_carry = S // 2  
                j_prime = j - c
                comb_term = comb[j][c]
                pow_term = mod_pow(nums[i], c)
                
                contribution_mult = (comb_term * pow_term) % MOD
                next_results = dp(i + 1, j_prime, next_carry)
                
                for k_prime_next, product_sum_next in next_results.items():
                    k_prime_current = k_prime_next + bit_val
                    
                    if k_prime_current not in results:
                        results[k_prime_current] = 0
                    new_sum = (contribution_mult * product_sum_next) % MOD
                    results[k_prime_current] = (results[k_prime_current] + new_sum) % MOD

            return results
        final_results = dp(0, m, 0)
        return final_results.get(k, 0)