# 1437. Check If All 1's Are at Least Length K Places Away — Explanation & Analysis

**Difficulty:** Easy
**Problem Link:** [LeetCode 1437](https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/description/)

## ✔️ Problem Summary
Given a binary array `nums`, determine whether every pair of `1`s in the array is at least `k` indices apart.

A pair of 1’s at positions `i` and `j` is valid only if:
```python
j - i - 1 >= k
```

---

## 💡 Key Insight
You only need to track the position of the **previous 1**.

Algorithm:

1. Set `prev = -1` to indicate no previous 1 has been seen.
2. For each index `i`:
   - If `nums[i] == 1`:
     - If this is **not** the first 1 (`prev != -1`) and  
       the distance `i - prev - 1` is **less than k**, return `False`.
     - Update `prev = i`.
3. If no invalid distances found, return `True`.

---

## ⏱️ Time & Space Complexity
| Metric | Complexity |
|--------|------------|
| **Time** | `O(n)` |
| **Space** | `O(1)` |

---

## 🧠 Example
For `nums = [1,0,0,1]` and `k = 2`  
✔️ Valid (two zeros between 1s)

For `nums = [1,0,1]` and `k = 2`  
✖️ Invalid (only one zero between 1s)

---

## ✅ Code Implementation (Your Code)
```python
class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        prev = -1  # previous 1's index

        for i, val in enumerate(nums):
            if val == 1:
                if prev != -1 and i - prev - 1 < k:
                    return False
                prev = i

        return True
```

### 📌 Why This Solution Is Optimal

- Single pass → very fast

- No extra memory

- Direct distance checking

- Works efficiently on very large inputs