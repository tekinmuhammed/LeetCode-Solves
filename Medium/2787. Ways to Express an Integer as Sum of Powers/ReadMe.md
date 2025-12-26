# 2787. Ways to Express an Integer as Sum of Powers

**Difficulty:** Medium  
**Link:** [LeetCode 2787](https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-pairs/)

---

## Problem Description
Given two integers `n` and `x`, find the number of ways to express `n` as the sum of **unique integers** each raised to the power `x`.  
Since the answer can be very large, return it modulo `10^9 + 7`.

**Example:**
```python
Input: n = 10, x = 2
Output: 1
Explanation: 10 = 1² + 3²
```

## Approach
1. **Generate all possible powers**:  
   Create a list of all integers `i` such that `i^x <= n`.
   
2. **Dynamic Programming (Subset Sum)**:  
   - Use a DP array `dp[s]` where `dp[s]` represents the number of ways to form sum `s` using unique powers.
   - Initialize `dp[0] = 1` (one way to form sum 0: select nothing).
   - For each power, update `dp` in reverse order to avoid reusing the same power multiple times.

3. **Modulo Operation**:  
   Since the result can be large, take modulo `10^9 + 7` at every step.

**Time Complexity:**  
- Power generation: `O(n^(1/x))`  
- DP update: `O(n * number_of_powers)`

**Space Complexity:** `O(n)`