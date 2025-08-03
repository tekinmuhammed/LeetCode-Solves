# 2106. Maximum Fruits Harvested After at Most K Steps

**Difficulty:** Hard  
**Problem Link:** [LeetCode 2106](https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps)

---

## Problem Description

You are given a 2D list `fruits` where each `fruits[i] = [position_i, amount_i]`, representing `amount_i` fruits located at position `position_i` on an infinite number line.

You are also given an integer `startPos` indicating your starting position and an integer `k` for the **maximum number of steps** you can take (moving one unit left or right per step).

Return the **maximum total number of fruits** you can collect within at most `k` steps.

---

### Example

**Input:**
```python
fruits = [[2,4],[4,3],[10,2]]
startPos = 4
k = 6
```

**Output:**
```python
7
```

### Explanation:

You can walk to position 2 and pick 4 fruits, then return to position 4 to pick 3 fruits. Total steps = 2 (left) + 2 (right) = 4 steps ≤ 6.

### Approach

#### Key Idea:

Try **two traversal patterns:**

1. Move left `x` steps, then right `k - 2x` steps.

2. Move right `x` steps, then left `k - 2x` steps.

-  For each combination of steps, determine the `left` and `right` bounds of positions you can reach.

- Use prefix sums to efficiently compute total fruits in the reachable range.

#### Steps:

1. Build a **prefix sum** array `sum_` for fast range fruit queries.

2. Use binary search (`bisect_left`, `bisect_right`) to determine start/end indices for each range.

3. Try both traversal strategies for all valid `x` values from `0` to `k // 2`.

### Complexity

- **Time Complexity:** `O(N + logN × K)`, where `N` is the number of fruit locations.

- - Preprocessing prefix sums: O(N)

- - Each of up to K/2 iterations uses binary search: O(logN)

- **Space Complexity:** `O(N)`

- - For storing prefix sums and fruit positions

### Tags

`Prefix-Sum`, `Greedy`, `Sliding-Window`, `Binary-Search`, `Two-Pointers`

### Notes

- The trick of reversing the direction (left then right, right then left) ensures you consider **all valid paths** within `k` steps.

- This is an optimization problem with spatial constraints; using sorted positions and prefix sums is a powerful combo.