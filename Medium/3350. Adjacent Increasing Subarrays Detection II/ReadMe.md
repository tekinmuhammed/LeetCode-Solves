# 🧩 3350. Adjacent Increasing Subarrays Detection II

**Difficulty:** Medium  
**Problem Link:** [LeetCode 3350](https://leetcode.com/problems/adjacent-increasing-subarrays-detection-ii/description/)

## 💡 Problem Description
You are given an integer array `nums`.  
You need to find the **maximum integer k** such that there exist **two adjacent subarrays** of length `k` which are both *strictly increasing*.

Return the maximum possible `k`.

---

## 🧠 Approach

We need to determine the largest `k` where two back-to-back increasing subarrays of length `k` exist.

### 🔹 Step 1. Precompute increasing sequence lengths
We first compute an auxiliary array `increase_len`, where:
- `increase_len[i]` = the length of the longest strictly increasing subarray **starting from index `i`**.

This helps us quickly check if `nums[i:i+k]` is strictly increasing — it will be if `increase_len[i] >= k`.

### Example:
```python
nums = [1, 2, 3, 2, 3, 4]
increase_len = [3, 2, 1, 3, 2, 1]
```

---

### 🔹 Step 2. Helper function `can_find(k)`
For a given `k`, we check if there exists a starting index `a` such that:
- `increase_len[a] >= k`
- `increase_len[a + k] >= k`

That means:
- The subarray `nums[a:a+k]` is increasing.
- The adjacent subarray `nums[a+k:a+2k]` is also increasing.

If such an `a` exists, `k` is valid.

---

### 🔹 Step 3. Binary Search on `k`
We perform a binary search over `k` from `0` to `N // 2`, since each of the two subarrays must have length `k`.

- If `can_find(mid)` is `True`, it means `k = mid` is possible → try larger values.
- Otherwise, reduce `k`.

This yields the **maximum possible** valid `k`.

---

## 🧩 Code Implementation

```python
class Solution(object):
    def maxIncreasingSubarrays(self, nums: list[int]) -> int:
        N = len(nums)
        if N < 2:
            return 0
        
        # Step 1: Precompute lengths of increasing subarrays
        increase_len = [0] * N
        increase_len[N - 1] = 1
        
        for i in range(N - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                increase_len[i] = 1 + increase_len[i + 1]
            else:
                increase_len[i] = 1
        
        # Step 2: Check if k-length adjacent increasing subarrays exist
        def can_find(k):
            if k == 0:
                return True
            if 2 * k > N:
                return False
            
            for a in range(N - 2 * k + 1):
                if increase_len[a] >= k and increase_len[a + k] >= k:
                    return True
            return False

        # Step 3: Binary search to find maximum k
        low, high, max_k = 0, N // 2, 0
        
        while low <= high:
            mid = (low + high) // 2
            if can_find(mid):
                max_k = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return max_k
```

### ⏱️ Complexity Analysis

- **Time Complexity:**	`O(N log N)` → computing `increase_len` takes `O(N)`, and each binary search iteration checks `O(N)`

- **Space Complexity:**	`O(N)` → for `increase_len` array

### 🧪 Example

**Input:**
```python
nums = [1, 2, 3, 2, 3, 4]
```

**Process:**

- For `k = 2`:
- - `[1, 2]` and `[3, 2]` → second not increasing
- - `[2, 3]` and `[2, 3]` → second is increasing ✅
- - Thus, `k = 2` is valid.

- For `k = 3`: not possible (adjacent 3-length increasing sequences don’t exist)

**Output:**
```python
2
```

### 🏁 Summary
✅ Precompute increasing runs.
✅ Use binary search to efficiently find the maximum `k`.
✅ Elegant combination of dynamic precomputation + search optimization.

### Tags
`LeetCode-Medium`