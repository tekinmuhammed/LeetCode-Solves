# 3330. Find the Original Typed String I

**Difficulty:** Easy  
**Link:** [LeetCode 3330](https://leetcode.com/problems/find-the-original-typed-string-i)

---

## Problem Description

You are given a string `word`, which is a version of an original string typed with a keyboard that **might allow repeating characters due to long key presses**.

Your task is to determine **how many possible original strings** could have produced the given typed string.

A valid original string only differs from `word` in that some characters **might have been typed more than once** consecutively.

Return the **number of possible original strings**.

---

## Example

### Input:
```python
word = "aabb"
```

### Output:
`2`

### Explanation:

The original string could be either:

- `"ab"` → by holding keys down for `a` and `b`, you get `"aabb"`.

- `"aab"` → by holding `a`, typing it twice, and pressing `b`.

So, 2 valid original strings can result in `"aabb"`.

### Constraints

- `1 <= word.length <= 10⁵`

- `word` contains only lowercase English letters.

### Approach

**Key Insight:**

Every **group of consecutive same letters** in `word` can correspond to **multiple typing patterns**, depending on how many times the key was held down.

The number of possible original strings is equal to **the number of character changes** (from one letter to a different one), plus 1 (for the first group).

### Algorithm

1. Initialize a result counter `ans` to 1 (first group always contributes one option).

2. Traverse the `word` from index 1:

- If the current character is **different** from the previous one, it's a new group → increment `ans`.

3. Return `ans`.

### Time and Space Complexity

- **Time Complexity:** `O(n)` — single pass over the string.

- **Space Complexity:** `O(1)` — constant extra space used.

### Tags

`Greedy`, `String`, `Counting`

### Notes

- This is a simplified version of "long press key" problems, where you determine how many different shorter original strings could result in a given longer typed output.

- The key observation is grouping consecutive characters and counting transitions.