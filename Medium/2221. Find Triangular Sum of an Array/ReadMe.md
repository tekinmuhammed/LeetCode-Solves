# 2221. Find Triangular Sum of an Array  

**Difficulty:** Easy  

## Problem Link  
[LeetCode - 2221. Find Triangular Sum of an Array](https://leetcode.com/problems/find-triangular-sum-of-an-array/)  

## Tags  
`Array` `Math` `Simulation`  

---

## Problem Description  
You are given a **0-indexed integer array `nums`**, where `nums[i]` is a digit between `0` and `9`.  

You need to perform the following process until only one element remains in the array:  

1. Create a new array of length `n-1`.  
2. Each element in the new array is defined as:  
   \[
   newNums[i] = (nums[i] + nums[i+1]) \mod 10
   \]  
3. Replace `nums` with `newNums`.  

Return the **last remaining element** in the array after performing the process.  

---

## Approach  

- This problem is a **simulation** task.  
- Repeatedly reduce the array by combining adjacent elements modulo 10.  
- Continue until only one number remains.  
- The last number is the answer.  

---

## Code Implementation  

```python
class Solution(object):
    def triangularSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        while len(nums) > 1:
            newNums = []
            for i in range(len(nums) - 1):
                newNums.append((nums[i] + nums[i+1]) % 10)
            nums = newNums
        return nums[0]
```

### Complexity Analysis
**Time Complexity:** `𝑂(𝑛2)`, since each reduction takes `𝑂(𝑛)` and there are `𝑛−1` reductions.

**Space Complexity:** `𝑂(𝑛)` for storing intermediate arrays.

### Example
**Input:**
```python
nums = [1,2,3,4,5]
```

**Process:**
```python
[1,2,3,4,5]
 → [3,5,7,9] → [8,2,6] → [0,8] → [8]
```

**Output:**
```python
8
```