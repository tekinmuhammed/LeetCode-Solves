# 1674. Minimum Moves to Make Array Complementary

**Difficulty:** Medium  
**Problem Link:** [LeetCode 1674](https://leetcode.com/problems/minimum-moves-to-make-array-complementary/description/)

---

## Problem
You are given an integer array `nums` of **even** length `n` and an integer `limit`. In one move, you can replace any integer from `nums` with another integer between `1` and `limit`, inclusive.

The array `nums` is **complementary** if for all indices `i` (0-indexed), `nums[i] + nums[n - 1 - i]` equals the same number. For example, the array `[1,2,3,4]` is complementary because for all indices `i`, `nums[i] + nums[n - 1 - i] = 5`.

Return the **minimum number of moves** required to make `nums` complementary.

---

# Approach

The brute force approach would be to test every possible target sum `T` (from `2` to `2 * limit`) and count the moves for all pairs. However, this results in an $O(N \times \text{limit})$ time complexity, which will cause a Time Limit Exceeded (TLE) error.

Instead, we can use a **Difference Array (Sweep Line Algorithm)** to optimize the interval updates.

For any pair `(a, b)` where `a = min(nums[i], nums[n-1-i])` and `b = max(nums[i], nums[n-1-i])`, let's analyze how many moves are required for a target sum `T`:

1. **`2 <= T < a + 1`**: We need **2 moves** (both elements must be changed, even if we change them to the minimum possible value `1`, their sum is still too big).
2. **`a + 1 <= T < a + b`**: We need **1 move** (we can just lower `b` to make the sum `T`).
3. **`T == a + b`**: We need **0 moves** (the sum is already `T`).
4. **`a + b < T <= b + limit`**: We need **1 move** (we can just increase `a` to make the sum `T`).
5. **`T > b + limit`**: We need **2 moves** (both elements must be changed, even if we change `a` to the maximum `limit`, their sum is still too small).

### The Difference Array Logic:
Instead of updating all sums `T` one by one, we record the *changes* in the number of moves at key boundaries:
* By default, assume **2 moves** are needed for all `T` starting from 2: `diff[2] += 2`.
* At `a + 1`, the required moves drop from 2 to 1: `diff[a + 1] -= 1`.
* At `a + b`, the required moves drop from 1 to 0: `diff[a + b] -= 1`.
* At `a + b + 1`, the required moves increase from 0 to 1: `diff[a + b + 1] += 1`.
* At `b + limit + 1`, the required moves increase from 1 to 2: `diff[b + limit + 1] += 1`.

Finally, we calculate the prefix sum of the `diff` array. This gives us the exact number of operations needed for every target sum `T`, allowing us to simply find the minimum.

---

# Example Walkthrough

Consider a pair `a = 2`, `b = 4` and `limit = 5`.

* Possible target sums range from `2` to `10`.
* Boundaries:
  * `a + 1 = 3`
  * `a + b = 6`
  * `a + b + 1 = 7`
  * `b + limit + 1 = 10`

Difference Array Updates:
* `diff[2] += 2`  (Assume 2 moves starting from T=2)
* `diff[3] -= 1`  (At T=3, drop to 1 move)
* `diff[6] -= 1`  (At T=6, drop to 0 moves)
* `diff[7] += 1`  (At T=7, go back up to 1 move)
* `diff[10] += 1` (At T=10, go back up to 2 moves)

When we compute the running sum (prefix sum) across these indices, the values beautifully reflect the exact number of moves needed for this specific pair for any target `T`.

---

# Complexity Analysis

Time Complexity

O(N + L)

Where `N` is the length of the `nums` array and `L` is the `limit`. We iterate through half of the array ($O(N/2)$) to build the difference boundaries. Then, we iterate through the possible target sums from `2` to `2 * L` ($O(L)$) to find the minimum operations.

Space Complexity

O(L)

We allocate a `diff` array of size `2 * limit + 2` to manage the sweep line boundaries.

---

# Code

```python
class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        diff = [0] * (2 * limit + 2)

        for i in range(n // 2):
            a = min(nums[i], nums[n - 1 - i])
            b = max(nums[i], nums[n - 1 - i])

            diff[2] += 2
            diff[a + 1] -= 1
            diff[a + b] -= 1
            diff[a + b + 1] += 1
            diff[b + limit + 1] += 1

        min_ops = n
        current_ops = 0

        for c in range(2, 2 * limit + 1):
            current_ops += diff[c]
            if current_ops < min_ops:
                min_ops = current_ops

        return min_ops
```