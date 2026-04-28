# 2033. Minimum Operations to Make a Uni-Value Grid 

**Difficulty:** Medium
**Problem Link:** [LeetCode 2033](https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/description/)

---

## Problem Description 

You are given a 2D integer `grid` of size `m x n` and an integer `x`. In one operation, you can **add** `x` to or **subtract** `x` from any element of the grid.

A **uni-value grid** is a grid where all the elements are equal.

Return the **minimum** number of operations to make the grid uni-value. If it is not possible, return `-1`.

---

## Approach: Median and Modular Arithmetic 

To solve this problem efficiently, we need to address two main conditions: whether it's possible to make the grid uni-value and, if so, which value minimizes the total operations.

### Key Ideas: 
1.  **Possibility Check (Modulo Logic):** For any two numbers $a$ and $b$ to be made equal by adding/subtracting $x$, their difference must be divisible by $x$. This is equivalent to saying $a \pmod x == b \pmod x$. If any element in the grid has a different remainder when divided by $x$ than the others, it's impossible to reach a uni-value state.
2.  **Optimality (The Median Property):** In statistics, the value $K$ that minimizes the sum of absolute differences $\sum |a_i - K|$ for a set of numbers is the **median** of that set. 
3.  **Calculation:** - Flatten the grid into a 1D array.
    - Sort the array to find the median.
    - Validate the modulo condition for all elements.
    - Sum the operations: $\frac{|a_i - \text{median}|}{x}$.



---

## Code 

```python
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        """
        :type grid: List[List[int]]
        :type x: int
        :rtype: int
        """
        # Step 1: Flatten the grid into a 1D array
        nums_array = []
        for row in grid:
            for num in row:
                nums_array.append(num)

        # Step 2: Sort the array to find the median
        nums_array.sort()

        length = len(nums_array)
        # The median minimizes the sum of absolute differences
        median = nums_array[length // 2]
        
        result = 0
        # Step 3: Iterate and calculate operations
        for number in nums_array:
            # If the gap between numbers isn't divisible by x, return -1
            if (number - median) % x != 0:
                return -1
            
            # Count operations needed to reach the median
            result += abs(median - number) // x

        return result
```

---

## Example Walkthrough

**Input:** `grid = [[2, 4], [6, 8]], x = 2`

1.  **Flattened & Sorted:** `[2, 4, 6, 8]`
2.  **Median:** `nums_array[4 // 2] = nums_array[2] = 6`
3.  **Modulo Check:**
    - `2 % 2 == 0`, `4 % 2 == 0`, `6 % 2 == 0`, `8 % 2 == 0`. (All match)
4.  **Operations:**
    - `|2 - 6| / 2 = 2`
    - `|4 - 6| / 2 = 1`
    - `|6 - 6| / 2 = 0`
    - `|8 - 6| / 2 = 1`
    - **Total:** `2 + 1 + 0 + 1 = 4`

**Output:** `4`

---

## Complexity Analysis

* **Time Complexity:** $O(MN \log(MN))$
    - Flattening the grid takes $O(MN)$.
    - Sorting the array of $MN$ elements takes $O(MN \log(MN))$.
    - The final pass takes $O(MN)$.
* **Space Complexity:** $O(MN)$
    - We store all grid elements in a separate list `nums_array`.

---

## Tags
`Math`, `Sorting`, `Matrix`, `Median`, `Greedy`