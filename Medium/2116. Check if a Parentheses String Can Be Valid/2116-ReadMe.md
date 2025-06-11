# 🧩 LeetCode 2116 - Check if a Parentheses String Can Be Valid

**Difficulty:** Medium  
**Problem Link:** [LeetCode 2116](https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid)

---

## 📘 Problem Description

You are given two strings:

- `s` — a string consisting of `'('` and `')'`
- `locked` — a string of the same length where:
  - `'1'` means the character in `s` **cannot be changed**
  - `'0'` means the character in `s` **can be changed** to either `'('` or `')'`

Return `True` if it's possible to make `s` a **valid parentheses string**, else return `False`.

---

## 🧪 Example

### Input:
```python
s = "))()))"
locked = "010100"
```

### Output:

`True`

#### 🧠 Approach

**Key Insight:**

- To be valid, the parentheses string must always maintain a **non-negative balance** while scanning from left to right (and from right to left for symmetry).

- Any `locked[i] == '0'` character gives flexibility to "fix" the string by replacing that position with `'('` or `')'`.

#### Two-Pass Greedy Scan:

1. Left to Right:

- Simulate balance by treating `locked == '0'` or `s[i] == '('` as adding to the open count.

- If at any point `open_count < 0`, too many unmatched `)` → return `False`.

2. Right to Left:

- Do a similar scan, but treat `locked == '0'` or `s[i] == ')'` as adding to close count.

- If `close_count < 0`, then too many unmatched `(` → return `False`.

3. If both passes succeed → return `True`.

#### Edge Case:

- If length of string `s` is odd → can't ever be valid → return `False`.

###  ⏱️ Complexity

- **Time Complexity:** `O(n)`

- **Space Complexity:** `O(1)`

### 🏷️ Tags
`greedy`, `string`, `parentheses`, `two-pointers`