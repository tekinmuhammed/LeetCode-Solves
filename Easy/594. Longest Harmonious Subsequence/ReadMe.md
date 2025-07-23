# 594. Longest Harmonious Subsequence

**Difficulty:** Easy  
**Link:** [LeetCode 594](https://leetcode.com/problems/longest-harmonious-subsequence)

---

## Problem Description

We define a harmonious array as an array where the **difference between its maximum and minimum value is exactly 1**.

Given an integer array `nums`, return the length of its **longest harmonious subsequence** among all possible subsequences.

---

## Example

### Input:
```python
nums = [1,3,2,2,5,2,3,7]
```

### Output:
```python
5
```

### Explanation:

The longest harmonious subsequence is `[3,2,2,2,3]`.

### Constraints

- `1 <= nums.length <= 2 * 10⁴`

- `-10⁹ <= nums[i] <= 10⁹`

### Approach
**Key Idea:**

- Count the frequency of each number using `collections.Counter`.

- For every number `x` in the frequency map, if `x + 1` exists, the subsequence formed by `x` and `x + 1` is valid.

- The length of this harmonious subsequence is `count[x] + count[x + 1]`.

### Algorithm Steps:

1. Count the occurrences of each number.

2. Iterate through each number in the map:

- If `num + 1` exists in the map, compute the total frequency of `num` and `num + 1`.

- Update the maximum length accordingly.

- Return the maximum length found.

### Time and Space Complexity

- **Time Complexity:** `O(n)`

- - One pass for counting + one pass for checking neighbors.

- **Space Complexity:** `O(n)`

- Due to storing frequencies in the hash map.

### Tags
`Hash-Table`, `Array`, `Frequency-Count`

### Notes

- A subsequence does not require elements to be contiguous.

- Only pairs of adjacent numbers (`x` and `x+1`) are considered.

- This solution avoids sorting and is efficient even for large inputs.