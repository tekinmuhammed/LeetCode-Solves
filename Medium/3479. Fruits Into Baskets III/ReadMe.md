# 3479. Fruits Into Baskets III

**Difficulty:** Medium  
**Problem Link:** [LeetCode 3479](https://leetcode.com/problems/fruits-into-baskets-iii)

---

## Problem Description

You are given two arrays:
- `fruits[i]`: the size of the `i-th` fruit.
- `baskets[j]`: the capacity of the `j-th` basket.

Each basket can hold **at most one fruit**, and each fruit must be placed into a **single unused basket** whose capacity is **greater than or equal to** the fruit’s size.

Your task is to **minimize the number of unplaced fruits**, and **optimize the placement** as efficiently as possible.

---

## Constraints

- The number of baskets `n` can be large (up to 10⁵).
- The naive approach of checking all baskets for each fruit will time out.

---

## Optimized Approach

We use **square root decomposition** to divide the baskets into √n blocks, each of size approximately √n:

1. Maintain a `maxV[]` array to track the **maximum capacity** in each block.
2. For each fruit:
   - Iterate over the blocks, and skip the block if its max capacity < fruit size.
   - When a suitable block is found, iterate **only within the block** to place the fruit.
   - After placing, update both `baskets[]` and the corresponding `maxV[]` for that block.
3. If no block can hold the fruit, count it as unplaced.

This optimization significantly reduces the number of comparisons per fruit.

---

### Complexity

- **Time Complexity:** `O(F × √N + N)`, where:

- - F = number of fruits

- - N = number of baskets

- - We check at most √N blocks per fruit, and each block has √N elements.

- **Space Complexity:** `O(√N)`, for the `maxV[]` array.

### Why Square Root Decomposition?

- Full iteration for each fruit → O(N × F), which is too slow.

- With square root decomposition, we reduce the number of checks dramatically by working with aggregated block-level data.

### Example

**Input:**
```python
fruits = [4, 5, 2]
baskets = [3, 5, 1, 6]
```

**Output:**
```python
1
```

### Explanation:

- 5 → basket[1] (5)

- 4 → basket[3] (6)

- 2 → basket[0] (3)

- All fruits placed successfully.

If we remove one basket, e.g., basket[1], then one fruit would remain unplaced.

### Tags

`Greedy`, `Square-Root-Decomposition`, `Optimization`, `Array`, `Simulation`

### Note

This is a good example of using **block decomposition** to solve time-constrained matching problems efficiently.