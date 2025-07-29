# 2411. Smallest Subarrays With Maximum Bitwise OR

**Difficulty:** Medium  
**Problem Link:** [LeetCode 2411](https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or)

---

## Problem Description

You are given an array `nums`. For each index `i`, return the length of the **smallest subarray starting at `i`** such that the bitwise OR of that subarray is equal to the maximum bitwise OR possible from index `i` to the end of the array.

---

### Example

**Input:**
```python
nums = [1,0,2,1,3]
```

**Output:**
```python
[3,3,2,2,1]
```

### Explanation:

- For index 0: The OR from index 0 to 2 (`1|0|2 = 3`) is the maximum OR possible, so length = 3.

- For index 4: Just [3] is enough.

### Approach

We work **backwards** from the end of the array, tracking **when each bit (0 to 31) was last seen**.

1. We maintain an array `last[0..31]` to record the **latest index** where each bit is set.

2. For each `i` from `n-1` to `0`:

- Update `last[j]` if the j-th bit is set in `nums[i]`.

- The farthest position `max_last` we must go to include all active bits determines the minimum subarray length starting from `i`.

### Complexity

- **Time Complexity:** `O(n * 32)` ≈ `O(n)`

- **Space Complexity:** `O(32)` for bit tracking + `O(n)` for result

### Tags

`Bit-Manipulation`, `Greedy`, `Array`, `Sliding-Window`, `Prefix`, `Suffix`

### Notes

-The idea is that to maintain the **maximum OR**, we must include all future numbers that contribute bits we don’t currently have.

- Going from right to left helps us keep track of how far we need to go from each index.