# 1582. Special Positions in a Binary Matrix

**Difficulty:** Easy  
**Problem Link:** [LeetCode 1582](https://leetcode.com/problems/special-positions-in-a-binary-matrix/description/)

---

## Problem Description

Given an $m \times n$ binary matrix `mat`, return the number of **special positions** in the matrix.

A position `(i, j)` is called **special** if `mat[i][j] == 1` and all other elements in row `i` and column `j` are `0` (rows and columns are 0-indexed).



---

## Approach

The brute-force way would be to check every `1` we find and then scan its entire row and column. However, that would be inefficient. Instead, we use a **two-pass frequency counting** approach.

### Key Ideas:
1.  **Pre-calculation:** We need to know how many `1`s exist in each row and each column.
2.  **First Pass:** Traverse the entire matrix once to populate two auxiliary arrays:
    - `row_sum[i]`: Stores the number of `1`s in the $i^{th}$ row.
    - `col_sum[j]`: Stores the number of `1`s in the $j^{th}$ column.
3.  **Second Pass:** Traverse the matrix again. For each position `(i, j)`, it is **special** if and only if:
    - `mat[i][j] == 1`
    - `row_sum[i] == 1` (It's the only one in its row)
    - `col_sum[j] == 1` (It's the only one in its column)

---

## Code

```python
class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        m = len(mat)
        n = len(mat[0])
        
        # Auxiliary arrays to store the count of 1s
        row_sum = [0] * m
        col_sum = [0] * n
        
        # First Pass: Count 1s in each row and column
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    row_sum[i] += 1
                    col_sum[j] += 1
        
        count = 0
        
        # Second Pass: Identify special positions
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    # Check if this 1 is unique in its row and column
                    if row_sum[i] == 1 and col_sum[j] == 1:
                        count += 1
        
        return count
```

---

## Example Walkthrough

**Input:** `mat = [[1,0,0],[0,0,1],[1,0,0]]`

1.  **First Pass (Counting):**
    - `row_sum` becomes `[1, 1, 1]` (Each row has one '1')
    - `col_sum` becomes `[2, 0, 1]` (Column 0 has two '1's, Column 2 has one '1')

2.  **Second Pass (Checking):**
    - `mat[0][0] == 1`: `row_sum[0]` is 1, but `col_sum[0]` is 2. **Not Special.**
    - `mat[1][2] == 1`: `row_sum[1]` is 1, and `col_sum[2]` is 1. **Special!** (Count = 1)
    - `mat[2][0] == 1`: `row_sum[2]` is 1, but `col_sum[0]` is 2. **Not Special.**

**Output:** `1`

---

## Complexity Analysis

* **Time Complexity:** $O(m \times n)$
    - We traverse the matrix twice ($2 \times m \times n$), which simplifies to $O(m \times n)$.
* **Space Complexity:** $O(m + n)$
    - We use two additional arrays to store the sums of rows ($m$) and columns ($n$).

---

## Tags
`Array`, `Matrix`, `Hash-Table`, `Pre-computation`