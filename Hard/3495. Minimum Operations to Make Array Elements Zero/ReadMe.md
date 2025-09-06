# 3495. Minimum Operations to Make Array Elements Zero

**Difficulty:** Hard  
**Link:** [LeetCode 3495](https://leetcode.com/problems/minimum-operations-to-make-array-elements-zero/)

---

## Problem Description
You are given a list of queries, where each query is of the form `[L, R]`.  
For each query, you need to determine the **minimum number of operations** required to make all elements in the range `[L, R]` equal to zero.  

Return the total number of operations for all queries.

---

## Example 1
**Input:**
```python
queries = [[1, 3]]
```

**Output:**
```python
2
```

---

## Example 2
**Input:**
```python
queries = [[2, 5], [1, 7]]
```

**Output:**
```python
7
```

---

## Constraints
- `1 <= queries.length <= 10^5`
- `1 <= queries[i][0] <= queries[i][1] <= 10^9`

---

## Approach

### Key Idea
- Define a helper function `get(num)` that computes the cumulative number of operations needed from `1` up to `num`.
- This function works in **levels of powers of 2**:
  - At each step, multiply the contribution `(i+1)//2` with the range size `(min(base*2 - 1, num) - base + 1)`.
  - Increase the base by powers of two (`base *= 2`).
- To compute the result for a query `[L, R]`:
```python
(get(R) - get(L-1) + 1) // 2
```
This effectively counts the minimal number of operations for the range.

### Algorithm
1. Initialize `res = 0`.
2. For each query `[L, R]`:
 - Compute the difference using `get(R)` and `get(L-1)`.
 - Accumulate the result into `res`.
3. Return the total result.

---

## Time and Space Complexity
- **Time Complexity:**  
- Each `get(num)` runs in `O(log num)` due to doubling of `base`.  
- Each query therefore takes `O(log R)`.  
- For `q` queries, complexity = `O(q log M)` where `M` is the maximum value in queries.
- **Space Complexity:** `O(1)` (only counters and a few variables).

---

## Tags
Math, Prefix Sum, Binary Representation, Greedy

---

## Notes
- The formula cleverly avoids simulating operations element by element, which would be too slow for `10^9`.  
- By working in powers of two, the algorithm efficiently captures the required transformation counts.