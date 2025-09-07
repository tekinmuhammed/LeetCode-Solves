# 1304. Find N Unique Integers Sum up to Zero

**Difficulty:** Easy  
**Link:** [LeetCode 1304](https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/)

---

## Problem Description
Given an integer `n`, return any array containing `n` **unique integers** such that their sum is equal to `0`.

---

## Example 1
**Input:**
```python
n = 5
```

**Output:**
```python
[-2, -1, 0, 1, 2]
```
---

## Example 2
**Input:**
```python
n = 3
```

**Output:**
```python
[-1, 0, 1]
```
---

## Example 3
**Input:**
```python
n = 1
```

**Output:**
```python
[0]
```
---

## Constraints
- `1 <= n <= 1000`

---

## Approach

### Key Idea
- Use symmetry around zero:
  - For every positive integer `i`, include its negative `-i`.
  - This ensures the sum cancels out.
- If `n` is odd, include `0` as the middle element.

### Algorithm
1. Initialize an empty result list.
2. For `i` from `1` to `n//2`:
   - Add both `i` and `-i` to the list.
3. If `n` is odd, append `0`.
4. Return the result.

---

## Time and Space Complexity
- **Time Complexity:** `O(n)` → we generate `n` numbers in a loop.  
- **Space Complexity:** `O(n)` → the output list contains `n` integers.

---

## Tags
Math, Constructive Algorithms, Array

---

## Notes
- Any valid permutation of the numbers is acceptable.  
- This approach guarantees uniqueness and correctness without needing extra checks.  