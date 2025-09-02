# 3025. Find the Number of Ways to Place People I

**Difficulty:** Medium  
**Link:** [LeetCode 3025](https://leetcode.com/problems/find-the-number-of-ways-to-place-people-i/)

---

## Problem Description
You are given a list of 2D points, where each point represents a possible position.  
We want to count the number of valid pairs `(A, B)` such that:  

1. `A.x <= B.x` and `A.y >= B.y` (A is top-left, B is bottom-right).  
2. There is no third point strictly inside the rectangle defined by A and B.  

Return the number of such valid pairs.

---

## Example

### Input:
```python
points = [[1,2],[2,1],[3,3]]
```

### Output:
```python
2
```

### Explanation:

- Pair (1,2) → (2,1) is valid (rectangle contains no extra point).

- Pair (1,2) → (3,3) is invalid (since condition A.y >= B.y is not met).

- Pair (3,3) → (2,1) is valid.

So the answer is `2`.

### Constraints

- 2 <= points.length <= 100

- points[i].length == 2

- 0 <= points[i][0], points[i][1] <= 100

### Approach
**Key Ideas:**

- Use brute-force to check all possible pairs `(i, j)`.

- For each pair, check:

- - If `A.x <= B.x` and `A.y >= B.y`.

- - If no other point lies inside the rectangle formed by A and B.

- If both conditions are satisfied, count the pair as valid.

### Time and Space Complexity

- **Time Complexity:** `O(n³)` → Iterating over all possible pairs (i, j) and checking against all other points.

- **Space Complexity:** `O(1)` → Only a few variables used.

### Tags

`Brute-Force`, `Geometry`, `Simulation`

### Notes

- This solution works correctly but is not optimized.

- For larger constraints, an efficient data structure (e.g., segment tree or sorting + sweep line) might be required.

- Since the constraints are small (n <= 100), the brute-force approach is acceptable.
