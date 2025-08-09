# 🔺 LeetCode 3066 - Minimum Operations to Exceed Threshold Value II

**Difficulty:** Medium  
**Problem Link:** [LeetCode 3066](https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii)

---

## 📘 Problem Description

You are given an array `nums` and an integer `k`.

You can perform the following operation multiple times:
- Choose the two **smallest elements** `x` and `y` from `nums`.
- Remove them, and insert a new element: `new = x * 2 + y`.

Return the **minimum number of operations** required to make **all elements in the array ≥ k**.

If it's impossible, return `-1`.

---

## 🧪 Example

### Input:
```python
nums = [1, 1, 1, 1]
k = 10
```

### Output:
```python
2
```

### Explanation:

- Operation 1: pick 1 and 1 → new = 1×2 + 1 = 3 → nums = [1, 1, 3]

- Operation 2: pick 1 and 1 → new = 1×2 + 1 = 3 → nums = [3, 3]

- Now all values ≥ 3, but not ≥ 10 → Keep going until all ≥ 10

After 4 operations → [15], which is ≥ 10 → Output: 4

### 🚀 Approach

We use a **min-heap** to always access the two smallest numbers efficiently:

- While the smallest element is less than `k`, pop the two smallest elements `x` and `y`.

- Push `x * 2 + y` back into the heap.

- Count how many such operations are needed.

Check if after operations the heap’s smallest element is ≥ `k`. If not, return `-1`.

### ⏱️ Complexity

- **Time Complexity:** `O(n log n)` — heap operations

- **Space Complexity:** `O(n)`

### 🏷️ Tags

`heap`, `priority-queue`, `greedy`, `simulation`, `leetcode-medium`