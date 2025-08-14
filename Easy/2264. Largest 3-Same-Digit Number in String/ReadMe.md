# 2264. Largest 3-Same-Digit Number in String
**Difficulty:** Easy  
**Problem Link:** [LeetCode 2264](https://leetcode.com/problems/largest-3-same-digit-number-in-string/description/)

---

## Problem Description
Given a string `num` consisting of digits, the goal is to find the **largest 3-digit substring** where all three digits are the same. If no such substring exists, return an empty string.

A "good integer" is defined as a substring of length 3 where all digits are identical (e.g., `"999"`, `"777"`, `"000"`). Among all possible good integers in the string, we must return the largest one in terms of numeric value.

---

## Approach
The solution takes a **direct search approach** by:
1. Defining all possible good integers in **descending order** from `"999"` down to `"000"`.
2. Iterating through this list to check if each possible good integer exists in the input string `num`.
3. Returning the **first match** found, since the list is sorted in descending order, guaranteeing the largest possible answer.

This approach is efficient because:
- The search space is very small (only 10 possible patterns).
- The first match found is guaranteed to be the largest possible good integer.
- The solution avoids unnecessary comparisons after finding the match.

---

## Detailed Steps
1. **Create the list of possible good integers**:  
   ```python
   same_digit_numbers = ["999", "888", "777", "666", "555", "444", "333", "222", "111", "000"]
   ```

This ensures we always check from the largest to the smallest.

2. **Helper function** `contains(same_digit_number)`:

This function scans through `num` to see if the given 3-digit repeated number appears as a substring.
It uses a loop with indexing rather than Python’s built-in `in` operator for explicit checking.

3. **Iterate through each possible good integer:**

- - For each candidate, call `contains()`.

- - If found, immediately return it.

4. **Return empty string if none are found.**

### Time Complexity

- `O(1)` in practical terms, because the number of patterns to check is fixed at 10.

- Each pattern search runs in **O(n)**, where `n` is the length of `num`.
Thus, worst-case complexity is **O(10 × n) ≈ O(n)**.

### Example Walkthrough

**Example 1:**
```python
Input: num = "6777133339"
Step 1: Check "999" → not found
Step 2: Check "888" → not found
Step 3: Check "777" → found (at index 1)
Output: "777"
```

**Example 2:**
```python
Input: num = "2300019"
Step 1: Check "999" → not found
...
Step 10: Check "000" → found (at index 2)
Output: "000"
```

### Key Insight

- Sorting the list of good integers in **descending order** ensures that the first match is the answer, eliminating the need to compare values after finding a match.

- Since the pattern length is fixed (3 digits), this method is **very fast** and requires no extra space beyond the list of possible values.