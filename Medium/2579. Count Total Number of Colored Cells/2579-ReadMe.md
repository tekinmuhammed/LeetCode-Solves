# 🟩 LeetCode 2579 - Count Total Number of Colored Cells

**Difficulty:** Easy  
**Problem Link:** [LeetCode 2579](https://leetcode.com/problems/count-total-number-of-colored-cells)

---

## 📘 Problem Description

There is a pattern of coloring cells over multiple steps. Initially, there is **1 colored cell**.

At step `n`, you color cells such that they form a diamond of side length `n`. Your task is to return the **total number of colored cells** after step `n`.

---

## 🧪 Examples

### Input:
```python
n = 3
```

### Output:

```python
13
```

Explanation:

- Step 1: 1 cell (center)

- Step 2: 5 cells total

- Step 3: 13 cells total

### 🔍 Pattern & Insight

This forms a diamond shape where each new layer adds 4 more cells than the previous.

The total number of colored cells after `n` steps is:

```python
1 + 4 * (1 + 2 + ... + (n - 1)) = 1 + 4 * ((n - 1) * n) // 2
```

This is an arithmetic series sum applied with geometric growth.

### ⏱️ Complexity

- **Time Complexity:** `O(1)`

- **Space Complexity:** `O(1)`

### 🏷️ Tags
`math`, `geometry`, `pattern-recognition`, `leetcode-easy`