# 1900. The Earliest and Latest Rounds Where Players Compete

**Difficulty:** Hard  
**Link:** [LeetCode 1900](https://leetcode.com/problems/the-earliest-and-latest-rounds-where-players-compete)

---

## Problem Description

There are `n` players in a single-elimination tournament, numbered from `1` to `n`.  
In each round, players are paired in the order `[1 vs n], [2 vs n-1], ...`.

You are given two specific players: `firstPlayer` and `secondPlayer`.

Return a list of two integers:
- The **earliest** round number where they can compete.
- The **latest** round number where they can compete.

---

## Example

### Input
```python
n = 11
firstPlayer = 2
secondPlayer = 4
```

### Output
```python
[3, 4]
```

### Constraints
- `2 <= n <= 30`

- `1 <= firstPlayer < secondPlayer <= n`

### Approach & Explanation
This problem is best solved using **dynamic programming with memoization**, where we simulate all possible tournament matchups.

#### Key Ideas:

- Players are matched symmetrically: player `i` vs player `n - i + 1`

- The two players meet when their positions are symmetric in a round.

- Because pairings shift based on which players win, we need to simulate all valid permutations recursively.

#### Steps:

1. Define `dp(n, f, s)` as the minimum and maximum round in which player `f` can meet player `s` among `n` players.

2. If `f + s == n + 1`, they meet directly in the current round.

3. Otherwise, simulate all match outcomes and recursively track when `f` and `s` could meet in reduced rounds.

4. Memoize the results using `@cache` to avoid recomputation.

5. Normalize `(f, s)` so that `f < s.`

### Time and Space Complexity

- **Time Complexity:**
Exponential in the worst case due to recursive simulation.
But limited by small `n` (`n ≤ 30`) and memoization, so practically fast.

- **Space Complexity:**
`O(n²)` for memoization cache.

### Tags
`Dynamic-Programming`, `Recursion`, `Memoization`, `Game-Simulation`

### Summary

This problem is a clever combination of **game tree simulation** and **memoization**.
Instead of brute-forcing all player matchups, we simulate only valid states and cache results.
A classic recursive DP trick in competitive programming.