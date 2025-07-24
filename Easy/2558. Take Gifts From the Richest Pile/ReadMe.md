# 🟨 LeetCode 2558 - Take Gifts From the Richest Pile

**Difficulty:** Easy  
**Problem Link:** [LeetCode 2558](https://leetcode.com/problems/take-gifts-from-the-richest-pile/)

---

## 📘 Problem Description

You are given an integer array `gifts`, where `gifts[i]` represents the number of gifts in the `i-th` pile.

You can perform the following operation exactly `k` times:

- Choose the pile with the most gifts.
- Replace its value with the **floor of its square root** (i.e., `floor(sqrt(gifts[i]))`).

Return the **total number of gifts remaining** after performing this operation `k` times.

---

## 🧪 Example

### Input
```python
gifts = [25, 64, 9, 4]
k = 4
```

### Output
```python
29
```

## Explanation

- Step 1: Take 64 → becomes 8 → [25, 8, 9, 4]

- Step 2: Take 25 → becomes 5 → [5, 8, 9, 4]

- Step 3: Take 9 → becomes 3 → [5, 8, 3, 4]

- Step 4: Take 8 → becomes 2 → [5, 2, 3, 4]

- Total sum: 5 + 2 + 3 + 4 = 14

## 🚀 Approach

- For `k` iterations:

- - Find the index of the maximum value in `gifts`.

- - Replace that value with the floor of its square root using `math.floor(math.sqrt(...))`.

- After all operations, return the sum of the modified array.

## ⏱️ Complexity

**Time Complexity:** `O(k * n)`

- Each iteration involves scanning the list to find the max.

**Space Complexity:** `O(1)`

- In-place operations on the `gifts` list.

> **💡 Optimization Tip:** You can improve performance to `O(k * log n)` by using a max-heap (priority queue).

## 🏷️ Tags

`array`, `math`, `greedy`, `priority-queue`, `simulation`, `leetcode-easy`