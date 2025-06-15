# ✂️ LeetCode 3223 - Minimum Length of String After Operations

**Difficulty:** Easy  
**Problem Link:** [LeetCode 3223](https://leetcode.com/problems/minimum-length-of-string-after-operations/)

---

## 📘 Problem Description

You are given a string `s`. In one operation, you can choose **any character** that occurs **at least twice**, and remove **two occurrences** of it.

You can repeat this operation as many times as possible.

Return the **minimum length** of the string after performing the operations.

---

## 🧪 Example

### Input:
```python
s = "aabccc"
```

### Output:
`1`

### Explanation:

- Remove two `'a'` → string becomes `"bccc"`

- Remove two `'c'` → string becomes `"bc"`

- Now nothing more can be removed → length is `1`.

### 🧠 Approach

#### Key Idea:

- For every character in the string:

- - As long as its count is ≥ 2, we can remove two of them at a time.

- - This process reduces its count by 2 repeatedly.

- - Eventually, each character can remain with at most 0 or 1 occurrence.

So, for each character with count `≥ 3`, we simulate these operations by subtracting 2 repeatedly.

The **final result** is the total remaining character count.

### ⏱️ Complexity

- **Time Complexity:** `O(n * m)`, where `n` is length of `s`, and `m` is the number of iterations to reduce frequent characters (can be optimized).

- **Space Complexity:** `O(1)` (since max 26 lowercase letters)

### ✅ Optimization Note

You can optimize `while f[k] >= 3: f[k] -= 2` with a one-liner:

```python
f[k] = f[k] % 2 if f[k] > 1 else f[k]
```

Or rewrite the logic like this:

```python
for k in f:
    if f[k] >= 2:
        f[k] %= 2
```

### 🏷️ Tags
`greedy`, `counting`, `hashmap`, `string`