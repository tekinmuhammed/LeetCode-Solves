# 1513. Number of Substrings With Only 1s — README

**Difficulty:** Medium  
**Link:** [LeetCode 1513](https://leetcode.com/problems/number-of-substrings-with-only-1s/description/)  

## 📌 Problem Summary
Given a binary string `s`, count how many substrings contain **only `'1'` characters**.

Example:  
`s = "11101"` → valid substrings are the continuous runs of `'1'`.

Every block of consecutive `1`s contributes:

\[
\frac{k(k+1)}{2}
\]

(where `k` is the block length)

The final answer must be taken modulo \(10^9 + 7\).

---

## 🚀 Solution Idea

We scan the string once while maintaining a counter:

### ✔ If current char is `'1'`  
Increase `consecutive`.

### ✔ If it is `'0'`  
The streak of `'1'` ends — count its substrings:

\[
\text{add } \frac{consecutive(consecutive + 1)}{2}
\]

Then reset `consecutive = 0`.

### ✔ End of string  
We must also add the last streak.

Efficient and linear time.

---

## 🧠 Why This Works

For a block `"111"` of length 3:

- `"1"`
- `"1"`
- `"1"`
- `"11"`
- `"11"`
- `"111"`

Total:  
\[
3 + 2 + 1 = 6 = \frac{3 \cdot 4}{2}
\]

Summing over all blocks gives the total result.

---

## ⏱ Complexity

- **Time:** \(O(n)\)  
- **Space:** \(O(1)\)

Optimal for input size up to \(10^5\).