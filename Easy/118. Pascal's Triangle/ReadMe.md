# 118. Pascal's Triangle

**Difficulty:** Easy  
**Problem Link:** [LeetCode 118](https://leetcode.com/problems/pascals-triangle/)

---

## Problem Description

Given an integer `numRows`, generate the first `numRows` of **Pascal's Triangle**.

In Pascal's Triangle:
- Each number is the sum of the two numbers directly above it.
- The triangle starts with a single 1 at the top.

---

### Example

**Input:**
```python
numRows = 5
```

**Output:**
```python
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
```

### Approach

- Initialize an empty list `result` to store all rows.

- For each row `i` from `0` to `numRows - 1`:

- - Start the row with all `1s: [1] * (i + 1)`

- - For indices `j` from `1` to `i - 1`, compute the value using the two values above:

- - - `row[j] = result[i - 1][j - 1] + result[i - 1][j]`

- Append the completed row to `result`.

### Complexity

- **Time Complexity:** `O(n²)`
We compute up to `n` rows and each row has up to `n` elements.

- **Space Complexity:** `O(n²)`
Final output is a list of lists with `n(n+1)/2` integers in total.

### Tags

`Array`, `Dynamic-Programming`, `Math`

### Notes

- Pascal's Triangle is a classic problem for learning 2D list construction.

- Useful in binomial expansions: row `i` corresponds to coefficients of `(a + b)^i`.