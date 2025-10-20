# 611. Valid Triangle Number

**Difficulty:** Medium
**Link:** [LeetCode 611](https://leetcode.com/problems/valid-triangle-number/description/)  

## Problem Description
Given an integer array `nums`, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

---

### Example 1
**Input:**  
```python
nums = [2,2,3,4]
```

**Output:**  
```python
3
```

**Explanation:**  
Valid combinations are:  
- `(2, 3, 4)`  
- `(2, 3, 4)` (the two different `2`s)  
- `(2, 2, 3)`

---

### Example 2
**Input:**  
```python
nums = [4,2,3,4]
```

**Output:**  
```python
4
```

---

## Approach
This problem uses the **triangle inequality rule**:  
For any triangle sides `a, b, c` (where `a ≤ b ≤ c`), a triangle is valid if:  
```python
a + b > c
```

### Steps:
1. Sort the array `nums`.  
2. Fix the largest side `c = nums[k]`.  
3. Use two pointers (`i` starting at `0`, `j` starting at `k-1`) to find valid pairs `(nums[i], nums[j])`.  
   - If `nums[i] + nums[j] > nums[k]`, then all pairs between `i` and `j` are valid. Count them as `(j - i)` and move `j` left.  
   - Otherwise, move `i` right.  
4. Repeat for each `k` from `n-1` down to `2`.

---

## Complexity Analysis
- **Time Complexity:** `O(n^2)` due to sorting (`O(n log n)`) + two-pointer scanning.  
- **Space Complexity:** `O(1)` since we only use pointers and counters.  

---

## Code Implementation
```python
class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        count = 0
        n = len(nums)

        # Fix the largest side at index k
        for k in range(n - 1, 1, -1):
            i, j = 0, k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    count += (j - i)
                    j -= 1
                else:
                    i += 1
        return count
```

### Tags
`LeetCode-Medium`, `Array`