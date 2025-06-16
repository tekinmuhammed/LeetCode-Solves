# ✨ LeetCode 3151 - Special Array I

**Difficulty:** Easy  
**Problem Link:** [LeetCode 3151](https://leetcode.com/problems/special-array-i)

---

## 🧩 Problem Description

You are given an array of integers `nums`. The array is **special** if **no two adjacent elements** have the same **parity** (even/odd status).

### Task:
Return `True` if the array is special, otherwise return `False`.

---

## 🔍 Example

### Input:
```python
nums = [2, 1, 4]
```

### Output:
`False`

### Explanation:

- 2 (even) → 1 (odd) ✅

- 1 (odd) → 4 (even) ✅

- BUT 4 is even and follows 2 (even), so it's not valid.

### 🧠 Approach & Intuition
This is a straightforward problem where we check the **parity (even or odd)** of adjacent elements.

#### 🔧 Strategy:

- Traverse the array from start to end.

- Compare each `nums[i] % 2` with `nums[i + 1] % 2`.

- If they are the same, the array is **not special**.

### ⏱️ Complexity

- **Time Complexity:** `O(n)`
We check each adjacent pair once.

- **Space Complexity:** `O(1)`
No extra space is used.

### 🏷️ Tags
`array`, `parity`, `adjacency`, `easy`, `implementation`

### ✅ Key Insight
The parity of a number can be determined using `num % 2`. To ensure alternating parity, adjacent elements must differ in their mod 2 values.
