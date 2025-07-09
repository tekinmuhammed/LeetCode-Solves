# 2099. Find Subsequence of Length K With the Largest Sum

**Difficulty:** Easy  
**Link:** [LeetCode 2099](https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/)

---

## Problem Description

You are given an integer array `nums` and an integer `k`.

Return **the subsequence of length `k`** with the **largest sum**.  
A **subsequence** is derived by deleting some or no elements of the array without changing the order of the remaining elements.

---

## Example

### Input:
```python
nums = [2, 1, 3, 3]
k = 2
```

### Output:
`[3, 3]`

### Constraints

- `1 <= nums.length <= 1000`

- `-10⁵ <= nums[i] <= 10⁵`

- `1 <= k <= nums.length`

### Approach

**Step-by-step Strategy:**

1. **Pair each number with its index** to keep track of the original order.

2. Sort the list by value in descending order to find the top `k` largest elements.

3. **Select the top `k` elements** and then sort them by their original indices.

4. **Return the values only**, in the original order of appearance.

This ensures both maximum sum and original subsequence order.

### Time and Space Complexity

- **Time Complexity:** `O(n log n)`
Sorting the array dominates the time cost.

- **Space Complexity:** `O(n)`
Due to auxiliary list of indexed pairs.

### Tags
`Greedy`, `Sorting`, `Subsequence`

### Notes

- Maintaining original indices ensures that the selected elements form a valid subsequence.

- This solution uses simple sorting tricks to maintain both maximum sum and element order.