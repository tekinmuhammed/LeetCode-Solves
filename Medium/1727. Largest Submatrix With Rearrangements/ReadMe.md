# 1727. Largest Submatrix With Rearrangements

**Difficulty:** Medium  
**Problem Link:** [LeetCode 1727](https://leetcode.com/problems/largest-submatrix-with-rearrangements/)

---

## Problem Description

You are given a binary matrix `matrix` of size $m \times n$. You are allowed to **rearrange the columns** of the matrix in any order.

Return the area of the **largest submatrix** within `matrix` where every element of the submatrix is `1` after reordering the columns optimally.

---

## Approach: Height Calculation and Sorting

The core idea is to treat each row as the base of a potential rectangle. Since we can rearrange columns, we don't care about their original horizontal positions—only their heights.

### Key Ideas:
1.  **Height Pre-calculation:** We iterate through the matrix from top to bottom. For each cell `(i, j)`, if `matrix[i][j] == 1`, we update its value to be the number of consecutive 1s ending at that cell (including itself).
    - If `matrix[i][j] == 1`, then `matrix[i][j] = matrix[i-1][j] + 1`.
    - This transforms each row into a representation of "column heights" available at that row.
2.  **Greedy Rearrangement:** For each row, we want to pick the tallest columns and put them side-by-side to form the widest possible rectangle.
    - We take all heights in the current row and sort them in **descending order**.
3.  **Area Calculation:** After sorting, for a height at index `j` (let's call it $h$), we can form a rectangle of height $h$ and width $j+1$.
    - $Area = h \times (j + 1)$
4.  **Global Maximum:** We keep track of the maximum area found across all rows.



---

## Code

```python
class Solution(object):
    def largestSubmatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        
        # Step 1: Pre-calculate the height of consecutive 1s for each column
        # We start from the second row (index 1)
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i-1][j]
        
        res = 0
        
        # Step 2: For each row, sort heights to find the best submatrix
        for i in range(m):
            # Sorting the heights in descending order to greedily find max area
            row = sorted(matrix[i], reverse=True)
            
            for j in range(n):
                # height = row[j], width = j + 1
                current_area = row[j] * (j + 1)
                res = max(res, current_area)
        
        return res
```

---

## Example Walkthrough

**Input:**
```
matrix = [[0,0,1],
          [1,1,1],
          [1,0,1]]
```

1.  **Heights Calculation:**
    - Row 0: `[0, 0, 1]`
    - Row 1: `[1, 1, 2]` (1s added to Row 0)
    - Row 2: `[2, 0, 3]` (1s added to Row 1)

2.  **Processing Row 2 (`[2, 0, 3]`):**
    - Sorted row: `[3, 2, 0]`
    - Width 1: $3 \times 1 = 3$
    - Width 2: $2 \times 2 = 4$
    - Width 3: $0 \times 3 = 0$
    - **Max Area at this row: 4**

**Result:** `4`

---

## Complexity Analysis

* **Time Complexity:** $O(m \cdot n \log n)$
    - We traverse the matrix to update heights: $O(m \cdot n)$.
    - For each of the $m$ rows, we perform a sort: $O(m \cdot n \log n)$.
* **Space Complexity:** $O(1)$ or $O(m \cdot n)$
    - If we are allowed to modify the input `matrix` in-place, the extra space is $O(1)$ (excluding the sorting overhead).

---

## Tags
Matrix, Greedy, Sorting, Dynamic-Programming