# 3201. Find the Maximum Length of Valid Subsequence I

**Difficulty:** Easy  
**Link:** [LeetCode 3201](https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i)

---

## Problem Description

You are given an array of integers `nums`. You need to find the **maximum length** of a **valid subsequence** based on the following condition:

A valid subsequence is one of:
1. A subsequence of only **even** numbers.
2. A subsequence of only **odd** numbers.
3. A subsequence where the parity **alternates starting with odd**.
4. A subsequence where the parity **alternates starting with even**.

Return the length of the **longest** such valid subsequence.

---

## Example

### Input
```python
nums = [1, 3, 5, 6, 4, 2]
```

### Output
```python
4
```

### Explanation

- Subsequence `[1, 6, 4, 2]` is alternating starting with odd → valid of length 4.

### Approach & Explanation

We evaluate all four valid subsequence types:

1. **All Evens:** Traverse and count even numbers.

2. **All Odds:** Traverse and count odd numbers.

3. **Alternating Starting with Odd:** Traverse and add elements if current parity matches the expected one (`odd → even → odd → ...`).

4. **Alternating Starting with Even:** Similar to above, but starts with even.

At each stage, we update `mx`, the max length encountered.

### Time and Space Complexity

- **Time Complexity:** `O(n)`
→ We scan the list 4 times, each in O(n).

- **Space Complexity:** `O(1)`
→ No extra data structures are used.

### Tags

`Greedy`, `Subsequence`, `Even/Odd`, `Two-Pointers`, `Simulation`

### Summary

Bu problem, temel kontrol yapılarıyla ardışık koşullara göre alt dizi seçimi pratiği sunar.
Çözüm stratejisi, dört farklı geçerli subsequence tipini ayrı ayrı test etmeye dayanır.