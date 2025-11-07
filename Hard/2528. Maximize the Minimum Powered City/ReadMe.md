# ⚡ LeetCode 2528 - Maximize the Minimum Powered City

**Difficulty:** Hard  
**Link:** [LeetCode 2528](https://leetcode.com/problems/maximize-the-minimum-powered-city/description/)

## 🧩 Problem Description
We are given:
- `stations[i]` → the number of power stations located in city `i`
- Each power station **affects all cities within radius `r`**, meaning city `i` receives power from all stations in the range `[i - r, i + r]`
- You can **add up to `k` new power stations** in any cities you choose.

Your goal is to **maximize the minimum total power** across all cities after optimally adding up to `k` new stations.

---

## 💡 Example

**Input:**
```python
stations = [1, 2, 4, 5, 0]
r = 1
k = 2
```

**Output:**
```python
5
```

**Explanation:**
- The power coverage radius `r = 1`
- Add 2 stations optimally (e.g., both near weaker cities)
- The minimum power across all cities can be raised to **5**.

---

## 🧠 Approach

### 🧩 Key Idea:
We want to **maximize the minimum power value** among all cities.  
This hints at using **binary search** on the answer — i.e., guess a target minimum power `val`,  
and check if we can achieve it by placing ≤ `k` new stations.

---

### 🪄 Step-by-Step Explanation

1. **Initial Power Calculation (Range Updates)**  
   Each station contributes power to a range `[i - r, i + r]`.  
   Instead of recomputing power for every city repeatedly, we use a **difference array** `cnt` to mark power contributions efficiently.

   - For station at index `i`:  
     ```
     cnt[i - r] += stations[i]
     cnt[i + r + 1] -= stations[i]
     ```
     (with bounds checking)

2. **Checking Feasibility (the `check` function)**  
   Given a target minimum power `val`, we simulate adding extra stations greedily:
   - Traverse from left to right, maintaining the current total power.
   - If the total power at city `i` is below `val`, we add enough new stations (`add = val - total`) to fix it.
   - Deduct these added stations from our budget `k`.
   - Update the difference array to reflect the extra power effect range.

   If we exceed `k`, `val` is **not achievable**.

3. **Binary Search on the Answer**  
   We search for the **maximum** achievable `val` in the range `[min(stations), sum(stations) + k]`:
   - If `check(mid)` succeeds → `val = mid` is achievable, try higher.
   - Otherwise, try lower.

---

## ⚙️ Code Implementation

```python
class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        cnt = [0] * (n + 1)

        # Build difference array (power coverage)
        for i in range(n):
            left = max(0, i - r)
            right = min(n, i + r + 1)
            cnt[left] += stations[i]
            cnt[right] -= stations[i]

        # Check if we can achieve minimum power >= val
        def check(val: int) -> bool:
            diff = cnt.copy()
            total = 0
            remaining = k

            for i in range(n):
                total += diff[i]
                if total < val:
                    add = val - total
                    if remaining < add:
                        return False
                    remaining -= add
                    end = min(n, i + 2 * r + 1)
                    diff[end] -= add
                    total += add
            return True

        # Binary search for the maximum possible minimum power
        lo, hi = min(stations), sum(stations) + k
        res = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if check(mid):
                res = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return res
```

### ⏱️ Complexity Analysis
| Operation           | Time Complexity                 | Explanation                  |
| ------------------- | ------------------------------- | ---------------------------- |
| Power preprocessing | `O(n)`                          | Difference array setup       |
| Each check          | `O(n)`                          | Linear scan with prefix sums |
| Binary search       | `O(log(sum(stations) + k))`     | Range of possible answers    |
| **Total**           | **O(n log(sum(stations) + k))** | Efficient solution           |
| Space               | **O(n)**                        | Difference arrays            |

### ✅ Summary
✔ Uses **binary search** to find maximum achievable minimum power
✔ Uses **difference array technique** for efficient range updates
✔ Greedy simulation ensures no unnecessary station additions

**Result:** Optimal, efficient, and clean implementation.