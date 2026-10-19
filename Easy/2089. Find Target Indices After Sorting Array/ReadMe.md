# 2089. Find Target Indices After Sorting Array

**Difficulty:** Easy  
**Problem Link:** [LeetCode 2089](https://leetcode.com/problems/find-target-indices-after-sorting-array/description/)

---

## Problem
You are given a 0-indexed integer array `nums` and a target element `target`.

A **target index** is an index `i` such that `nums[i] == target` after sorting `nums` in non-decreasing order.

Return a list of the target indices of `nums` after sorting it. If there are no target indices, return an empty list. The returned list must be sorted in increasing order.

Example:

Input  
nums = [1, 2, 5, 2, 3], target = 2  

Output  
[1, 2]  

Explanation  
After sorting, `nums` is `[1, 2, 2, 3, 5]`.  
The indices where `nums[i] == 2` are `1` and `2`.

---

## Approach

While a naïve approach would involve sorting the entire array ($\mathcal{O}(N \log N)$) and then scanning for the target, we can solve this much more efficiently in **$\mathcal{O}(N)$ time without actually sorting**.

The final position of the `target` elements in a sorted array depends entirely on two counts:
1. **`cnt1`**: The count of elements strictly smaller than `target`. This tells us the starting index where the target elements will begin.
2. **`cnt2`**: The count of elements exactly equal to `target`. This tells us how many consecutive positions the target will occupy.

Steps:
1. Iterate through `nums` once to compute `cnt1` (elements `< target`) and `cnt2` (elements `== target`).
2. Generate the resulting index list as a contiguous range starting from `cnt1` up to `cnt1 + cnt2 - 1` using `list(range(cnt1, cnt1 + cnt2))`.
3. Return the resulting index array.

---

## Example Walkthrough

Let's trace `nums = [1, 2, 5, 2, 3]`, `target = 2`

1. **Iteration**:
   * `num = 1`: `< 2` $\rightarrow$ `cnt1 = 1`
   * `num = 2`: `== 2` $\rightarrow$ `cnt2 = 1`
   * `num = 5`: `> 2` (ignored)
   * `num = 2`: `== 2` $\rightarrow$ `cnt2 = 2`
   * `num = 3`: `> 2` (ignored)
2. **Final Counts**:
   * `cnt1 = 1` (one element is smaller than 2)
   * `cnt2 = 2` (two elements equal 2)
3. **Range Generation**:
   * `list(range(1, 1 + 2))` $\rightarrow$ `list(range(1, 3))` $\rightarrow$ `[1, 2]`.

Result: `[1, 2]`

---

## Complexity Analysis

**Time Complexity:** $\mathcal{O}(N)$  
Where $N$ is the length of the array `nums`. We traverse the array a single time to count the elements. Generating the range takes time proportional to the number of target occurrences (`cnt2`), which is bounded by $N$. Thus, the time complexity is strictly linear, outperforming any sorting-based approach.

**Space Complexity:** $\mathcal{O}(K)$  
Where $K$ is the number of occurrences of `target` in `nums` (which is stored in the output array `res`). Auxiliary space outside of the output list is $\mathcal{O}(1)$.

---

## Code

```python
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        cnt1 = 0  # Number of elements less than target
        cnt2 = 0  # Number of elements equal to target
        for num in nums:
            if num < target:
                cnt1 += 1
            elif num == target:
                cnt2 += 1
        res = list(range(cnt1, cnt1 + cnt2))  # Array of indices
        return res
```