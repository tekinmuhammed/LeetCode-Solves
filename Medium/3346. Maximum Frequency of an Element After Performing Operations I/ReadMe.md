# 3346. Maximum Frequency of an Element After Performing Operations I

**Difficulty:** Medium
**Problem Link:** [LeetCode 3346](https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-i/description/)

## 🧩 Problem Description
You are given:
- an integer array `nums`,
- and two integers `k` and `numOperations`.

You can perform at most `numOperations` operations.  
In each operation:
- Choose an **unselected index** `i`.
- Add an integer `x` such that `-k ≤ x ≤ k` to `nums[i]`.

Return the **maximum frequency** of any element that can be achieved after performing these operations.

---

## 💡 Intuition

The key is to find how many numbers can be converted into the **same target value** within the constraints:
- Each element can change by at most `±k`.
- We can modify at most `numOperations` elements.

For each possible target value `i` in the range `[min(nums), max(nums)]`,  
we can:
1. Find how many numbers are within `[i - k, i + k]`.
2. Count how many of them can become equal to `i`.
3. Add at most `numOperations` additional transformations if available.

---

## ⚙️ Approach

1. **Sort the array** to enable binary search operations (`bisect`).
2. **Precompute frequency** of each number using a loop.
3. For every possible integer `i` between `nums[0]` and `nums[-1]`:
   - Use `bisect_left` and `bisect_right` to find the range of elements that can become `i` (`[i - k, i + k]`).
   - Compute potential frequency:
     - If `i` already exists in `nums`, we can increase its count by up to `numOperations`.
     - If not, we can form at most `numOperations` new instances.
   - Keep track of the **maximum achievable frequency**.

---

## 💻 Code Implementation

```python
from typing import List
import bisect

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        ans = 0
        num_count = {}
        last_num_index = 0
        
        # Step 1: Count frequency of each unique number
        for i in range(len(nums)):
            if nums[i] != nums[last_num_index]:
                num_count[nums[last_num_index]] = i - last_num_index
                ans = max(ans, i - last_num_index)
                last_num_index = i

        num_count[nums[last_num_index]] = len(nums) - last_num_index
        ans = max(ans, len(nums) - last_num_index)

        # Step 2: Try each possible target value i
        for i in range(nums[0], nums[-1] + 1):
            l = bisect.bisect_left(nums, i - k)
            r = bisect.bisect_right(nums, i + k) - 1

            if i in num_count:
                temp_ans = min(r - l + 1, num_count[i] + numOperations)
            else:
                temp_ans = min(r - l + 1, numOperations)

            ans = max(ans, temp_ans)

        return ans
```

### 🧠 Explanation of Key Steps

- `nums.sort()`:	Sorting simplifies range and binary search operations.

- `num_count`:	Stores how often each unique number appears.

- `bisect_left(nums, i - k)` / `bisect_right(nums, i + k)`:	Finds the valid range of numbers that can be turned into `i`.

- `temp_ans = min(r - l + 1, num_count[i] + numOperations)`:	Calculates the achievable frequency for target `i`.

- `ans = max(ans, temp_ans)`:	Updates the global maximum frequency.

### ⏱️ Complexity Analysis

- **Time Complexity:**	`O(n log n + R log n)`	Sorting + binary search for each possible target `i` (where `R = nums[-1] - nums[0]`).
- **Space Complexity:**	`O(n)`	HashMap for counting unique elements.

### 🧪 Example
```python
Input:
nums = [1, 3, 4]
k = 2
numOperations = 1

Output:
2
```

### Explanation:

- You can add `+2` to `nums[0] = `1 → becomes `3`

- Resulting array: `[3, 3, 4]`

- Maximum frequency = `2`

### ✅ Summary

- Sort the array for efficient searching.

- Use binary search to find all numbers that can become a target value.

- Combine existing frequency with up to `numOperations` modifications.

- Track the maximum frequency achievable.

This method efficiently balances **operation limits**, **range constraints**, and **frequency maximization**.

### Tags
`LeetCode-Medium`