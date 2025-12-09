# 3583. Count Special Triplets — Explanation & Analysis

**Difficulty:** Medium  
**Problem Link:** [LeetCode 3583](https://leetcode.com/problems/count-special-triplets/description/)

## 🔍 Problem Summary
Given an array `nums`, we need to count the number of **special triplets** `(i, j, k)` such that:

- `i < j < k`
- `nums[i] = nums[j] * 2`
- `nums[k] = nums[j] * 2`

The answer must be returned modulo **10⁹ + 7**.

---

## 💡 Approach Overview
We use two counters:

- `left` → counts numbers to the left of index `j`
- `right` → counts numbers to the right of index `j`

For each index `j`, the number of valid triplets with `j` as the middle element is:
```python
count_left = left[2 * nums[j]]
count_right = right[2 * nums[j]]
triplets_for_j = count_left * count_right
```

Then we update the counters and continue.

This results in an **O(n)** time solution.

---

## 🧠 Step-by-Step Logic

1. Initialize:
   - `right = Counter(nums)`
   - `left = {}` (empty counter)

2. Iterate through each `j`:
   - Remove current value from `right`
   - Compute `target = 2 * nums[j]`
   - Fetch count on the left: `left[target]`
   - Fetch count on the right: `right[target]`
   - Add `left[target] * right[target]` to the answer
   - Add current value to `left`

---

## ⏱️ Time & Space Complexity

| Complexity | Value |
|-----------|--------|
| Time      | **O(n)** |
| Space     | **O(n)** |

This is the optimal approach for this problem.

---

## ✅ Code (Your Solution)

```python
class Solution(object):
    def specialTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        
        from collections import Counter
        
        right = Counter(nums)
        left = Counter()
        
        ans = 0
        
        for j, val in enumerate(nums):
            right[val] -= 1
            if right[val] == 0:
                del right[val]
            
            target = val * 2
            
            count_i = left.get(target, 0)
            count_k = right.get(target, 0)
            
            ans = (ans + count_i * count_k) % MOD
            
            left[val] += 1
        
        return ans
```