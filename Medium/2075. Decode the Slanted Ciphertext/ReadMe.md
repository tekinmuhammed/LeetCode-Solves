# 2075. Decode the Slanted Ciphertext

**Difficulty:** Medium
**Problem Link:** [LeetCode 2075](https://leetcode.com/problems/decode-the-slanted-ciphertext/description/)

---

## Problem Description

A string `originalText` was encoded into a slanted cipher matrix with a specified number of `rows`. The matrix is filled row by row, and the original message is then read **diagonally** starting from the top-left.

Given the `encodedText` and the number of `rows`, return the decoded `originalText`.

**Note:** Trailing spaces added during the matrix filling should be removed, but spaces that were part of the original message must be preserved.

---

## Approach: Diagonal Matrix Traversal

The problem can be solved by visualizing the 1D string as a 2D matrix of size $rows \times cols$.

### Key Ideas:
1.  **Grid Dimensions:** We calculate the number of columns using the formula:  
    $$cols = \frac{len(encodedText)}{rows}$$
2.  **Diagonal Reading:** The original message starts at the top row (row 0). For every starting column `start_col` in the first row, we follow the diagonal:
    - Move from $(i, j)$ to $(i+1, j+1)$.
    - This continues until we hit the boundary of the matrix ($i = rows$ or $j = cols$).
3.  **Index Mapping:** Since the matrix is represented as a 1D string, the 2D coordinate $(i, j)$ maps to the 1D index:  
    $$index = i \times cols + j$$
4.  **Trimming:** The problem specifies that only the **trailing** spaces should be removed. Python's `.rstrip()` method is perfect for this as it preserves leading and middle spaces.



---

## Code

```python
class Solution(object):
    def decodeCiphertext(self, encodedText, rows):
        """
        :type encodedText: str
        :type rows: int
        :rtype: str
        """
        # If there is only one row, the encoded text is the original text
        if rows == 1:
            return encodedText
        
        n = len(encodedText)
        cols = n // rows
        
        res = []
        
        # Every diagonal starts from the first row (i = 0)
        for start_col in range(cols):
            i, j = 0, start_col
            
            # Follow the diagonal: (0, start_col) -> (1, start_col + 1) -> ...
            while i < rows and j < cols:
                # Convert 2D coordinates to 1D index
                res.append(encodedText[i * cols + j])
                i += 1
                j += 1
        
        # Join the characters and remove trailing spaces added for padding
        return "".join(res).rstrip()
```

---

## Example Walkthrough

**Input:** `encodedText = "ch   ie   pr", rows = 3`

1.  **Calculate Dimensions:** `n = 12`, `rows = 3` $\rightarrow$ `cols = 4`.
2.  **Matrix Visualization:**
    ```
    c h _ _
    _ i e _
    _ _ p r
    ```
3.  **Diagonals:**
    - Start at `j=0`: (0,0)='c', (1,1)='i', (2,2)='p' $\rightarrow$ "cip"
    - Start at `j=1`: (0,1)='h', (1,2)='e', (2,3)='r' $\rightarrow$ "her"
    - Start at `j=2`: (0,2)=' ', (1,3)=' ' $\rightarrow$ "  "
    - Start at `j=3`: (0,3)=' ' $\rightarrow$ " "
4.  **Result:** `"cipher   "`. After `.rstrip()`, we get `"cipher"`.

---

## Complexity Analysis

* **Time Complexity:** $O(N)$
    - We visit each character of the `encodedText` at most once during the diagonal traversal.
* **Space Complexity:** $O(N)$
    - We store the decoded characters in a list before joining them into the final string.

---

## Tags
`String`, `Matrix`, `Simulation`, `Diagonal-Traversal`