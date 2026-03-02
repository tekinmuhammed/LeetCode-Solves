# 1536. Minimum Swaps to Arrange a Binary Grid

**Difficulty:** Medium  
**Problem Link:** [LeetCode 1536](https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid/description/)

---

## Problem Description

Given an $n \times n$ binary `grid`, in one step you can choose two **adjacent rows** of the grid and swap them.

A grid is said to be **valid** if for each row $i$ (where $0 \le i < n$), there are at least $n - 1 - i$ trailing zeros.

Return the minimum number of steps to make the grid valid, or **-1** if the grid cannot be made valid.

---

## Approach

The core challenge is to satisfy the condition: **Row $i$ must have at least $n - 1 - i$ trailing zeros.**

### Key Ideas:
1.  **Simplification:** Instead of working with the whole matrix, we calculate the number of **trailing zeros** for each row and store them in a list (`trailing_zeros`).
2.  **Greedy Strategy:** * For each position $i$ in the grid, we need a row that has at least `target = n - 1 - i` zeros.
    * We search for the **first (nearest)** row $j$ (where $j \ge i$) that satisfies this condition.
    * Choosing the nearest row is optimal because it minimizes the number of adjacent swaps needed to bring that row to position $i$.
3.  **Simulation:** Once a valid row is found at index $j$, we "bubble" it up to index $i$. The number of swaps required is exactly $j - i$.
4.  **Edge Case:** If no row from $i$ to $n-1$ satisfies the target, it's impossible to fix the grid, so we return `-1`.

---

## Code

```python
class Solution(object):
    def minSwaps(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        
        # Calculate trailing zeros for each row
        trailing_zeros = []
        for row in grid:
            count = 0
            for i in range(n - 1, -1, -1):
                if row[i] == 0:
                    count += 1
                else:
                    break
            trailing_zeros.append(count)
        
        res = 0
        for i in range(n):
            # Target zeros for row i is (n - 1 - i)
            target = n - 1 - i
            
            # Find the nearest row that satisfies the target
            found = -1
            for j in range(i, n):
                if trailing_zeros[j] >= target:
                    found = j
                    break
            
            # If no valid row is found, return -1
            if found == -1:
                return -1
            
            # Simulate swaps: add the distance to result
            res += (found - i)
            
            # Move the found row to the current position i
            val = trailing_zeros.pop(found)
            trailing_zeros.insert(i, val)
            
        return res
```

---

## Example Walkthrough

**Input:** `grid = [[0,0,1],[1,1,0],[1,0,0]]` ($n=3$)

1.  **Calculate Trailing Zeros:**
    * Row 0: `[0,0,1]` -> 0 zeros
    * Row 1: `[1,1,0]` -> 1 zero
    * Row 2: `[1,0,0]` -> 2 zeros
    * `trailing_zeros = [0, 1, 2]`

2.  **Iteration $i = 0$:** (Target: $3-1-0 = 2$ zeros)
    * `trailing_zeros[2]` (2) $\ge$ 2. Found at $j=2$.
    * Swaps: `res += (2 - 0) = 2`.
    * Update list: `[2, 0, 1]`

3.  **Iteration $i = 1$:** (Target: $3-1-1 = 1$ zero)
    * `trailing_zeros[2]` (1) $\ge$ 1. Found at $j=2$.
    * Swaps: `res += (2 - 1) = 3`.
    * Update list: `[2, 1, 0]`

4.  **Final Result:** `3`

---

## Complexity Analysis

* **Time Complexity:** $O(n^2)$
    * Calculating trailing zeros: $O(n^2)$.
    * Searching and moving rows: $O(n^2)$.
* **Space Complexity:** $O(n)$
    * Storing the count of trailing zeros for $n$ rows.

---

## Tags
Greedy, Matrix, Array, Simulation