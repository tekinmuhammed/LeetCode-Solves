# 812. Largest Triangle Area

**Difficulty:** Easy  
**Link:** [LeetCode 812](https://leetcode.com/problems/largest-triangle-area/description/)

## Problem Description
You are given an array of points on the 2D plane. Each point is represented as `[x, y]`.  
Return the **largest area of a triangle** that can be formed by choosing any three points.

---

### Example 1
**Input:**  
```python
points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
```

**Output:**  
```python
2.0
```

**Explanation:**  
The largest triangle is formed by the points `(0,2)`, `(2,0)`, and `(0,0)` with an area of `2`.

---

### Example 2
**Input:**  
```python
points = [[1,0],[0,0],[0,1]]
```

**Output:**  
```python
0.5
```

---

## Approach
We use the **shoelace formula** (determinant method) to calculate the area of a triangle given 3 points `(x1, y1), (x2, y2), (x3, y3)`:

\[
Area = \frac{1}{2} \times |x1 \cdot y2 + x2 \cdot y3 + x3 \cdot y1 - y1 \cdot x2 - y2 \cdot x3 - y3 \cdot x1|
\]

### Steps:
1. Iterate over all possible combinations of 3 points using `itertools.combinations(points, 3)`.
2. For each triplet, calculate the triangle area using the shoelace formula.
3. Keep track of the maximum area found.
4. Return the maximum value.

---

## Complexity Analysis
- **Time Complexity:** `O(n^3)` because we check all possible triplets (`n choose 3`).  
- **Space Complexity:** `O(1)` since only a few variables are used.  

---

## Code Implementation
```python
import itertools

class Solution(object):
    def largestTriangleArea(self, points):
        def area(p, q, r):
            return 0.5 * abs(
                p[0]*q[1] + q[0]*r[1] + r[0]*p[1]
                - p[1]*q[0] - q[1]*r[0] - r[1]*p[0]
            )

        return max(area(*triangle) for triangle in itertools.combinations(points, 3))
```

### Tags

`LeetCode-Easy`