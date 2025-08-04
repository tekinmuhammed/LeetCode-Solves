# 904. Fruit Into Baskets

**Difficulty:** Medium  
**Problem Link:** [LeetCode 904](https://leetcode.com/problems/fruit-into-baskets)

---

## Problem Description

You are visiting a fruit farm, and the farm has a row of trees. Each tree produces exactly one type of fruit.

You can carry **at most two types of fruit**, and your baskets can carry any amount of fruit, but only one type per basket.

You want to pick as many fruits as possible from a **contiguous** subarray of trees, while carrying only **two types** of fruits.

Return the length of the longest such subarray.

---

### Example

**Input:**
```python
fruits = [1,2,1,2,3]
```

**Output:**
```python
4
```

### Explanation:

You can pick from index 0 to 3 (1,2,1,2). Total = 4 fruits. You can't pick `3` because it would require a third basket.

### Approach

This problem is equivalent to finding the **length of the longest subarray with at most two distinct elements**.

We can use the **sliding window** technique:

1. Use two pointers (`left` and `right`) to define a window.

2. Maintain a hash map (or `defaultdict`) to count fruit types in the current window.

3. When more than two types are present, move the `left` pointer forward until the condition is satisfied again.

4. Update the `max_len` as you go.

### Complexity

- **Time Complexity:** `O(N)`
Each fruit is added and removed from the window at most once.

- **Space Complexity:** `O(1)`
Since only 2 types of fruits are allowed at a time, the map will contain at most 2 keys.

### Tags

`Sliding-Window`, `Hash-Map`, `Two-Pointers`

### Notes

- This pattern is widely used in other problems like:

- - Longest Substring Without Repeating Characters

- - Longest Substring with At Most K Distinct Characters

- Use of `defaultdict` simplifies the counting logic.