# 📦 LeetCode 1769 - Minimum Number of Operations to Move All Balls to Each Box

**Difficulty:** Medium  
**Problem Link:** [LeetCode 1769](https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box)

---

## 📘 Problem Description

You are given a binary string `boxes` of length `n`, where:
- Each character is either `'0'` (no ball) or `'1'` (has a ball).

For each box `i`, compute the **minimum number of operations** needed to move **all balls** to box `i`.

**Rules:**
- You can move a ball from one box to an adjacent box in **1 operation**.

Return a list of size `n`, where each element is the total number of moves to gather all balls at that index.

---

## 🧪 Example

### Input:
```python
boxes = "110"
```

### Output:

`[1, 1, 3]`

### Explanation:

- To move all balls to box 0: 1 move (ball from index 1) → total = 1

- To move all balls to box 1: 1 move (ball from index 0) → total = 1

- To move all balls to box 2: 1 move (from 0) + 2 moves (from 1) → total = 3

### 🚀 Approach

To avoid a naive O(n²) solution, we use a **two-pass linear scan**:

1. **Left to Right Pass**

- Track how many balls (`count`) have been seen so far.

- Add `count` to cumulative moves for each step.

- This gives cost of moving left-side balls to each index.

2. **Right to Left Pass**

- Do the same in reverse to handle right-side balls.

By summing these two passes, we get the total moves required for each box.

### ⏱️ Complexity
- **Time Complexity:** `O(n)` — two linear passes

- **Space Complexity:** `O(n)` — for the result array

### 🏷️ Tags
`array`, `prefix-sum`, `simulation`, `two-pass`, `leetcode-medium`