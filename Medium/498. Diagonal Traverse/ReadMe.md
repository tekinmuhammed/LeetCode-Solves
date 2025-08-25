# 498. Diagonal Traverse  

**Difficulty:** Medium  
**Link:** [LeetCode 498](https://leetcode.com/problems/diagonal-traverse/)  

---

## Problem Description  

Given an `m x n` matrix `mat`, return all elements of the matrix in **diagonal order**.  

The traversal alternates between moving **up-right** and **down-left** until all elements are visited.  

---

## Example  

### Input:  
```python
mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]
```

### Output:
```python
[1,2,4,7,5,3,6,8,9]
```

### Constraints

- `1 <= m, n <= 10^4`

- `1 <= m * n <= 10^4`

- `-10^5 <= mat[i][j] <= 10^5`

### Approach
**Key Ideas:**

- Use a **simulation approach**.

- Start from the top-left element `(0,0)`.

- Maintain a **direction flag**:

- - `1` → moving **up-right**

- - `-1` → moving **down-left**

- At each step:

- - Append the current element to the result.

- - Update `(row, col)` depending on the direction.

- -  Handle **boundary conditions** (hitting the top, bottom, left, or right edge).

- - Flip direction when needed.

### Time and Space Complexity

- **Time Complexity:** `O(m * n)` — each element is visited exactly once.

- **Space Complexity:** `O(1)` extra space (excluding the result array).

### Tags

`Matrix`, `Simulation`, `Array`

### Notes

- The key challenge is correctly handling **edge cases** when hitting matrix boundaries.

- Alternative approach: group elements by the sum of their indices (`i + j`) and traverse diagonals accordingly.