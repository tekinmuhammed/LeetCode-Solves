# 📝 LeetCode 326. Power of Three
**Difficulty:** Easy  
**Problem Link:** [LeetCode 326](https://leetcode.com/problems/power-of-three/description/)

---

## Problem Description
Given an integer `n`, determine whether it is a power of three.  
In other words, return `True` if there exists an integer `x` such that:
n == 3^x

Otherwise, return `False`.

**Example 1:**
Input: n = 27
Output: True
Explanation: 27 = 3^3

**Example 2:**
Input: n = 0
Output: False
Explanation: 0 cannot be expressed as a power of three.

**Example 3:**
Input: n = 9
Output: True
Explanation: 9 = 3^2

**Example 4:**
Input: n = 45
Output: False

---

## Approach

### 1. Check for non-positive numbers
- If `n <= 0`, it cannot be a power of three, so we immediately return `False`.

### 2. Iterative division
- While `n` is divisible by `3` (i.e., `n % 3 == 0`), we divide it by `3`.
- This process continues until:
  - We reach `1` (meaning `n` was exactly a power of three).
  - Or we find that `n` is no longer divisible by `3` (meaning it’s not a power of three).

### 3. Final check
- If after division the result is `1`, then `n` was a power of three.

---

## Time and Space Complexity
- **Time Complexity:** `O(log₃ n)` — We divide `n` by `3` repeatedly until it becomes `1`.
- **Space Complexity:** `O(1)` — We use only constant extra space.

---

## Alternative Approaches
1. **Mathematical check using logarithms**
   - We can check if `log₃(n)` is an integer, but due to floating-point precision errors, the iterative division method is safer.
   
2. **Precomputation**
   - Since `3^19` is the largest power of three that fits in a 32-bit signed integer, we can precompute all such values and check membership in a set.

---