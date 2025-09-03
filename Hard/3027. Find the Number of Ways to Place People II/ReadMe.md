# 3027. Find the Number of Ways to Place People II

**Difficulty:** Medium  
**Link:** [LeetCode 3027](https://leetcode.com/problems/find-the-number-of-ways-to-place-people-ii/)

---

## Problem Description
You are given a list of 2D points, where each point represents a possible position.  
We want to count the number of valid pairs `(A, B)` such that:  

1. `A.x <= B.x` and `A.y >= B.y` (A is top-left, B is bottom-right).  
2. There is no third point strictly inside the rectangle defined by A and B.  

This is a follow-up to **3025. Find the Number of Ways to Place People I**, but with an optimized solution.

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

- (1,2) → (2,1) is valid.

- (3,3) → (2,1) is valid.

- (1,2) → (3,3) is invalid due to condition violation.

So the answer is `2`.

### Constraints

- 2 <= points.length <= 1000

- points[i].length == 2

- 0 <= points[i][0], points[i][1] <= 1000

### Approach
**Key Ideas:**

- Sort the points by `(x ascending, y descending)` to simplify pair validation.

- For each `pointA`, maintain bounds `(xMin, xMax, yMin, yMax)`.

- Iterate over possible `pointB` candidates and check if they fit within the valid region.

- If valid:

- - Increment the counter.

- - Update bounds to prevent illegal points from being considered later.

This reduces unnecessary checks compared to the brute-force approach in Problem I.

### Time and Space Complexity

- **Time Complexity:** `O(n²)` → Nested iteration over point pairs after sorting.

- **Space Complexity:** `O(1)` → Only variables for bounds and counter are used.

### Tags

`Sorting`, `Geometry`, `Greedy`, `Optimization`

### Notes

- Compared to Problem I (brute-force O(n³)), this solution is significantly faster.

- Sorting by `(x, -y)` ensures that potential candidates are always processed in a valid order.

- This is a good example of transforming a brute-force geometric problem into a more efficient solution using sorting and greedy bounds.