# 🔍 LeetCode 1346 - Check If N and Its Double Exist

**Difficulty:** Easy  
**Problem Link:** [LeetCode 1346](https://leetcode.com/problems/check-if-n-and-its-double-exist)

---

## 📘 Problem Description

Given an array `arr` of integers, check if there exist **two indices** `i` and `j` such that:

- `i != j`
- `arr[i] == 2 * arr[j]`

Return `True` if such elements exist, otherwise return `False`.

---

## 🧪 Example

### Input:
```python
arr = [10, 2, 5, 3]
```

## Output:
```python
True
```
## Explanation:
`10 == 2 * 5`

## 🚀 Approach
We use a `set` to keep track of previously seen numbers.

For each number in the array:

- Check if its double exists in the set

- Or if it is even, check if its half exists in the set

If found, return `True`. Otherwise, after the loop, return `False`.

## ⏱️ Complexity
- **Time Complexity:** `O(n)`

- **Space Complexity:** `O(n)` (for the `seen` set)

## 🏷️ Tags
`array`, `set`, `hash-table`, `search`, `leetcode-easy`