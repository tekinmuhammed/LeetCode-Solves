# 3347. Maximum Frequency of an Element After Performing Operations II

## 🧩 Problem Description

You are given:
- an integer array `nums`,
- and two integers `k` and `numOperations`.

In each operation:
- You can choose **any unselected index** `i`.
- Add an integer `x` such that `-k ≤ x ≤ k` to `nums[i]`.

You can perform at most `numOperations` operations in total.  
Your task is to **maximize the frequency** of any single element in the array after performing these operations.

---

## 💡 Intuition

This problem extends the idea of **Problem 3346**, but with a wider search space for potential “target values” (called *modes*).

Instead of checking every integer between `min(nums)` and `max(nums)`,  
we generate a smaller set of **promising candidate target values** (`modes`) based on:
- Each unique number itself,
- That number ± `k`, since these boundaries often define optimal transformation ranges.

This optimization significantly reduces unnecessary iterations while keeping accuracy.

---

## ⚙️ Approach

1. **Sort the array** for efficient range search using binary search (`bisect`).
2. **Count frequencies** of all unique elements and record them in a dictionary (`num_count`).
3. **Build a set of candidate target values (`modes`)**:
   - Include each number,
   - Include `number - k` and `number + k` if they fall within bounds.
4. For each candidate `mode`:
   - Find how many numbers fall within `[mode - k, mode + k]` using binary search.
   - If `mode` already exists in `nums`, we can enhance its count by at most `numOperations`.
   - Otherwise, we can convert up to `numOperations` numbers to it.
5. Track the **maximum achievable frequency** among all candidate modes.

---

## 💻 Code Implementation

```python
from collections import defaultdict
from typing import List
import bisect

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        ans = 0
        num_count = defaultdict(int)
        modes = set()

        # Add candidate "mode" values and their shifted boundaries
        def add_mode(value):
            modes.add(value)
            if value - k >= nums[0]:
                modes.add(value - k)
            if value + k <= nums[-1]:
                modes.add(value + k)

        # Step 1: Count frequencies of unique numbers
        last_num_index = 0
        for i in range(len(nums)):
            if nums[i] != nums[last_num_index]:
                num_count[nums[last_num_index]] = i - last_num_index
                ans = max(ans, i - last_num_index)
                add_mode(nums[last_num_index])
                last_num_index = i

        num_count[nums[last_num_index]] = len(nums) - last_num_index
        ans = max(ans, len(nums) - last_num_index)
        add_mode(nums[last_num_index])

        # Step 2: Evaluate all candidate target values (modes)
        for mode in sorted(modes):
            l = bisect.bisect_left(nums, mode - k)
            r = bisect.bisect_right(nums, mode + k) - 1

            if mode in num_count:
                temp_ans = min(r - l + 1, num_count[mode] + numOperations)
            else:
                temp_ans = min(r - l + 1, numOperations)

            ans = max(ans, temp_ans)

        return ans
```

### 🧠 Explanation of Key Steps

- `nums.sort()`: Sorting simplifies the process of locating valid number ranges.

- `num_count`: Stores frequency of each distinct number.

- `add_mode(value)`: Adds potential target values — including value ± k — to reduce redundant scanning.

- `bisect_left`, `bisect_right`: Find the range [mode - k, mode + k] of numbers that can be transformed into mode.

- `temp_ans`: Calculates achievable frequency for a given mode after up to numOperations modifications.

- `ans`: Tracks the global maximum frequency found so far.

### ⏱️ Complexity Analysis

- **Time Complexity:**	`O(n log n + m log n)`	Sorting (`n log n`) + scanning candidate modes (`m log n`), where `m` is number of modes (≤ 3 × unique elements).

- **Space Complexity:**	`O(n)`	Frequency dictionary + mode set.

### 🧪 Example
```python
Input:
nums = [2, 3, 5]
k = 2
numOperations = 2

Output:
3
```

### Explanation:

- You can add `+2` to `nums[0] = 2` → becomes `4`.

- You can add `-1` to `nums[2] = 5` → becomes `4`.

- Final array: `[4, 3, 4]`

- Then with one more allowed operation, you can turn `3 → 4`.

- Maximum frequency = `3`.

### ✅ Summary

Builds upon 3346 but optimizes by only testing key target values.

Uses sorting + binary search for efficient range queries.

Achieves a balance between accuracy and performance by leveraging value boundaries.

Elegant and efficient — particularly for large arrays with clustered values.
