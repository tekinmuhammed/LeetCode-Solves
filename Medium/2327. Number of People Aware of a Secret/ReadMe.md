# 2327. Number of People Aware of a Secret

**Difficulty:** Medium  
**Link:** [LeetCode 2327](https://leetcode.com/problems/number-of-people-aware-of-a-secret/)

---

## Problem Description
On day 1, one person discovers a secret.  

- Each person can share the secret with others starting from **`delay`** days after they learn it.  
- Each person forgets the secret exactly **`forget`** days after they learn it.  

Given integers `n`, `delay`, and `forget`, return the number of people who still know the secret at the end of day `n`.  

The answer must be returned **modulo 10^9 + 7**.

---

## Example 1
**Input:**
```python
n = 6, delay = 2, forget = 4
```

**Output:**
```python
5
```

**Explanation:**
- Day 1: person A learns the secret.  
- Day 2: person A cannot share yet.  
- Day 3: person A starts sharing.  
- Day 4: person A shares with B, and so on.  
- By the end of day 6, 5 people still know the secret.  

---

## Example 2
**Input:**
```python
n = 4, delay = 1, forget = 3
```

**Output:**
```python
6
```

---

## Constraints
- `2 <= n <= 1000`
- `1 <= delay < forget <= n`

---

## Approach

### Key Idea
- Use **dynamic programming (DP)**:
  - `dp[i]` = number of people who learn the secret on day `i`.  
  - For each `day`, these people contribute to future days between `[day + delay, day + forget)`.  
  - Add their contribution to `dp[share]`.  

- At the end, sum up `dp` values from days `[n - forget + 1, n]`, because only these people still remember the secret.

### Algorithm
1. Initialize an array `dp` of size `n+1`.
2. Set `dp[1] = 1` (first person learns the secret).  
3. For each `day` in `1..n`:
   - For each `share` in `[day+delay, min(day+forget, n)]`:
     - Update `dp[share] += dp[day] (mod 10^9+7)`.  
4. Compute the sum of `dp[day]` for `day` in `[n-forget+1, n]`.  

---

## Time and Space Complexity
- **Time Complexity:** O(n * forget) in the worst case.  
- **Space Complexity:** O(n) due to the DP array.  

---

## Tags
Dynamic Programming, Simulation, Modulo Arithmetic

---

## Notes
- This is a **simulation-based DP** solution.  
- Optimizations exist (prefix sums to reduce inner loop), but the given approach is simpler and sufficient for the constraints.  