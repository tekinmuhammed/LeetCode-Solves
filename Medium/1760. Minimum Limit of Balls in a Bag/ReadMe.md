# 🎯 LeetCode 1760 - Minimum Limit of Balls in a Bag

**Difficulty:** Medium  
**Problem Link:** [LeetCode 1760](https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/)

---

## 📘 Problem Description

You are given:

- `nums`: A list where `nums[i]` is the number of balls in the `i-th` bag.
- `maxOperations`: The maximum number of operations you can perform.

**Operation Rule:** In one operation, you can split one bag of balls into **two** bags **with positive number of balls**.

Your goal is to **minimize the maximum number of balls** in any bag **after** performing at most `maxOperations` operations.

---

## 🧪 Example

### Input:
```python
nums = [9]
maxOperations = 2
```

## Output:
```python
3
```

## Explanation:

- One possible way: split 9 → [6, 3], then split 6 → [3, 3, 3].

- Maximum balls in a bag: 3.

## 🚀 Approach

We want the **smallest possible maximum bag size**, so:

- Use **binary search** on the result:

- - Search between `1` and `max(nums)`

- - For each candidate `maxPenalty`, check:

- - - How many operations are needed to ensure all bags have ≤ `maxPenalty` balls?

- - - For each `num`, the number of splits is `(num - 1) // maxPenalty`

- If the number of operations is within `maxOperations`, we try smaller penalty (move left).
Otherwise, we try bigger penalty (move right).

## ⏱️ Complexity

- **Time Complexity:** `O(n * log(max(nums)))`

- **Space Complexity:** `O(1)`

## 🏷️ Tags

`binary-search`, `greedy`, `splitting`, `bags`, `leetcode-medium`