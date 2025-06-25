# 🔢 LeetCode 2965 - Find Missing and Repeated Values

**Difficulty:** Easy  
**Problem Link:** [LeetCode 2965](https://leetcode.com/problems/find-missing-and-repeated-values)

---

## 📘 Problem Description

You are given an `n x n` grid that should contain all numbers from `1` to `n^2` exactly once. However, due to an error:
- One number appears **twice** (repeated).
- One number is **missing**.

Your task is to return `[repeated, missing]`.

---

## 🧪 Examples

### Input:

```python
grid = [[1, 3], [2, 2]]
```

### Output:

```python
[2, 4]
```

### 🧠 Approach

1. **Flatten the 2D grid** into a 1D list.

2. **Count occurrences** using a `Counter`.

3. **Scan from 1 to n²** to find:

- Number that appears `twice` → repeated

- Number that appears `zero times` → missing

### ⏱️ Complexity

- **Time Complexity:** `O(n²)` — flattening and counting

- **Space Complexity:** `O(n²)` — for storing frequencies

### 🏷️ Tags
`hashmap`, `counting`, `matrix`, `easy`