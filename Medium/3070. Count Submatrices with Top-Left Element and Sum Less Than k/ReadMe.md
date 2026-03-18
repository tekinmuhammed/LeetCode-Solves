# 3070. Count Submatrices with Top-Left Element and Sum Less Than k

**Difficulty:** Medium 
**Problem Link:** [LeetCode 3070](https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/description/)

---

## Problem Description

You are given a **0-indexed** integer matrix `grid` and an integer `k`.

Return the number of **submatrices** that contain the top-left element of the grid (i.e., `grid[0][0]`) and have a sum of elements less than or equal to `k`.

---

## Approach: 2D Prefix Sum (In-place)

Since every submatrix must include the top-left element `(0, 0)`, every valid submatrix is uniquely defined by its bottom-right corner `(i, j)`. The sum of such a submatrix is the **2D Prefix Sum** at position `(i, j)`.

### Key Ideas:
1.  **In-place Transformation:** Instead of creating a new matrix, we transform the input `grid` so that each cell `grid[i][j]` stores the sum of the rectangle from `(0, 0)` to `(i, j)`.
2.  **Inclusion-Exclusion Principle:** To calculate the sum at `(i, j)` efficiently:
    - Add the value above: `grid[i-1][j]`
    - Add the value to the left: `grid[i][j-1]`
    - Subtract the diagonal value (because it was added twice): `grid[i-1][j-1]`
    - The formula is: $S(i, j) = val(i, j) + S(i-1, j) + S(i, j-1) - S(i-1, j-1)$
3.  **Counting:** After calculating the prefix sum for a cell, we simply check if `grid[i][j] <= k`. If it is, we increment our result.



---

## Code

```python
class Solution(object):
    def countSubmatrices(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        res = 0
        
        # Step 1: Calculate 2D prefix sum in-place
        for i in range(m):
            for j in range(n):
                # Add sum of submatrix above
                if i > 0:
                    grid[i][j] += grid[i-1][j]
                
                # Add sum of submatrix to the left
                if j > 0:
                    grid[i][j] += grid[i][j-1]
                
                # Subtract the overlapping diagonal submatrix
                if i > 0 and j > 0:
                    grid[i][j] -= grid[i-1][j-1]
                
                # Step 2: Check the condition
                if grid[i][j] <= k:
                    res += 1
                else:
                    # Optimization: Since values are positive, 
                    # if grid[i][j] > k, larger submatrices in this row
                    # will also exceed k.
                    break 
        
        return res
```

---

## Example Walkthrough

**Input:** `grid = [[7,6,3],[6,6,1]], k = 18`

1.  **Cell (0,0):** Sum = 7. ($7 \le 18$) $\rightarrow$ `res = 1`
2.  **Cell (0,1):** Sum = 7 + 6 = 13. ($13 \le 18$) $\rightarrow$ `res = 2`
3.  **Cell (0,2):** Sum = 13 + 3 = 16. ($16 \le 18$) $\rightarrow$ `res = 3`
4.  **Cell (1,0):** Sum = 7 + 6 = 13. ($13 \le 18$) $\rightarrow$ `res = 4`
5.  **Cell (1,1):** Sum = 13 (left) + 13 (above) - 7 (diag) + 6 (curr) = 25. ($25 > 18$) $\rightarrow$ Stop row.

**Final Result:** `4`

---

## Complexity Analysis

* **Time Complexity:** $O(m \times n)$
    - We visit each cell in the matrix exactly once to calculate the sum and check the condition.
* **Space Complexity:** $O(1)$
    - The prefix sums are calculated in-place, modifying the original `grid` without using extra data structures.

---

## Tags
`Matrix`, `Prefix-Sum`, `Dynamic-Programming`, `Array`