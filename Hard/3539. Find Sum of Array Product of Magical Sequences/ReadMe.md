# 🧙‍♂️ 3539. Find Sum of Array Product of Magical Sequences

**Difficulty:** Hard  
**Link:** [LeetCode 3539](https://leetcode.com/problems/find-sum-of-array-product-of-magical-sequences/description)

## 🧩 Problem Description  
You are given three integers `m`, `k`, and an array `nums`. You need to compute the **sum of all possible magical sequence products** under specific selection and bitwise constraints.  
A *magical sequence* is formed by choosing `m` elements (with repetition allowed) from the array `nums` such that the number of *set bits* in the total sum equals `k`.  
The answer should be returned **modulo 1,000,000,007**.

---

## 💡 Intuition  
This problem combines **dynamic programming**, **modular arithmetic**, and **combinatorial mathematics**.  

We simulate the process of selecting elements `m` times, keeping track of how many bits are set in the resulting binary sum.  
At each position (corresponding to a power of 2 from the numbers), we consider how many times a particular number is used (`c` times), and how this affects the current bit and the carry-over to higher bits.

Key ideas:
- Precompute **binomial coefficients** (`comb[m][c]`) for efficiency.  
- Use **modular exponentiation** to handle large powers.  
- Apply **memoized DP** (`lru_cache`) to store intermediate states defined by `(i, j, carry)`.  
- Each DP state returns a dictionary mapping “number of set bits” → “sum of sequence products”.  
- Finally, extract the total for the target bit count `k`.

---

## 🧮 Approach  
1. **Precompute combinations (`C(m, c)`)** using Pascal’s triangle up to `m = 30`.  
2. **Implement modular exponentiation (`mod_pow`)** to compute `nums[i]^c % MOD`.  
3. **Use recursive DP** with memoization:
   - `dp(i, j, carry)` returns a dictionary `{set_bits: total_product_sum}`.  
   - For each number, try all possible counts `c ∈ [0, j]`.  
   - Update carry and accumulate bit counts dynamically.  
4. **Combine recursive results** and compute the final modulo result.  

---

## 🧠 Example  
```python
Input:
m = 3
k = 2
nums = [1, 2, 3]

Output:
<computed result>
```

- Here, we evaluate all possible ways to pick 3 numbers (with repetition) such that the sum of their powers produces exactly 2 set bits in binary form. The total sum of all valid products (mod 1e9+7) is returned.

### 🧰 Code Implementation

```python
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
```

### 📊 Complexity Analysis

- **Time Complexity:** `O(N * m^2)` (due to nested loops and recursive branching)
- **Space Complexity:** `O(N * m^2)` (from DP memoization and dictionaries)

### 🧷 Tags
`Dynamic-Programming` · `Combinatorics` · `Bit-Manipulation` · `Modular-Arithmetic` · `Memoization`