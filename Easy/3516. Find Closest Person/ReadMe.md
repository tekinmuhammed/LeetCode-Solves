# 3516. Find Closest Person

**Difficulty:** Easy  
**Link:** [LeetCode 3516](https://leetcode.com/problems/find-closest-person/)

---

## Problem Description
You are given three integers `x`, `y`, and `z`:
- Person 1 is located at position `x`.  
- Person 2 is located at position `y`.  
- The target person is located at position `z`.  

Return:
- `1` if Person 1 is closer to the target.  
- `2` if Person 2 is closer to the target.  
- `0` if both are equally close.  

---

## Example

### Input:
```python
x = 1
y = 5
z = 2
```

### Output:
```python
1
```

###  Explanation:

- Distance from Person 1 to target = |1 - 2| = 1

- Distance from Person 2 to target = |5 - 2| = 3

- Person 1 is closer → return 1.

### Constraints

- -1000 <= x, y, z <= 1000

###  Approach

1. Compute distances:

- `dist1 = abs(x - z)`

- `dist2 = abs(y - z)`

2. Compare distances:

- If `dist1 < dist2` → return `1`.

- If `dist2 < dist1` → return `2`.

- If equal → return 0.

This is a **direct math comparison** problem.

### Time and Space Complexity

- **Time Complexity:** `O(1)` → Only constant-time arithmetic and comparisons.

- **Space Complexity:** `O(1)` → Only a few integer variables are used.

### Tags

`Math`, `Simulation`, `Comparison`, `Easy-Problem`

### Notes

- A very straightforward implementation.

- Useful for practicing absolute value and conditional checks.

- This problem is a good warm-up for beginners before attempting more complex geometry or distance-based problems.