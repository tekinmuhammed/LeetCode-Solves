# 🟨 LeetCode 1652 - Defuse the Bomb

**Difficulty:** Easy  
**Problem Link:** [LeetCode 1652](https://leetcode.com/problems/defuse-the-bomb/)

---

## 📘 Problem Description

You are given a list of integers called `code` and an integer `k`. The list is circular, and your goal is to return a new list such that:

- If `k > 0`: each element at index `i` becomes the sum of the next `k` elements (wrapping around).
- If `k < 0`: each element becomes the sum of the previous `k` elements (wrapping around).
- If `k == 0`: each element becomes `0`.

---

## 🧪 Example

### Input:
```python
code = [5, 7, 1, 4]
k = 3
```

## Output:
```python
[12, 10, 16, 13]
```

## 🚀 Approach

- We use modular arithmetic (`% n`) to handle the circular nature of the array.

- For each index `i`, compute the sum of the required `k` elements depending on the sign of `k`.

- Time complexity is `O(n * |k|)`, which is acceptable for small values of `k`.

## ⏱️ Complexity

- **Time Complexity:** O(n * |k|)

- **Space Complexity:** O(n)

## 🏷️ Tags
`array`, `simulation`, `circular-array`, `leetcode-easy`
        