# 2154. Keep Multiplying Found Values by Two — Explanation & Analysis

**Difficulty:** Easy  
**Problem Link:** [LeetCode 2154](https://leetcode.com/problems/keep-multiplying-found-values-by-two/description/)

## ✔️ Problem Summary
Given an array `nums` and an integer `original`:

- While `original` exists in `nums`, you must **double** it.
- When it no longer exists, return the final value.

---

## 💡 Key Idea
Convert `nums` into a **set** for O(1) lookups.  
Then keep doubling `original` until it’s no longer found in the set.

---

## ⏱️ Time & Space Complexity
| Metric | Complexity |
|--------|------------|
| **Time** | `O(n + k)` — building set + doubling steps |
| **Space** | `O(n)` |

`k` is the small number of doubling iterations — usually tiny.

---

## 🧠 Example
`nums = [5,3,6,1,12], original = 3`

- 3 in nums → original = 6  
- 6 in nums → original = 12  
- 12 in nums → original = 24  
- 24 not in nums → stop  

Result: **24**

---

## ✅ Code Implementation (Your Code)
```python
class Solution(object):
    def findFinalValue(self, nums, original):
        s = set(nums)   # O(1) lookup
        
        while original in s:
            original *= 2
            
        return original
```

### 📌 Why This Solution Is Optimal

- Set lookup is the fastest approach

- Loop only runs for values actually present

- No unnecessary sorting or extra passes