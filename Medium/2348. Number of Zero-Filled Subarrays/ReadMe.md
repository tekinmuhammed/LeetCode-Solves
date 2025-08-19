# 2348. Number of Zero-Filled Subarrays  

**Difficulty:** Medium  
**Link:** [LeetCode 2348](https://leetcode.com/problems/number-of-zero-filled-subarrays/)  

---

## Problem Description  

Given an integer array `nums`, return the number of **subarrays filled with 0**.  

A subarray is a contiguous non-empty sequence of elements within an array.  

---

## Example  

### Input:  
```python
nums = [1,3,0,0,2,0,0,4]
```

### Output:
```python
6
```

### Explanation:

- `[0]` occurs 4 times.

- `[0,0]` occurs 2 times.
Total = `6`.

### Constraints

- `1 <= nums.length <= 10^5`

- `-10^9 <= nums[i] <= 10^9`

### Approach
**Key Ideas:**

- Each time we encounter a `0`, it can form new subarrays ending at that index.

- Maintain a running counter (`count`) of consecutive zeros.

- For every `0` encountered, increment `count` and add it to the result (`result`).

- If the number is non-zero, reset `count = 0`.

- This way, the formula automatically counts all possible zero-filled subarrays.

### Time and Space Complexity

- **Time Complexity:** `O(n)` — iterate through the array once.

- **Space Complexity:** `O(1)` — uses only constant extra space.

### Tags

`Array`, `Prefix-Sum`, `Math`

### Notes

- The trick lies in using the running `count` to accumulate subarrays efficiently.

- This avoids generating all subarrays explicitly (which would be `O(n^2)`).