# 2200. Find All K-Distant Indices in an Array

**Difficulty:** Easy  
**Link:** [LeetCode Problem 2200](https://leetcode.com/problems/find-all-k-distant-indices-in-an-array)

---

## Problem Description

Given an integer array `nums`, a key value `key`, and an integer `k`, return a list of all indices `i` such that:

There exists an index `j` where:
- `nums[j] == key` **and**
- `abs(i - j) <= k`

Return the answer in **increasing order**.

---

## Example

### Input:
```python
nums = [3,4,9,1,3,9,5]
key = 9
k = 1
```

### Output:
```python
[1,2,3,4,5,6]
```

### Explanation:

- `nums[2] == 9` → all indices from `1` to `3` are within distance 1 → `[1,2,3]`

- `nums[5] == 9` → all indices from `4` to `6` are within distance 1 → `[4,5,6]`

- Union of both ranges = `[1,2,3,4,5,6]`

### Constraints

- `1 <= nums.length <= 1000`

- `0 <= nums[i] <= 1000`

- `key` is guaranteed to be in `nums`

- `1 <= k <= nums.length`

### Approach

- Iterate through the array to identify all indices where `nums[j] == key`.

- For each such index `j`, mark all indices `i` such that `abs(i - j) <= k`.

- Use a `set` to avoid duplicates.

- Return the result as a sorted list.

### Time and Space Complexity

- **Time Complexity:** `O(n * k)`

In the worst case, for each occurrence of `key`, up to `2k+1` elements are processed.

- **Space Complexity:** `O(n)`

Due to the result set.

### Tags
`Array`, `Brute-Force`, `Set`

### Notes

- Using a `set` ensures no duplicate indices.

- Sorting is done at the end to meet the output requirement.