# 🔁 LeetCode 2657 - Find the Prefix Common Array of Two Arrays

**Difficulty:** Medium  
**Problem Link:** [LeetCode 2657](https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/)

---

## 📘 Problem Description

You are given two **0-indexed integer arrays** `A` and `B` of length `n`.

A **prefix common array** `C` is defined such that `C[i]` is the number of **common elements** between `A[0..i]` and `B[0..i]`.

Return the array `C`.

---

## 🧪 Example

### Input:
```python
A = [1,3,2,4]
B = [3,1,2,4]
```

### Output:
```python
[0,2,3,4]
```

### Explanation:
- i = 0: A[0]=1, B[0]=3 → no common → `0`

- i = 1: A[:2]=[1,3], B[:2]=[3,1] → common = {1,3} → `2`

- i = 2: common = {1,2,3} → `3`

- i = 3: all values match → `4`

### 🧠 Approach

- Use a **set** to keep track of all the elements seen so far from both arrays.

- At each index `i`, check if `A[i]` and `B[i]` are already seen.

- If yes, increment the common count.

- If not, add them to the set.

- Append the current count to the result array.

### ⏱️ Complexity
- **Time Complexity:** `O(n)` — Single pass through arrays

- **Space Complexity:** `O(n)` — At most `2n` distinct elements in `seen`

### 🧼 Note

The code handles the double count of `A[i] == B[i]` gracefully, since `A[i]` and `B[i]` are processed separately and the `seen` set ensures uniqueness.

### 🏷️ Tags
`prefix`, `hashing`, `array`, `set`, `simulation`