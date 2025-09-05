# 2749. Minimum Operations to Make the Integer Zero

**Difficulty:** Medium  
**Link:** [LeetCode 2749](https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero/)

---

## Problem Description
You are given two integers `num1` and `num2`.  

In one operation, you can choose any integer `i >= 0` and do:
```python
num1 = num1 - (num2 + 2^i)
```

Return the minimum number of operations required to make `num1 = 0`.  
If it is not possible, return `-1`.

---

## Example 1
**Input:**
```python
num1 = 3, num2 = -2
```

**Output:**
```python
3
```

**Explanation:**
We can pick i = 0, 1, 2 in three steps.

---

## Example 2
**Input:**
```python
num1 = 5, num2 = 7
```

**Output:**
```python
-1
```

**Explanation:**
No valid sequence of operations exists.

---

## Constraints
- `1 <= num1 <= 10^9`
- `-1000 <= num2 <= 1000`

---

## Approach

1. Iterate over possible number of operations `k` (from 1 to 60).  
2. Compute:
```python
target = num1 - k * num2
```
If `target < 0`, then impossible → return `-1`.  

3. Check conditions:
- `bin(target).count("1") <= k` (enough operations to cover all set bits).  
- `k <= target` (cannot have more operations than the value itself).  

4. If valid, return `k`.  
5. If no valid `k` found, return `-1`.

---

## Time and Space Complexity
- **Time Complexity:** O(60) → at most 60 iterations, each with constant work.  
- **Space Complexity:** O(1) → only uses a few integer variables.

---

## Tags
Greedy, Bit Manipulation, Binary Representation, Math

---

## Notes
- The key trick is using **`bin(x).count("1")`** to determine the minimum number of powers of two needed.  
- The `k ≤ target` condition ensures we do not assign more terms than available value.  
- The loop limit of 60 is safe since `2^60` exceeds `10^18`.