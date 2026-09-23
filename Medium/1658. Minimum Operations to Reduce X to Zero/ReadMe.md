# 1658. Minimum Operations to Reduce X to Zero

**Difficulty:** Medium  
**Problem Link:** [LeetCode 1658](https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/description/)

---

## Problem
You are given an integer array `nums` and an integer `x`. In one operation, you can either remove the leftmost or the rightmost element from the array `nums` and subtract its value from `x`. Note that this modifies the array for future operations.

Return the **minimum number of operations** to reduce `x` to exactly 0 if it is possible, otherwise, return `-1`.

Example:

Input  
nums = [1,1,4,2,3], x = 5  

Output  
2  

Explanation  
The optimal solution is to remove the last two elements (2 and 3) to reduce x to zero.

---

# Approach

Instead of trying to find the minimum number of elements at the edges that sum up to `x`, we can flip the problem inside out. 

Finding the **minimum** elements at the edges that sum to `x` is mathematically equivalent to finding the **longest contiguous subarray** in the middle that sums to `total_sum - x`. 

Let this target sum be `k = sum(nums) - x`. We can use the **Sliding Window** technique to find the longest subarray that sums exactly to `k`.

Steps:
1. **Target Calculation**: Compute `k = sum(nums) - x`. If `k < 0`, it's impossible to reach `x` because the total sum of the array is less than `x`. Return `-1`.
2. **Sliding Window Setup**: Use two pointers, `i` (left) and `j` (right), and a running sum `s`. Track the maximum length of a valid subarray in `best`.
3. **Expand Window**: Iterate `j` through the array, adding `nums[j]` to `s`.
4. **Shrink Window**: If `s` exceeds `k`, increment `i` and subtract `nums[i]` from `s` until `s` is less than or equal to `k`.
5. **Record Max Length**: Whenever `s == k`, update `best` with the maximum window size (`j - i + 1`).
6. **Result Calculation**: If `best` remains `-1`, no valid subarray was found, so return `-1`. Otherwise, the minimum operations required is the total length of the array minus `best`.

---

# Code

```python
class Solution:
    def minOperations(self, A: List[int], x: int) -> int:
        k = sum(A) - x
        if k < 0: return -1 
        best = -1
        
        s = i = 0
        
        for j, num in enumerate(A):
            s += num
            while s > k:
                s -= A[i]
                i += 1  
            if s == k:
                best = max(best, j - i + 1)

        return -1 if best < 0 else len(A) - best
```

---

# Example Walkthrough

Let's trace `nums = [1, 1, 4, 2, 3]`, `x = 5`.

1. **Calculate Target**: `total_sum = 11`. Target `k = 11 - 5 = 6`.
2. **Sliding Window**:
   * `j = 0`, `num = 1`: `s = 1`
   * `j = 1`, `num = 1`: `s = 2`
   * `j = 2`, `num = 4`: `s = 6`. **Match!** `s == k`. `best = max(-1, 2 - 0 + 1) = 3`.
   * `j = 3`, `num = 2`: `s = 8`. Window shrinks: remove `A[0]`(1). `s = 7`. Shrink again: remove `A[1]`(1). `s = 6`. **Match!** `s == k`. `best = max(3, 3 - 2 + 1) = 3`.
   * `j = 4`, `num = 3`: `s = 9`. Window shrinks: remove `A[2]`(4). `s = 5`. Loop ends.
3. **Result**: The longest subarray summing to 6 has length `best = 3`. Minimum operations = `len(nums) - best = 5 - 3 = 2`.

Result is `2`.

---

# Complexity Analysis

Time Complexity

$\mathcal{O}(N)$

Where $N$ is the number of elements in the array. The right pointer `j` iterates through the array exactly once. The left pointer `i` only moves forward, visiting each element at most once. Thus, the total number of operations is at most $2N$, which simplifies to strictly linear time.

Space Complexity

$\mathcal{O}(1)$

We only use a few integer variables (`k`, `best`, `s`, `i`) to keep track of the window state and sums. No additional data structures are created, making the auxiliary space constant.