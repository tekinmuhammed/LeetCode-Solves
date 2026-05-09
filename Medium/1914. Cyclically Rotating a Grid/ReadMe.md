# 1914. Cyclically Rotating a Grid

**Difficulty:** Medium 
**Problem Link:** [LeetCode 1914](https://leetcode.com/problems/cyclically-rotating-a-grid/description/)

---

## Problem 
You are given an `m x n` integer matrix `grid` and an integer `k`. You need to cyclically rotate the grid counter-clockwise by `k` steps.

A cyclic rotation means shifting the elements of each concentric layer of the grid. 

Return the matrix `grid` after applying the `k` steps of cyclic rotation to it.

---

# Approach 

The problem asks us to rotate concentric layers of a matrix. Rotating a 2D perimeter is difficult to manage in-place with coordinate math, but if we "unroll" the perimeter into a 1D array, the problem reduces to a simple array rotation.

Steps:

1. **Count the Layers:** A grid of size `m x n` has `min(m // 2, n // 2)` concentric layers.
2. **Extract Each Layer:** For each layer, we traverse its perimeter in a **counter-clockwise** direction (Left edge -> Bottom edge -> Right edge -> Top edge). As we traverse, we record three things:
   * The row index (`r`)
   * The column index (`c`)
   * The actual value (`val`)
3. **Optimize the Rotation:** A layer with `total` elements repeating a rotation `total` times results in the exact same layer. Therefore, rotating `k` times is mathematically equivalent to rotating `k % total` times. This modulo operation prevents Time Limit Exceeded (TLE) errors for massive values of `k`.
4. **Reassign Values:** We iterate through the coordinates we saved. For a position at index `i` in our unrolled layer, its new value after a counter-clockwise shift of `kk` will come from the index `(i + total - kk) % total` of the `val` array. 
5. **Update and Return:** Write the newly calculated values back into the `grid` using the saved `r` and `c` coordinates.

---

# Example Walkthrough 

Consider a single layer (a 1D array representation of the perimeter):
`val = [1, 2, 3, 4, 5, 6]` (Length `total = 6`)
`k = 2`

We want to rotate it counter-clockwise. This means elements move "forward" in our traversal path, or alternatively, the element that lands at index `i` comes from `kk` steps "behind" it.

* `kk = 2 % 6 = 2`
* For index `0`: New value comes from `(0 + 6 - 2) % 6 = 4`. `val[4]` is `5`.
* For index `1`: New value comes from `(1 + 6 - 2) % 6 = 5`. `val[5]` is `6`.
* For index `2`: New value comes from `(2 + 6 - 2) % 6 = 0`. `val[0]` is `1`.

The newly formed layer `[5, 6, 1, 2, 3, 4]` is then mapped back to the 2D grid coordinates.
 
---

# Complexity Analysis 

Time Complexity

O(m * n)

We process each element of the `m x n` grid exactly twice: once when extracting it into the 1D arrays, and once when writing the rotated value back into the grid. The modulo calculation takes O(1) time. Thus, the overall time scales linearly with the number of elements in the grid.

Space Complexity

O(m + n)

We process the grid layer by layer. The auxiliary space used (`r`, `c`, and `val` arrays) only needs to hold the perimeter of the current layer. The outermost layer has the largest perimeter, which is roughly `2m + 2n`. Therefore, the space complexity is bounded by O(m + n).

---
 
# Code 

```python
class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        nlayer = min(m // 2, n // 2)  # level count 
        
        # enumerate each layer counterclockwise starting from the top-left corner 
        for layer in range(nlayer):
            r = []  # row index of each element 
            c = []  # column index of each element 
            val = []  # value of each element 
            
            for i in range(layer, m - layer - 1):  # left 
                r.append(i)
                c.append(layer)
                val.append(grid[i][layer])
                
            for j in range(layer, n - layer - 1):  # down 
                r.append(m - layer - 1)
                c.append(j)
                val.append(grid[m - layer - 1][j])
                
            for i in range(m - layer - 1, layer, -1):  # right 
                r.append(i)
                c.append(n - layer - 1)
                val.append(grid[i][n - layer - 1])
                
            for j in range(n - layer - 1, layer, -1):  # up 
                r.append(layer)
                c.append(j)
                val.append(grid[layer][j])
                
            total = len(val)  # total number of elements in each layer 
            kk = k % total  # equivalent number of rotations 
            
            # find the value at each index after rotation 
            for i in range(total):
                idx = (
                    i + total - kk
                ) % total  # the index corresponding to the value after rotation 
                grid[r[i]][c[i]] = val[idx]
                
        return grid
```