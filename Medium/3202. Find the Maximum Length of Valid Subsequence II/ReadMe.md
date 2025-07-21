# 3202. Find the Maximum Length of Valid Subsequence II

**Difficulty:** Medium  
**Link:** [LeetCode 3202](https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii)

---

## Problem Description

Given an integer array `nums` and an integer `k`, return the **maximum length** of a valid subsequence such that:

- The absolute difference between adjacent elements in the subsequence is divisible by `k`.

Formally, for a subsequence `[a₁, a₂, ..., aₙ]`, it is valid if:
∀ i ∈ [1, n-1], (aᵢ - aᵢ₊₁) % k == 0

---

## Example

### Input
```python
nums = [3, 6, 9, 12]
k = 3
```

### Output
`4`

### Explanation

Every adjacent difference is divisible by 3, so the full array is a valid subsequence.

### Approach & Explanation

We use **Dynamic Programming with a 2D DP table:**

- Let `dp[i][j]` be the length of the longest valid subsequence where the last modulo-`k` values are `i` and `j`.

- Iterate through the `nums` array, and for each number:

- - Reduce it modulo `k`: `num % k`.

- - For each previous modulo prev, update the dp state:
```python
dp[prev][num] = dp[num][prev] + 1
```

- - This swaps the roles of `prev` and `num`, ensuring alternating modulo differences are tracked.

The result is the **maximum** of all such lengths in the DP table.

### Time and Space Complexity

- **Time Complexity:** `O(n × k)`

- → For each number, we iterate over all k previous states.

- **Space Complexity:** `O(k²)`

- → We use a k×k DP matrix.

### Tags
`Dynamic-Programming`, `Modulo-Arithmetic`, `Subsequence`, `Matrix-DP`

### Summary

Bu problem, modüler aritmetiği ve iki boyutlu DP'yi harmanlayarak, geçerli artış düzenine sahip en uzun alt diziyi bulmayı amaçlar.
Yaratıcı bir DP durumu ile klasik subsequence sorularına güzel bir varyasyon sunar.