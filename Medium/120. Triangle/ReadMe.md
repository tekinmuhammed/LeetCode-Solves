# 120. Triangle

## Problem Description
Given a triangle array, return the **minimum path sum** from top to bottom.  

At each step, you may move to either of the two adjacent numbers in the row below.

---

### Example 1
**Input:**  
```python
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
```

**Output:**  
```python
11
```

**Explanation:**  
The path is `2 → 3 → 5 → 1`, which sums up to `11`.

---

### Example 2
**Input:**  
```python
triangle = [[-10]]
```

**Output:**
```python  
-10
```

---

## Approach
This problem can be solved using **Dynamic Programming (DP)** with a **bottom-up** approach:

1. Start from the second-to-last row of the triangle.  
2. For each element, add the minimum of the two adjacent elements from the row below.  
   - Example:  
     ```
     triangle[row][col] += min(triangle[row+1][col], triangle[row+1][col+1])
     ```
3. Continue updating until the top row is reached.  
4. The top element (`triangle[0][0]`) will contain the minimum path sum.

---

## Complexity Analysis
- **Time Complexity:** `O(n^2)` where `n` is the number of rows in the triangle (we process each element once).  
- **Space Complexity:** `O(1)` since we update the triangle in-place without extra storage.  

---

## Code Implementation
```python
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # Start from the second-to-last row and move upward
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                triangle[row][col] += min(triangle[row + 1][col], triangle[row + 1][col + 1])

        return triangle[0][0]
```

### Tags

`LeetCode-Medium`