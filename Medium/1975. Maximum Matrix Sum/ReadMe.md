# 🟦 LeetCode 1975 - Maximum Matrix Sum

**Difficulty:** Medium  
**Problem Link:** [LeetCode 1975](https://leetcode.com/problems/maximum-matrix-sum)

---

## 📘 Problem Description

Given an `n x n` integer matrix, you are allowed to **negate** any number of elements (change sign).  
Your goal is to maximize the sum of all elements after doing any number of such operations.

---

## 🧪 Example

### Input:
```python
matrix = [
    [1, -1],
    [-1, 1]
]
```

### Output:

`4`

## 🚀 Approach

- Sum Absolute Values:

- - No matter what, each element contributes its absolute value to the maximum potential sum.

- Track Sign Information:

- - Count how many negative numbers there are.

- - Track the smallest absolute value in the matrix.

- Handle Odd Negatives:

- - If there’s an even number of negative numbers, we can flip them all to positive — return total absolute sum.

- - If there’s an odd number, we must leave one negative — subtract twice the smallest absolute value.

## ⏱️ Complexity

- **Time Complexity:** O(n²)

- **Space Complexity:** O(1)

## 🏷️ Tags

`matrix`, `greedy`, `math`, `absolute-value`, `sign-handling`, `leetcode-medium`