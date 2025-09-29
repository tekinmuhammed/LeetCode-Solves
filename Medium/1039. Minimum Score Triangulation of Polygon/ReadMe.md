# 1039. Minimum Score Triangulation of Polygon  

**Difficulty:** Medium
**Link:** [LeetCode 812](https://leetcode.com/problems/minimum-score-triangulation-of-polygon/description/)

## Problem Description  
We are given a convex polygon with `n` vertices labeled in order and an array `values` where `values[i]` represents the value of the `i`-th vertex.  
The task is to **triangulate the polygon** (divide it into triangles without adding new points, only connecting existing vertices) in such a way that the **sum of the scores of the triangles is minimized**.  

The score of a triangle with vertices `(i, j, k)` is computed as:  

\[
\text{score}(i, j, k) = values[i] \times values[j] \times values[k]
\]

We need to return the **minimum possible score** after triangulating the polygon.  

---

## Approach  

This problem is a **Dynamic Programming (DP on intervals)** problem.  
- A polygon with `n` vertices can be recursively broken into sub-polygons.  
- For each interval `[i, j]` (sub-polygon), we try to pick a middle vertex `k` (`i < k < j`) and compute:  

\[
dp[i][j] = \min_{i < k < j} \big( dp[i][k] + dp[k][j] + values[i] \times values[j] \times values[k] \big)
\]

### Steps:
1. Initialize a `dp` table of size `n x n` with zeros.  
2. Iterate over increasing polygon lengths (`length = 3 ... n`).  
3. For each interval `[i, j]`, compute the minimum score by checking all possible partitions (`k`).  
4. The answer will be stored in `dp[0][n-1]`, representing the minimum triangulation score of the entire polygon.  

---

## Code Implementation  

```python
class Solution(object):
    def minScoreTriangulation(self, values):
        """
        :type values: List[int]
        :rtype: int
        """
        n = len(values)
        dp = [[0] * n for _ in range(n)]
        
        # Polygon length starts from 3 upwards
        for length in range(3, n+1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = float("inf")
                for k in range(i+1, j):
                    dp[i][j] = min(
                        dp[i][j],
                        dp[i][k] + dp[k][j] + values[i]*values[j]*values[k]
                    )
        
        return dp[0][n-1]
```

### Complexity Analysis
- **Time Complexity:**

- - `𝑂(𝑛3)`, since for each interval `[i, j]`, we check all possible `k`.

- **Space Complexity:**
- - `𝑂(𝑛2)` for the DP table.

### Example
**Input:**
```python
values = [1, 3, 1, 4, 1, 5]
```

**Output:**
```python
13
```

**Explanation:**

The optimal triangulation produces triangles with minimum score sum = `13`.