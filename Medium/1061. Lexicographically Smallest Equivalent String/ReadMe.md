# 1061. Lexicographically Smallest Equivalent String

**Problem Link:** [LeetCode 1061](https://leetcode.com/problems/lexicographically-smallest-equivalent-string/)  
**Difficulty:** Medium

## Problem Description

You are given two strings `s1` and `s2` of equal length, which define equivalence relationships between characters.  
Each character `s1[i]` is equivalent to `s2[i]`, and equivalence is **transitive and symmetric**.  

You are also given a string `baseStr`.  
Your task is to return the lexicographically smallest string that can be formed by replacing each character in `baseStr` with its **smallest equivalent character**.

---

## Example

```python
Input: s1 = "parker", s2 = "morris", baseStr = "parser"
Output: "makkek"
```

---

## Approach

- We use a **Union-Find (Disjoint Set Union)** data structure to group equivalent characters.
- During union operations, we always keep the **smallest character** in the group as the representative to ensure minimal lexicographical output.
- Finally, we map each character in `baseStr` to its group's representative.

---

### Complexity

- **Time:** `O(N + M)`, where N = len(s1), M = len(baseStr)

- **Space:** `O(1)`, uses constant space for 26 lowercase letters

### Tags

`Union-Find`, `Greedy`, `Graph`, `String`