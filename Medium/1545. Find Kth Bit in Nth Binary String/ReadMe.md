# LeetCode 1545 - Find Kth Bit in Nth Binary String

## 🔗 Problem Link 
[LeetCode 1545 - Find Kth Bit in Nth Binary String](https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/)

## 🧠 Problem Description 

We are given a recursive binary string definition:

- `S1 = "0"`
- `Sn = Sn-1 + "1" + reverse(invert(Sn-1))`

Where `invert()` turns all `0`s into `1`s and vice versa, and `reverse()` reverses the string.

Given `n` and `k`, return the `k-th` bit of `Sn`.

## 🧪 Example

```python
Input: n = 3, k = 1
S1 = "0"
S2 = "011"
S3 = "0111001"
Output: "0"
```

## 💡 Approach

Recursively build `Sn` using the given rule.

`Sn = Sn-1 + "1" + reverse(invert(Sn-1))`

After full construction, return the (k-1)th character.

## 🧮 Complexity

**Time Complexity:** O(2^n)

**Space Complexity:** O(2^n)

⚠️ This is not the most efficient solution for large `n`, but works for small input ranges.

## 📌 Tags

`recursion`, `binary-strings`, `string-manipulation`, `divide-and-conquer`