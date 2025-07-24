# 2138. Divide a String Into Groups of Size k

**Difficulty:** Easy  
**Problem Link:** [LeetCode 2138](https://leetcode.com/problems/divide-a-string-into-groups-of-size-k)

---

## Problem Description

Given a string `s`, divide it into groups of size `k`. If the last group is smaller than `k` characters, fill the remaining characters with the given `fill` character so that each group has exactly length `k`.

Return a list of the string groups.

---

## Example

### Input:

```python
s = "abcdefghi", k = 3, fill = "x"
```

### Output:
```python
["abc", "def", "ghi"]
```

### Input:

```python
s = "abcdefghij", k = 3, fill = "z"
```

### Output:

```python
["abc", "def", "ghiz"]
```

### Constraints

- `1 <= s.length <= 100`

- `s` consists of lowercase English letters.

- `1 <= k <= 100`

- `fill` is a lowercase English letter.

### Approach

- Iterate through the string `s` in steps of `k`.

- Extract substrings of length `k`.

- If a substring is shorter than `k`, fill it with the character `fill` until it reaches length `k`.

- Append each group to the result list.

### Time and Space Complexity

- **Time Complexity:** `O(n)`, where `n` is the length of the string `s`.

- **Space Complexity:** `O(n / k)` for storing the groups.

### Tags

`String`, `Simulation`, `LeetCode-Easy`

### Notes

- This is a good example of a simple simulation-based string manipulation problem.

- Padding logic is critical to ensure all output strings are of equal length.