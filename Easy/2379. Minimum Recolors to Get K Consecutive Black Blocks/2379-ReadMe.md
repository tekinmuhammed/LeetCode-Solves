# 🎨 LeetCode 2379 - Minimum Recolors to Get K Consecutive Black Blocks

**Difficulty:** Easy  
**Problem Link:** [LeetCode 2379](https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks)

---

## 📘 Problem Description

You are given a string `blocks` consisting of `'B'` (black) and `'W'` (white) characters, and an integer `k`.

Your task is to return the **minimum number of white blocks** that must be recolored to black in order to have at least **one substring of length `k`** consisting only of black blocks (`'B'`).

---

## 🧪 Examples

### Example 1:
```python
Input: blocks = "WBBWWBBWBW", k = 7
Output: 3
Explanation: Need to recolor 3 white blocks in the best 7-length window.
```

### Example 2:
```python
Input: blocks = "WBWBBBW", k = 2
Output: 0
Explanation: Already has a substring "BB".
```

### 🧠 Approach

- Use a **sliding window** of size `k` to check each substring.

- Count the number of `'W'` in the current window.

- Update the minimum number of white blocks to recolor as the window slides.

### ⏱️ Complexity

- **Time Complexity:** O(n), where `n` is the length of `blocks`.

- **Space Complexity:** O(1)

### 🏷️ Tags
`sliding-window`, `string`, `greedy`, `easy`