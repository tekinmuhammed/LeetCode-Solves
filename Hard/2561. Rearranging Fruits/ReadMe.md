# 2561. Rearranging Fruits

**Difficulty:** Medium  
**Problem Link:** [LeetCode 2561](https://leetcode.com/problems/rearranging-fruits/)

---

## Problem Description

You are given two baskets of fruits, represented by two integer arrays `basket1` and `basket2`. Each integer represents a type of fruit. You are allowed to **swap** the fruits between the baskets. Your goal is to **make the two baskets have the same type and frequency** of fruits using the **minimum total cost**.

- The cost to swap two fruits `x` and `y` is `min(x, y)` unless you choose to remove both and insert two fruits of type `m`, where the cost becomes `2 * m` (m is the smallest fruit type across both baskets).
- You can only perform swaps between the baskets or use the auxiliary replacement strategy.

Return the **minimum total cost** to make the baskets identical, or `-1` if it's impossible.

---

### Example

**Input:**
```python
basket1 = [4,2,2,2]
basket2 = [1,4,1,2]
```

**Output:**
```python
1
```

### Approach

1. **Count Frequency Difference:**

- Use a `Counter` to track how many times each fruit appears in each basket.

- For a solution to exist, each fruit type must have an even total count.

2. **Build Swap List:**

- For each fruit where frequency differs, add half of the excess to a `merge` list.

3. **Calculate Minimum Swap Cost:**

- Sort the merge list to prioritize cheaper fruits first.

- The cost of each swap is either the fruit itself or `2 * m`, where `m` is the smallest fruit type (used as an auxiliary replacement).

### Complexity

- **Time Complexity:** `O(n log n)`
Sorting the `merge` list dominates the runtime.

- **Space Complexity:** `O(n)`
For storing frequency map and swap list.

### Tags

`Greedy`, `Sorting`, `Hash-Table`, `Math`

### Notes

- Key insight: it's cheaper to replace two expensive fruits with the smallest one than to swap them directly.

- Efficient handling of imbalances through frequency counting and minimal replacement cost is critical.