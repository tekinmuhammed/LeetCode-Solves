# 3234. Count the Number of Substrings With Dominant Ones — README

**Difficulty:** Medium  
**Problem Link:** [LeetCode 3234](https://leetcode.com/problems/count-the-number-of-substrings-with-dominant-ones/description/)

## 📌 Problem Summary
Given a binary string `s`, count how many substrings satisfy:

\[
\text{#ones} \ge (\text{#zeros})^2
\]

A substring is **dominant** if the number of `1`s is at least the square of the number of `0`s.

`n` can be up to **100,000**, so an \(O(n^2)\) brute force is impossible.

---

## 🚀 High-Level Idea

### ✔ Key Insight
If a substring contains `N0` zeros, then:

\[
N1 \ge N0^2
\]

But since:

- `N1 ≤ n`
- `N0²` grows rapidly

We only need to consider:

- **Case 1:** `N0 = 0`
- **Case 2:** `1 ≤ N0 ≤ B`, where  
  \[
  B = \lfloor \sqrt{n} \rfloor + 1
  \]

If `N0 > B`, then `N0² > n`, thus impossible to satisfy.

---

## 🧠 Detailed Strategy

### **1. Substrings with no zeros (N0 = 0)**
For a contiguous block of `k` ones:

\[
\frac{k(k+1)}{2}
\]

valid substrings exist.

Summing over all such blocks gives the total for this case.

---

### **2. Substrings with 1 ≤ N0 ≤ B**
Let `zero_indices[k]` be the index of the k-th zero.

We consider windows from the i-th zero to the j-th zero:

- Number of zeros:
  \[
  k = j - i + 1
  \]

- Core segment:  
  from `p_start = zero_indices[i]`  
  to `p_end = zero_indices[j]`

- Ones inside core:
  \[
  N1_{\text{core}} = (p\_end - p\_start + 1) - k
  \]

- Additional ones required:
  \[
  N1_{\text{needed}} = k^2 - N1_{\text{core}}
  \]

- Available ones:
  - Before core (`max_prefix_ones`)
  - After core (`max_suffix_ones`)

We count all `(prefix, suffix)` combinations satisfying:

\[
\text{prefix} + \text{suffix} \ge N1_{\text{needed}}
\]

Your implementation correctly uses bounded loops and arithmetic counting.

---

## ⏱ Complexity

**Time Complexity:**  
\[
O(n \sqrt{n})
\]

**Space Complexity:**  
\[
O(n)
\]

---

## ✅ Final Evaluation
The solution is:

- Optimal ✔  
- Editorial-level ✔  
- Efficient for n = 100,000 ✔  
- Mathematically correct ✔  

One of the hardest counting problems — your solution handles it excellently.