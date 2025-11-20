# 757. Set Intersection Size At Least Two

**Difficulty:** Hard 
**Problem Link:** [LeetCode 757](https://leetcode.com/problems/set-intersection-size-at-least-two/description/)

## ✔️ Problem Summary
You are given several intervals.  
Your task is to choose the **minimum number of integers** such that **each interval contains at least two** of the chosen integers.

---

## 💡 Main Strategy (Greedy)
To minimize added numbers, we sort intervals by:

1. **End ascending**  
2. **Start descending**  

This ensures:
- We process the interval that finishes earliest first,
- And among those, the one with the **largest starting point** (most restrictive).

We maintain two chosen numbers:

`a < b`

These represent the **largest two chosen points so far**.

For each interval:

### Case 1: `start > b` — no chosen point is inside  
We must add **two new points**:  
- `end - 1`
- `end`

### Case 2: `start > a` — only one chosen point is inside  
We must add **one new point**:  
- `end`

### Case 3: otherwise  
Two points already exist in the interval → no action.

---

## ⏱️ Time & Space Complexity

| Metric | Complexity |
|--------|------------|
| **Time** | `O(n log n)` due to sorting |
| **Space** | `O(1)` extra space |

---

## 🧠 Example

**Intervals:**
```python
[[1,3], [3,7], [2,6]]
```

**Sorted:**
```python
[[1,3], [2,6], [3,7]]
```

Process them — you add numbers minimally until every interval has ≥2 points.

---

## ✅ Code Implementation (Your Code)

```python
class Solution(object):
    def intersectionSizeTwo(self, intervals):
        # Sort by end asc, and start desc
        intervals.sort(key=lambda x: (x[1], -x[0]))
        
        res = 0
        # last two chosen points
        a = -1
        b = -1
        
        for start, end in intervals:
            # Case 1: both points are outside the interval
            if start > b:
                # we need 2 new numbers
                res += 2
                b = end
                a = end - 1
            # Case 2: only one point is inside
            elif start > a:
                # need 1 more number
                res += 1
                a = b
                b = end
        
        return res
```

### 📌 Why This Solution Is Optimal

- Greedy always picks points as far right as possible

- Minimizes how many new numbers need to be added

- Matches the official editorial solution style

