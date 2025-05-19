# 🟨 LeetCode 1829 - Maximum XOR for Each Query

**Difficulty:** Medium  
**Problem Link:** [LeetCode 1829](https://leetcode.com/problems/maximum-xor-for-each-query/)

---

## 📘 Problem Description

- You are given an integer array `nums` and an integer `maximumBit`. 

- For every `i` from 0 to `nums.length - 1`, define `prefix[i]` as the XOR of `nums[0] to nums[i]`.

- Also define `k[i]` as the integer such that:
`prefix[i] XOR k[i] = maximum possible value with maximumBit bits.`

- Return an array of `k` values, where the `i-th` element is the result for the array `nums[0...n-1-i]`.

---

## 🧪 Example

### Input:
```cpp
nums = [0,1,1,3]
maximumBit = 2
```

## Output:
```cpp

[0,3,2,3]
```

## 🚀 Approach
- First, compute the cumulative XOR of the whole array.

- The maximum number that can be represented with `maximumBit` bits is `2^maximumBit - 1` → this will be our XOR mask.

- For each query (from last to first), find the number `k` such that `prefix[i] XOR k = mask`, so `k = prefix[i] ^ mask`.

- After each query, remove the effect of the last number by XORing it out from the cumulative XOR.

## ⏱️ Complexity
- **Time Complexity:** O(n)

- **Space Complexity:** O(n)

## 🏷️ Tags
`bit-manipulation`, `prefix-xor`, `leetcode-medium`

## 📝 Notes
- Knowing that `x ^ k = max` implies `k = x ^ max` is key to solving this problem.

- Reverse simulation (from end to start) is used to efficiently compute each answer.