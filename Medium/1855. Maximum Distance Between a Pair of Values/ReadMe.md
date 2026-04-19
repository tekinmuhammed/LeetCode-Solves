# 1855. Maximum Distance Between a Pair of Values

**Difficulty:** Medium  
**Problem Link:** [LeetCode 1855](https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/)

---

## Problem Description

You are given two **non-increasing** integer arrays `nums1` and `nums2`. A pair of indices $(i, j)$ is **valid** if:
1. $0 \le i < nums1.length$
2. $0 \le j < nums2.length$
3. $i \le j$
4. $nums1[i] \le nums2[j]$

The **distance** of the pair is $j - i$. Return the **maximum distance** of any valid pair $(i, j)$. If there are no valid pairs, return $0$.

---

## Approach: Two Pointers (Greedy)

Since both arrays are already sorted in **non-increasing** order, we can use a two-pointer approach to find the maximum distance efficiently without checking every possible pair.

### Key Ideas:
1.  **Dual Pointers:** Initialize pointer `i` for `nums1` and pointer `j` for `nums2`.
2.  **Valid Pair Expansion:** If `nums1[i] <= nums2[j]`, the condition is satisfied. Since we want to maximize $j - i$, we keep `i` fixed and increment `j` to see if a further index in `nums2` also satisfies the condition.
3.  **Invalid Pair Adjustment:** If `nums1[i] > nums2[j]`, the current `nums1[i]` is too large. Since `nums2` is non-increasing, any index after `j` will have an even smaller value, so we must increment `i` to find a smaller value in `nums1`.
4.  **Constraint $i \le j$:** If `j` ever falls behind `i`, we move `j` to match `i` to satisfy the problem's index constraint.



---

## Code

```python
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        i = 0
        j = 0
        max_dist = 0
        
        # Traverse both arrays using two pointers
        while i < len(nums1) and j < len(nums2):
            # Check the primary condition: nums1[i] <= nums2[j]
            if nums1[i] <= nums2[j]:
                # Update maximum distance
                max_dist = max(max_dist, j - i)
                # Try to increase j to find a larger distance
                j += 1
            else:
                # nums1[i] is too large, move to a smaller value in nums1
                i += 1
            
            # Ensure j is at least as large as i (i <= j constraint)
            if j < i:
                j = i
                
        return max_dist
```

---

## Example Walkthrough

**Input:** `nums1 = [55,30,5,4,2], nums2 = [100,20,10,10,5]`

1.  **i=0 (55), j=0 (100):** $55 \le 100$ is True. `max_dist = 0`. $j \rightarrow 1$.
2.  **i=0 (55), j=1 (20):** $55 \le 20$ is False. $i \rightarrow 1$.
3.  **i=1 (30), j=1 (20):** $30 \le 20$ is False. $i \rightarrow 2$.
4.  **i=2 (5), j=2 (10):** $5 \le 10$ is True. `max_dist = 0`. $j \rightarrow 3$.
5.  **i=2 (5), j=3 (10):** $5 \le 10$ is True. `max_dist = 1`. $j \rightarrow 4$.
6.  **i=2 (5), j=4 (5):** $5 \le 5$ is True. `max_dist = 2`. $j \rightarrow 5$. (Loop ends)

**Output:** `2`

---

## Complexity Analysis

* **Time Complexity:** $O(n + m)$
    - We iterate through `nums1` (length $n$) and `nums2` (length $m$) at most once. Each pointer only moves forward.
* **Space Complexity:** $O(1)$
    - We only use a few constant-sized integer variables for pointers and the result.

---

## Tags
Two-Pointers, Array, Binary-Search, Greedy