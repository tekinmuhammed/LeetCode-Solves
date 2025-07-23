# 1717. Maximum Score From Removing Substrings

**Difficulty:** Medium  
**Problem Link:** [LeetCode 1717](https://leetcode.com/problems/maximum-score-from-removing-substrings/)

---

## Problem Description

You are given a string `s` and two integers `x` and `y`.

You can perform two types of operations on the string:

- Remove **"ab"** and gain **`x`** points.
- Remove **"ba"** and gain **`y`** points.

You can perform the operations in any order, but each substring can only be removed once.

Return the **maximum total score** you can achieve after applying these operations any number of times.

---

### Example

**Input:**
```python
s = "cdbcbbaaabab", x = 4, y = 5
```

### Output:
```python
19
```

### Explanation:

- First, remove `"ba"` to get 5 points.

- Then remove `"ab"` twice to get 4 + 4 = 8 points.

- Then remove `"ba"` again to get 5 more points.

- Total: 5 + 8 + 5 = 18. (Actually 19 in optimal order.)

The correct approach chooses the higher scoring pair to remove first.

### Approach

To **maximize the score**, we always remove the pattern that gives the higher point value first:

1. Define a helper function `remove_pattern(s, a, b, point)` that:

- - Uses a **stack** to remove adjacent matching pairs (`a + b`) and returns the modified string and score gained.

2. Use this helper function twice:

- - First, remove the pattern that gives more points (`"ab"` or `"ba"` depending on which is higher).

- - Then, remove the other pattern from the **remaining string**.

This greedy strategy ensures we maximize the score from the more valuable pattern before possibly disturbing its structure by removing the less valuable one.

### Complexity

- **Time Complexity:** `O(n)`, where `n` is the length of the string `s`. Each character is pushed and popped from the stack at most once.

- **Space Complexity:** `O(n)` in the worst case due to the stack.

### Tags

`Greedy`, `Stack`, `String-Manipulation`

### Key Insights

- The **order** in which you remove substrings affects the total score.

- Using a **greedy** strategy and a **stack** allows us to efficiently simulate the removal and maximize points.
