# 3130. Find All Possible Stable Binary Arrays II

**Difficulty:** Hard  
**Problem Link:** [LeetCode 3130](https://leetcode.com/problems/find-all-possible-stable-binary-arrays-ii/description/)

---

## Problem Description

Given three positive integers `zero`, `one`, and `limit`, return the number of **stable** binary arrays that can be formed.

A binary array is **stable** if:
1. It contains exactly `zero` number of 0s.
2. It contains exactly `one` number of 1s.
3. Each **subsegment** of identical elements has a length of **at most** `limit`.

Since the answer may be very large, return it **modulo $10^9 + 7$**.

---

## Approach: Top-Down Dynamic Programming (Memoization)

This solution uses a recursive approach with memoization to solve the counting problem. The core logic relies on the **Inclusion-Exclusion Principle** to enforce the `limit` constraint.

### Key Ideas:
1.  **State Definition:** `dp(zero, one, lastBit)` returns the number of stable arrays that can be formed with the remaining `zero` and `one` counts, where the last bit placed was `lastBit`.
2.  **Transition Logic:**
    - To place a `0`, we consider all stable arrays from the state `(zero - 1, one)`.
    - **Subtracting Invalid Cases:** If the current number of zeros exceeds the `limit`, we must subtract the sequences that would have resulted in `limit + 1` consecutive zeros. This specifically happens if we add a `0` to a sequence that already ended with exactly `limit` zeros.
3.  **Base Cases:**
    - If `zero == 0` or `one == 0`, we check if the remaining count of the other digit exceeds the `limit`. If it does, no stable array can be formed from that path.
4.  **Memory Management:** Using `@cache` ensures that each state is calculated only once. `dp.cache_clear()` is used to free memory after the result is obtained.



---

## Code

```python
class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        mod = 10**9 + 7

        @cache
        def dp(zero, one, lastBit):
            # Base Case: No more zeros left
            if zero == 0:
                # If we just placed a 0 or we have too many ones left, it's invalid
                if lastBit == 0 or one > limit:
                    return 0
                else:
                    return 1
            
            # Base Case: No more ones left
            elif one == 0:
                # If we just placed a 1 or we have too many zeros left, it's invalid
                if lastBit == 1 or zero > limit:
                    return 0
                else:
                    return 1
            
            if lastBit == 0:
                # Number of ways ending in 0
                res = dp(zero - 1, one, 0) + dp(zero - 1, one, 1)
                # Inclusion-Exclusion: Subtract sequences that violate the limit
                if zero > limit:
                    res -= dp(zero - limit - 1, one, 1)
            else:
                # Number of ways ending in 1
                res = dp(zero, one - 1, 0) + dp(zero, one - 1, 1)
                # Inclusion-Exclusion: Subtract sequences that violate the limit
                if one > limit:
                    res -= dp(zero, one - limit - 1, 0)
            
            return res % mod

        # The result is the sum of arrays ending in 0 and arrays ending in 1
        res = (dp(zero, one, 0) + dp(zero, one, 1)) % mod
        dp.cache_clear()
        return res
```

---

## Example Walkthrough

**Input:** `zero = 3, one = 3, limit = 2`

1.  The algorithm starts by trying to place either a `0` or a `1`.
2.  In each step, it recursively calls `dp` with reduced counts.
3.  If it attempts to place more than 2 (the `limit`) zeros in a row, the subtraction `res -= dp(zero - limit - 1, one, 1)` effectively cancels out those invalid paths.
4.  The memoization table stores results for states like `(2, 3, 0)`, `(2, 3, 1)`, etc., to avoid redundant calculations.

---

## Complexity Analysis

* **Time Complexity:** $O(zero \times one)$
    - There are $zero \times one \times 2$ possible states in the memoization table. Each state is computed in $O(1)$ time.
* **Space Complexity:** $O(zero \times one)$
    - Due to the storage required for the memoization table (cache) and the recursion stack.

---

## Tags
Dynamic-Programming, Recursion, Memoization, Combinatorics, Hard-Logic