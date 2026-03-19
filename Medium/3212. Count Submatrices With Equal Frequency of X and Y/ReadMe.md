# 3212. Count Submatrices With Equal Frequency of X and Y

**Difficulty:** Medium  
**Problem Link:** [LeetCode 3212](https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y/description/)

---

## Problem Description

Given a 2D character matrix `grid`, return the number of **submatrices** that:
1. Contain the top-left element `grid[0][0]`.
2. Have an **equal frequency** of characters `'X'` and `'Y'`.
3. Contain **at least one** character `'X'`.

---

## Approach: Dual 2D Prefix Sums

Since all submatrices must start at `(0, 0)`, we can represent any valid submatrix by its bottom-right corner `(i, j)`. To solve this efficiently, we use the **2D Prefix Sum** technique to keep track of two things simultaneously.

### Key Ideas:
1.  **Frequency Balance (`diff`):**
    - We assign a value of `1` to `'X'`, `-1` to `'Y'`, and `0` to any other character (like `'.'`).
    - The sum of these values in a submatrix starting from `(0, 0)` tells us the balance. If the sum is **0**, then the number of `'X'`s equals the number of `'Y'`s.
2.  **Requirement Check (`countX`):**
    - We need to ensure at least one `'X'` is present. We maintain a second 2D prefix sum table that counts the occurrences of `'X'`.
3.  **Efficient Calculation:**
    - Both tables are populated in a single pass using the Inclusion-Exclusion Principle:
      $$S(i, j) = val(i, j) + S(i-1, j) + S(i, j-1) - S(i-1, j-1)$$
4.  **Final Count:**
    - A submatrix ending at `(i, j)` is valid if `diff[i][j] == 0` and `countX[i][j] > 0`.

---

## Code

```python
class Solution(object):
    def numberOfSubmatrices(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        
        # diff[i][j] stores (count of X - count of Y) in submatrix (0,0) to (i,j)
        diff = [[0]*n for _ in range(m)]
        # countX[i][j] stores total count of 'X' in submatrix (0,0) to (i,j)
        countX = [[0]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                # Determine value for diff balance
                val = 0
                if grid[i][j] == 'X':
                    val = 1
                elif grid[i][j] == 'Y':
                    val = -1
                
                diff[i][j] = val
                countX[i][j] = 1 if grid[i][j] == 'X' else 0
                
                # Apply 2D prefix sum logic
                if i > 0:
                    diff[i][j] += diff[i-1][j]
                    countX[i][j] += countX[i-1][j]
                if j > 0:
                    diff[i][j] += diff[i][j-1]
                    countX[i][j] += countX[i][j-1]
                if i > 0 and j > 0:
                    diff[i][j] -= diff[i-1][j-1]
                    countX[i][j] -= countX[i-1][j-1]
        
        res = 0
        # Iterate through all submatrices anchored at (0,0)
        for i in range(m):
            for j in range(n):
                # Condition: Equal X and Y (diff == 0) and at least one X
                if diff[i][j] == 0 and countX[i][j] > 0:
                    res += 1
        
        return res
```

---

## Example Walkthrough

**Input:**
```
grid = [["X","Y","."],
        ["Y",".","."]]
```

1.  **At (0,0):** `grid[0][0] = 'X'`. `diff = 1`, `countX = 1`. (Balance $\neq 0$)
2.  **At (0,1):** `grid[0][1] = 'Y'`. `diff = 1 + (-1) = 0`, `countX = 1`. 
    - **Valid Submatrix!** (Balance is 0, has at least one X).
3.  **At (1,1):** Submatrix includes `X`, `Y`, `Y`, `.`. `diff = 1 - 1 - 1 = -1`. (Balance $\neq 0$)

---

## Complexity Analysis

* **Time Complexity:** $O(m \times n)$
    - We traverse the matrix to build the prefix sum tables and once more to count the results.
* **Space Complexity:** $O(m \times n)$
    - We use two additional 2D arrays (`diff` and `countX`) to store the prefix sums.

---

## Tags
`Matrix`, `Prefix-Sum`, `String`, `Counting`, `Array`