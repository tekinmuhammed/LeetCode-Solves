# 3741. Minimum Distance Between Three Equal Elements II

**Difficulty:** Medium  
**Problem Link:** [LeetCode 3741](https://leetcode.com/problems/minimum-distance-between-three-equal-elements-ii/)

---

## Problem Description

You are given an integer array `nums`. You need to find three indices `i`, `j`, and `k` such that:
1.  $0 \le i < j < k < nums.length$
2.  $nums[i] == nums[j] == nums[k]$

The **distance** is defined as $|i - j| + |j - k| + |k - i|$, which simplifies to **$2 \times (k - i)$** for sorted indices.

Return the **minimum possible distance**. If no such three indices exist, return `-1`. This version has larger constraints ($N$ up to $10^5$), requiring an $O(N)$ or $O(N \log N)$ solution.

---

## Approach: Linear Scan with Next-Occurrence Mapping

To solve this in linear time, we observe that for any given value, the minimum distance between any three occurrences will always be found in **three consecutive occurrences** of that value.

### Key Ideas:
1.  **Consecutive Triplet Insight:** If we have indices $pos_1 < pos_2 < pos_3 < pos_4$ with the same value, the distance of $(pos_1, pos_2, pos_4)$ is $2(pos_4 - pos_1)$, which is guaranteed to be larger than the distance of $(pos_1, pos_2, pos_3)$ or $(pos_2, pos_3, pos_4)$. Thus, we only need to check triplets of consecutive occurrences.
2.  **Next-Pointer Array (`nxt`):** We build an array where `nxt[i]` stores the index of the *very next* occurrence of the value `nums[i]`. 
3.  **Hash Map for Tracking:** A hash map `occur` is used during a backward pass to keep track of the last seen index for each value.
4.  **Single Pass Minimization:** Once `nxt` is built, we iterate through the array once. For each index `i`, we look for `second_pos = nxt[i]` and `third_pos = nxt[second_pos]`. If both exist, we calculate the distance $2 \times (third\_pos - i)$ and update our minimum.



---

## Code

```python
class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # nxt[i] will store the index of the next occurrence of nums[i]
        nxt = [-1] * n
        occur = {} # Value -> Last seen index
        ans = n + 1

        # Step 1: Backward pass to fill the nxt array
        for i in range(n - 1, -1, -1):
            if nums[i] in occur:
                nxt[i] = occur[nums[i]]
            occur[nums[i]] = i

        # Step 2: Forward pass to check consecutive triplets
        for i in range(n):
            second_pos = nxt[i]
            if second_pos != -1:
                # Find the third occurrence relative to the first
                third_pos = nxt[second_pos]
                if third_pos != -1:
                    # distance = (j-i) + (k-j) + (k-i) = 2 * (k-i)
                    ans = min(ans, third_pos - i)

        # ans * 2 gives the total pairwise absolute difference sum
        return -1 if ans == n + 1 else ans * 2
```

---

## Example Walkthrough

**Input:** `nums = [1, 2, 1, 3, 1, 1]`

1.  **Preprocessing (`nxt` array):**
    - `nxt[0] = 2` (next 1 is at index 2)
    - `nxt[2] = 4` (next 1 is at index 4)
    - `nxt[4] = 5` (next 1 is at index 5)
2.  **Iteration:**
    - At `i=0`: `second=2, third=4`. Distance = $2 \times (4 - 0) = 8$.
    - At `i=2`: `second=4, third=5`. Distance = $2 \times (5 - 2) = 6$.
3.  **Result:** `6`.

---

## Complexity Analysis

* **Time Complexity:** $O(N)$
    - One backward pass to build the `nxt` array: $O(N)$.
    - One forward pass to find the minimum distance: $O(N)$.
* **Space Complexity:** $O(N)$
    - We use an array `nxt` of size $N$ and a hash map `occur` that can store up to $N$ unique values.

---

## Tags
`Array`, `Hash-Table`, `Linear-Scan`, `Greedy`, `Optimization`