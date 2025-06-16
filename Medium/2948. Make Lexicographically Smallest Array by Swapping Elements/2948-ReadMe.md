# 🔄 LeetCode 2948 - Make Lexicographically Smallest Array by Swapping Elements

**Difficulty:** Hard  
**Problem Link:** [LeetCode 2948](https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements)

---

## 📘 Problem Description

Given an array `nums` and an integer `limit`, you are allowed to **swap any two elements** if their **absolute difference** is less than or equal to `limit`.

You can do **any number of swaps** under this rule. Your task is to **return the lexicographically smallest array** possible after performing these allowed swaps.

---

## 🔍 Example

### Input:
```python
nums = [1, 5, 3, 9, 8]
limit = 2
```

### Output:
```python
[1, 3, 5, 8, 9]
```

### 🧠 Approach & Intuition

The key idea is:

- If two elements `nums[i]` and `nums[j]` can be swapped directly or indirectly via a sequence of allowed swaps, they **belong to the same group** (component).

- Each group can be independently sorted to minimize lexicographical order.

- We use **Union-Find (Disjoint Set Union - DSU)** to group swappable indices.

#### Steps:
1. **Sort** the array while keeping original indices.

2. **Group** indices into components using DSU if the absolute difference between values is ≤ `limit`.

3. **Collect and sort** elements in each group.

4. **Reconstruct** the final result by inserting sorted values back into their positions within the group.

### ⏱️ Complexity

- **Time Complexity:** `O(n log n)`
(Due to sorting and DSU operations being near-constant time)

- **Space Complexity:** `O(n)`

### 🏷️ Tags
`greedy`, `union-find`, `sorting`, `graph`, `disjoint-set`, `lexicographic`

### ✅ Key Insight
This is a **graph connectivity** problem in disguise — if you treat swappable indices as connected, sorting within each connected group leads to the smallest array.