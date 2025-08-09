# 🔢 LeetCode 2698 - Find the Punishment Number of an Integer

**Difficulty:** Medium  
**Problem Link:** [LeetCode 2698](https://leetcode.com/problems/find-the-punishment-number-of-an-integer)

---

## 📘 Problem Description

Given a positive integer `n`, the **punishment number** is defined as the **sum of the squares** of all integers `i` in the range `[1, n]` such that:

- `i * i` can be split into **one or more substrings**, and
- the sum of these substrings (interpreted as integers) equals `i`.

Return the **punishment number** of `n`.

---

## 🧪 Example

### Input:
```python
n = 10
```

### Output:
```python
182
```

### Explanation:

- Valid values:

- - 1 → 1² = "1" → 1 == 1 ✅

- - 9 → 9² = "81" → 8 + 1 = 9 ✅

- - 10 → 10² = "100" → 10 + 0 = 10 ✅

- Punishment number: 1² + 9² + 10² = 1 + 81 + 100 = 182

### 🚀 Approach

We iterate from `1` to `n`, and for each number:

1. Square the number.

2. Check if the square can be **partitioned into substrings** whose numeric sum equals the original number.

- Use backtracking (DFS) to explore all possible partitions.

- If at any point the sum exceeds the target, prune the path.

If valid, add the square of the number to the total punishment sum.

### ⏱️ Complexity

- **Time Complexity:** `O(n · 2^d)`, where `d` is the number of digits in `i²` (backtracking over digit partitions).

- **Space Complexity:** `O(d)` for recursive call stack.

### 🏷️ Tags

`backtracking`, `math`, `recursion`, `string`, `leetcode-medium`