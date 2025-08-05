# 3477. Fruits Into Baskets II

**Difficulty:** Easy  
**Problem Link:** [LeetCode 3477](https://leetcode.com/problems/fruits-into-baskets-ii) *(contest problem)*

---

## Problem Description

You are given two arrays:
- `fruits[i]`: the size of the `i-th` fruit.
- `baskets[j]`: the capacity of the `j-th` basket.

Each basket can hold **at most one fruit**, and each fruit must be placed into a **single unused basket** whose capacity is **greater than or equal to** the fruit’s size.

Your task is to return the **number of fruits that could not be placed into any basket**.

---

### Example

**Input:**
```python
fruits = [1, 3, 2]
baskets = [2, 1, 3]
```

**Output:**
```python
0
```

### Explanation:

All fruits can be placed into baskets:

- Fruit 1 → Basket with capacity 1

- Fruit 3 → Basket with capacity 3

- Fruit 2 → Basket with capacity 2

### Approach

This is a simple **greedy matching** problem:

- For each fruit, try to find any unused basket that can fit it (i.e., basket ≥ fruit size).

- If found, mark the basket as used.

- If no such basket exists, increase the count of unplaced fruits.

We maintain a `used[]` array to track which baskets are already used.

### Complexity

- **Time Complexity:** `O(N²)`

- - For each fruit (N), you may check all baskets (N).

- **Space Complexity:** `O(N)`

- - For the `used` list.

### Optimization Tip

To improve efficiency for large inputs:

- - Sort `fruits` and `baskets`

- - Use a greedy two-pointer approach (match smallest fruit with smallest possible basket)

### Tags

`Greedy`, `Matching`, `Simulation`, `Array`

### Notes

- This is an example of a basic **resource allocation** problem.

- For higher constraints, sorting would be essential for performance.