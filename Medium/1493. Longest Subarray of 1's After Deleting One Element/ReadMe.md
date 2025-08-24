# 1493. Longest Subarray of 1's After Deleting One Element  

**Difficulty:** Medium  
**Link:** [LeetCode 1493](https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/)  

---

## Problem Description  

Given a binary array `nums`, you must delete **exactly one element** from the array.  

Return the length of the longest subarray containing only `1`s after deleting one element.  

---

## Example  

### Input:  
```python
nums = [1,1,0,1]
```

### Output:
```python
3
```

### Explanation:

After deleting the `0`, the array `[1,1,1]` is obtained with length `3`.

### Constraints

- `1 <= nums.length <= 10^5`

- `nums[i]` is either `0` or `1`

###   Approach
**Key Ideas:**

- Use the **sliding window (two pointers)** technique.

- Maintain a window `[left, right]` that contains at most one zero.

- As you expand `right`:

- - Increment `zero_count` when encountering a `0`.

- -  If `zero_count > 1`, move `left` forward until there is at most one zero in the window.

- At each step, update `max_len` as `(right - left)` instead of `(right - left + 1)`, because we must delete exactly one element.

### Time and Space Complexity

- **Time Complexity:** `O(n)` — each element visited at most twice (sliding window).

- **Space Complexity:** `O(1)` — constant extra space.

### Tags

`Sliding-Window`, `Two-Pointers`, `Array`

### Notes

- Key trick: subtracting `1` from window length ensures that exactly one element is deleted.

- If the array contains all `1`s, the answer is `len(nums) - 1`.