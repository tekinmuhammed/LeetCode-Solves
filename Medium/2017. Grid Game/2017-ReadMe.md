# 🎮 LeetCode 2017 - Grid Game

**Difficulty:** Medium  
**Problem Link:** [LeetCode 2017](https://leetcode.com/problems/grid-game/)

---

## 📘 Problem Description

You are given a 2-row grid (`grid[2][n]`). Two robots play a game:

- The **first robot** starts at cell (0, 0) and moves right until the end of the first row, then down to the second row and moves left to (1, 0), collecting points.
- The **second robot** can choose **any column `i`** to switch from the first to the second row, and wants to **minimize** the first robot’s maximum score **after** this switch.

Your task: **Find the minimum possible score the second robot can guarantee** (i.e., the *maximum score* that the first robot can be forced to collect, minimized over all possible switches).

---

## 🧪 Example

### Input:
```python
grid = [[2,5,4],
        [1,5,1]]
```

### Output:

`4`

### Explanation:

- If second robot switches after column `i = 1`, robot 1 collects:

- - top row (col 2): 4

- - bottom row (col 0): 1

- - max = 4 → minimized

## 🧠 Approach & Intuition

1. Precompute **prefix sums** for both rows:

- `top_prefix[i]`: total sum from `grid[0][0]` to `grid[0][i]`

- `bottom_prefix[i]`: total sum from `grid[1][0]` to `grid[1][i]`

2. Iterate over every column `i` as a possible switch point:

- Robot 1 will collect:

- - Remaining of top row: `top_prefix[-1] - top_prefix[i]`

- - Passed bottom row: `bottom_prefix[i - 1]` (if `i > 0`)

- Take the **max** of these two values — this is the worst-case score Robot 1 gets.

3. Minimize the worst-case across all `i`.

### ⏱️ Complexity

- **Time Complexity:** `O(n)`

- **Space Complexity:** `O(n)`

### 🏷️ Tags
`greedy`, `prefix-sum`, `min-max`, `grid`

### ✅ Key Insight
The second robot can **strategically switch** at the point that **minimizes the maximum gain** the first robot can obtain from either remaining path. This is a classic **minimax strategy**.