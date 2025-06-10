# 🔁 LeetCode 2381 - Shifting Letters II

**Difficulty:** Medium  
**Problem Link:** [LeetCode 2381](https://leetcode.com/problems/shifting-letters-ii)

---

## 📘 Problem Description

You are given a lowercase string `s` and a list of shift operations `shifts`, where each shift is represented as `[start, end, direction]`:
- `start` and `end` define a substring of `s`.
- `direction` is `1` for shifting characters **forward** (e.g. `'a' → 'b'`) and `0` for shifting **backward** (e.g. `'b' → 'a'`).

You must apply **all shift operations**, and return the **final shifted string**.

Each letter wraps around the alphabet (i.e., `'z' + 1 = 'a'` and `'a' - 1 = 'z'`).

---

## 🧪 Example

### Input:
```python
s = "abc"
shifts = [[0,1,0],[1,2,1],[0,2,1]]
```

### Output:
`"ace"`

### Explanation:
 
1. Apply `[0,1,0]`: shift s[0:1] backward → `"zbc"`

2. Apply `[1,2,1]`: shift s[1:2] forward → `"zcc"`

3. Apply `[0,2,1]`: shift entire string forward → `"ace"`

### 🚀 Approach

- Use a **difference array (delta)** to efficiently track multiple range updates.

- For each operation:

- - If direction is forward, add `+1` to `delta[start]` and `-1` to `delta[end+1]`.

- - If direction is backward, do the opposite.

- Convert `delta` to prefix sums to get net shifts per character.

- Apply the shift at each index, using modulo 26 to wrap around the alphabet.

This avoids applying each shift directly (which would be O(n × m)), and improves performance to linear time.

### ⏱️ Complexity
- **Time Complexity:** `O(n + m)`, where

- - `n = len(s)`

- - `m = len(shifts)`

- **Space Complexity:** `O(n)`, due to the delta array

### 🏷️ Tags
`string`, `prefix-sum`, `range-update`, `difference-array`, `leetcode-medium`