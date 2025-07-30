# 3333. Find the Original Typed String II

**Difficulty:** Hard  
**Link:** [LeetCode 3333](https://leetcode.com/problems/find-the-original-typed-string-ii)

---

## Problem Description

You are given a string `word` formed by holding down keys and potentially typing characters multiple times.

Also, you're given an integer `k`. Your task is to find how many **distinct original strings** of length **at least `k`** can result in the `word` through key holding.

### A valid original string:
- Contains only one of each group of consecutive identical characters from `word`.
- The total length of the original string must be **at least `k`**.

Return the number of such distinct original strings modulo **10⁹ + 7**.

---

## Constraints

- `1 <= word.length <= 10⁵`
- `1 <= k <= word.length`
- `word` contains only lowercase English letters

---

## Example

### Input:
```python
word = "aaabbcc"
k = 3
```

### Output:
`15`

### Intuition & Approach

**Step 1: Group Frequencies**

- Count consecutive character groups: e.g., `"aaabbcc"` becomes groups `[3,2,2]`.

**Step 2: Total Possibilities**

- Each group of `g` identical characters allows `g` choices (press the key 1, 2, ..., `g` times).

- So the **total number of all typed sequences** is the product of each group size.

**Step 3: Remove Invalids**

- Some of these sequences correspond to original strings shorter than `k`. These are invalid.

- Use **Dynamic Programming (DP)** to count and subtract those invalid original strings with fewer than `k` characters.

### Algorithm

1. Build a `freq` list of group lengths.

2. Calculate `ans = freq[0] * freq[1] * ... * freq[n-1]` modulo 10⁹+7.

3. Use a DP array `f[j]` to store number of subsequences that create original strings of length `j`.

4. Subtract the number of sequences that have original length `< k` (using prefix sums for efficiency).

5. Return `(ans - g[k-1]) % mod`.

### Time and Space Complexity

- **Time Complexity:** `O(n + k × g)`

where `n` is the length of `word`, and `g` is the number of groups.

- **Space Complexity:** `O(k)`

### Tags

`Dynamic-Programming`, `Prefix-Sum`, `Combinatorics`, `String-Grouping`, `Hard`

### Notes

- This problem extends the idea of "long press typing" by introducing combinatorics and DP to **restrict the shape** of valid originals.

- A clever use of prefix sums (`g[]`) makes the solution efficient even for large `k`.