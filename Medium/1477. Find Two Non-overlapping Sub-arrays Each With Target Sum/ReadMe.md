# 1477. Find Two Non-overlapping Sub-arrays Each With Target Sum

**Difficulty:** Medium
**Problem Link:** [LeetCode 1477](https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/description/)

---

## Problem
Given an array of integers `arr` and an integer `target`. 

You have to find **two non-overlapping sub-arrays** of `arr` each with a sum equal to `target`. There can be multiple answers; you need to find two sub-arrays such that the sum of their lengths is **minimum**.

Return the minimum sum of the lengths of the two sub-arrays, or return `-1` if you cannot find such two sub-arrays.

Example:

Input  
arr = [3,2,2,4,3], target = 3  

Output  
2  

Explanation  
Only two sub-arrays have sum = 3 ([3] and [3]). The sum of their lengths is 1 + 1 = 2.

---

# Approach

To find subarrays that sum to a specific target efficiently, we use a **Prefix Sum combined with a Hash Map (`pos`)**. To ensure the subarrays are non-overlapping and have the minimum total length, we use **Dynamic Programming** on the fly. 

A brilliant optimization in your code is that it **modifies the input array `arr` in place** to act as the DP array. Here is how it works:

1. **Prefix Sum Map**: We keep a running sum `s`. We store `pos[s] = i`, which means the prefix sum `s` was seen at index `i`.
2. **Finding a Valid Subarray**: As we iterate, if `s - target` exists in our `pos` map at index `j`, it means the subarray from index `j + 1` to `i` sums exactly to `target`. Its length is `i - j`.
3. **Finding a Preceding Subarray (The DP part)**: To get two *non-overlapping* arrays, we need the length of the shortest valid subarray that ended **at or before index `j`**. 
   * As we progress, we keep track of the minimum length seen so far in `min_l`.
   * We overwrite `arr[i] = min_l`. This cleverly transforms `arr` into a DP array where `arr[i]` stores the shortest valid subarray length found up to index `i`.
   * Thus, the best preceding subarray length is simply `arr[j]`.
4. **Updating the Answer**: We update our global answer `ans` with `length + arr[j]`. 
   *(Note: If `j == -1`, it means our current subarray starts at the very beginning of the array (index 0). There can be no preceding subarray, so we add `n` to invalidate this combination.)*

---

# Code

```python
class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        pos = {0: -1}
        n = len(arr)
        s = 0
        ans = n + 1
        min_l = n
        
        for i, x in enumerate(arr):
            s += x
            
            # If we find a subarray summing to target ending at i
            if s - target in pos:
                j = pos[s - target]
                length = i - j
                
                # Minimum total length = current length + best length before it
                ans = min(ans, length + (n if j == -1 else arr[j]))
                
                # Update the minimum length of a single subarray seen so far
                min_l = min(min_l, length)
                
            # Overwrite arr[i] to act as our DP state
            arr[i] = min_l
            pos[s] = i
            
        return -1 if ans == n + 1 else ans
```

---

# Example Walkthrough

Let's trace `arr = [3,2,2,4,3]`, `target = 3`, `n = 5`

* `pos = {0: -1}`, `min_l = 5`, `ans = 6`

1. **i = 0, x = 3**
   * `s = 3`. `s - target = 0`. Exists in `pos` at `j = -1`.
   * `length = 0 - (-1) = 1`.
   * `ans = min(6, 1 + 5)` (since j == -1, we use n=5) $\rightarrow$ `ans = 6`.
   * `min_l = min(5, 1) = 1`.
   * `arr[0] = 1`. `pos = {0: -1, 3: 0}`.
   
2. **i = 1, x = 2**
   * `s = 5`. `5 - 3 = 2` (not in `pos`).
   * `arr[1] = 1` (carries forward `min_l`). `pos[5] = 1`.

3. **i = 2, x = 2**
   * `s = 7`. `7 - 3 = 4` (not in `pos`).
   * `arr[2] = 1`. `pos[7] = 2`.

4. **i = 3, x = 4**
   * `s = 11`. `11 - 3 = 8` (not in `pos`).
   * `arr[3] = 1`. `pos[11] = 3`.

5. **i = 4, x = 3**
   * `s = 14`. `14 - 3 = 11`. Exists in `pos` at `j = 3`.
   * `length = 4 - 3 = 1`.
   * `ans = min(6, length + arr[3])` $\rightarrow$ `min(6, 1 + 1) = 2`.
   * `min_l = min(1, 1) = 1`.
   * `arr[4] = 1`. `pos[14] = 4`.

Final `ans = 2`. (Valid, less than `n+1`). Return 2.

---

# Complexity Analysis

Time Complexity

$\mathcal{O}(N)$

We iterate through the array `arr` exactly once. Dictionary lookups (checking `s - target in pos` and inserting) operate in $\mathcal{O}(1)$ average time. Thus, the total time complexity is strictly linear.

Space Complexity

$\mathcal{O}(N)$

We repurpose the input array `arr` as our DP table, which saves space. However, we use a Hash Map (`pos`) to store the prefix sums. In the worst case, all prefix sums are unique, so the Hash Map takes $\mathcal{O}(N)$ space.