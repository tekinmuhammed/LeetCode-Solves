# 3296. Minimum Number of Seconds to Make Mountain Height Zero

**Difficulty:** Medium  
**Problem Link:** [LeetCode 3296](https://leetcode.com/problems/minimum-number-of-seconds-to-make-mountain-height-zero/description/?)

---

## Problem Description

You are given an integer `mountainHeight` and an array `workerTimes` representing the base time it takes for each worker to reduce the mountain's height.

For a worker $i$ with base time $T_i$:
- Reducing the 1st unit of height takes $T_i$ seconds.
- Reducing the 2nd unit takes $2 \times T_i$ seconds.
- Reducing the $k^{th}$ unit takes $k \times T_i$ seconds.

In total, reducing the height by $k$ units takes $T_i + 2T_i + \dots + kT_i = T_i \times \frac{k(k+1)}{2}$ seconds.

Workers can work **simultaneously**. Return the **minimum** number of seconds needed to reduce the mountain height to zero.

---

## Approach: Binary Search on Answer

Since the total height reduced increases as time increases, the function is **monotonic**. This allows us to use **Binary Search** to find the minimum time required.

### Key Ideas:
1.  **Search Range:**
    - `l = 1`: The minimum possible time.
    - `r = max(workerTimes) * H * (H + 1) // 2`: The worst-case scenario where the slowest worker does all the work.
2.  **Feasibility Check (`check(mid)`):**
    - For a given time `mid`, we calculate how many units $k$ each worker can reduce.
    - For a worker with base time $t$, we need to find the largest $k$ such that:
      $$t \times \frac{k(k+1)}{2} \le mid \implies \frac{k^2 + k}{2} \le \frac{mid}{t}$$
3.  **Solving for $k$:**
    - Let $W = \frac{mid}{t}$. We solve the quadratic inequality: $k^2 + k - 2W \le 0$.
    - Using the quadratic formula: $k = \frac{-1 + \sqrt{1 + 8W}}{2}$.
    - We take the `floor` of this value to get the maximum units reduced by that worker.
4.  **Conclusion:** If the sum of all $k$ values for all workers is $\ge mountainHeight$, then the time `mid` is sufficient.



---

## Code

```python
class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        """
        :type mountainHeight: int
        :type workerTimes: List[int]
        :rtype: int
        """
        maxWorkerTimes = max(workerTimes)
        # Search range: from 1 second to the worst-case time for one worker
        l = 1
        r = maxWorkerTimes * mountainHeight * (mountainHeight + 1) // 2
        ans = r
        eps = 1e-7 # Small epsilon for floating point precision

        while l <= r:
            mid = (l + r) // 2
            total_reduced = 0
            
            for t in workerTimes:
                # Max work value allowed for this worker in 'mid' time
                work_limit = mid // t
                
                # Using quadratic formula to solve: k^2 + k - 2*work_limit <= 0
                # k = (-1 + sqrt(1 + 8*work_limit)) / 2
                k = int((-1 + ((1 + work_limit * 8) ** 0.5)) / 2 + eps)
                total_reduced += k
                
                # Early exit if we already met the requirement
                if total_reduced >= mountainHeight:
                    break
            
            if total_reduced >= mountainHeight:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1

        return ans
```

---

## Example Walkthrough

**Input:** `mountainHeight = 4, workerTimes = [2, 1, 1]`

1.  **Binary Search `mid = 3`:**
    - Worker 1 ($t=2$): $2 \times \frac{k(k+1)}{2} \le 3 \implies k=1$
    - Worker 2 ($t=1$): $1 \times \frac{k(k+1)}{2} \le 3 \implies k=2$
    - Worker 3 ($t=1$): $1 \times \frac{k(k+1)}{2} \le 3 \implies k=2$
    - **Total:** $1 + 2 + 2 = 5$. Since $5 \ge 4$, time `3` is possible.
2.  **Binary Search `mid = 2`:**
    - Worker 1: $k=1$ (2 sec)
    - Worker 2: $k=1$ (1 sec)
    - Worker 3: $k=1$ (1 sec)
    - **Total:** $1 + 1 + 1 = 3$. Since $3 < 4$, time `2` is not enough.

**Result:** `3`

---

## Complexity Analysis

* **Time Complexity:** $O(N \log(MaxTime))$
    - $N$ is the number of workers.
    - $MaxTime$ is $O(\max(T_i) \times H^2)$. 
    - The binary search takes $\log(MaxTime)$ steps, and in each step, we iterate through $N$ workers.
* **Space Complexity:** $O(1)$
    - We use a constant amount of extra space for variables.

---

## Tags
`Binary-Search`, `Math`, `Quadratic-Formula`, `Greedy`