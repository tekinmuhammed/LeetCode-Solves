# 1871. Jump Game VII

**Difficulty:** Medium
**Problem Link:** [LeetCode 1871](https://leetcode.com/problems/jump-game-vii/description/)

---

## Problem
You are given a **0-indexed** binary string `s` and two integers `minJump` and `maxJump`. In the beginning, you are standing at index `0`, which is equal to `'0'`. You can move from index `i` to index `j` if the following conditions are fulfilled:
* `i + minJump <= j <= min(i + maxJump, s.length - 1)`
* `s[j] == '0'`

Return `true` if you can reach index `s.length - 1` in `s`, or `false` otherwise.

---

# Approach

A naive Dynamic Programming (DP) approach would check every index `j` and look back at all valid previous indices `i` in the window `[j - maxJump, j - minJump]` to see if any of them are reachable. However, this takes $O(N \times (\text{maxJump} - \text{minJump}))$ time, which leads to a Time Limit Exceeded (TLE) error for large inputs.

To optimize this to $O(N)$, we use **Dynamic Programming combined with a Prefix Sum array**.

Steps:

1. **State Definition:** * `f[i]`: A boolean/integer array where `f[i] = 1` if index `i` is reachable, and `0` otherwise.
   * `pre[i]`: A prefix sum array that keeps track of the total number of reachable indices from index `0` up to `i`.
2. **Initialization:** * We start at index `0`, so `f[0] = 1`.
   * For all indices before `minJump`, we cannot jump to them, but we initialize `pre[i] = 1` for the range `[0, minJump)` because index `0` is the only reachable spot in that prefix.
3. **Optimized Window Query:**
   * For every index `i` from `minJump` to the end of the string, we calculate the valid jump window boundaries: `left = i - maxJump` and `right = i - minJump`.
   * If `s[i] == '0'`, we need to know if there is *at least one* reachable index in the window `[left, right]`.
   * Instead of a slow loop, we use our prefix sum array: `total = pre[right] - pre[left - 1]`. If this `total > 0`, it mathematically guarantees there is a valid launchpad for our jump!
   * We update `f[i]` based on this condition.
4. **Update Prefix Sum:** * Regardless of whether `i` was reachable or not, we update the prefix sum for the next iterations: `pre[i] = pre[i - 1] + f[i]`.
5. **Result:** Return `True` if `f[n - 1]` is `1`.
 
--- 
 
# Example Walkthrough

Consider `s = "011010"`, `minJump = 2`, `maxJump = 3`.
Length `n = 6`.

* **Initialization:**
  * `f[0] = 1`
  * `pre[0] = 1`, `pre[1] = 1` (since `minJump = 2`, we prefill up to index 1).
* **i = 2 (s[2] = '1'):**
  * It's a '1', so we can't land here. `f[2] = 0`.
  * `pre[2] = pre[1] + f[2] = 1 + 0 = 1`.
* **i = 3 (s[3] = '0'):**
  * `left = 3 - 3 = 0`, `right = 3 - 2 = 1`.
  * `total = pre[1] - pre[-1] (treated as 0) = 1 - 0 = 1`.
  * Since `total > 0`, `f[3] = 1` (reachable from index 0).
  * `pre[3] = pre[2] + f[3] = 1 + 1 = 2`.
* **i = 4 (s[4] = '1'):**
  * It's a '1'. `f[4] = 0`.
  * `pre[4] = pre[3] + f[4] = 2 + 0 = 2`.
* **i = 5 (s[5] = '0'):**
  * `left = 5 - 3 = 2`, `right = 5 - 2 = 3`.
  * `total = pre[3] - pre[1] = 2 - 1 = 1`.
  * Since `total > 0`, `f[5] = 1` (reachable from index 3).
  * `pre[5] = pre[4] + 1 = 3`.
 
Finally, return `f[5]` which is `1` (`True`).
 
--- 
 
# Complexity Analysis 
 
Time Complexity 
 
O(N) 
 
Where `N` is the length of the string `s`. We iterate through the string exactly once. Inside the loop, the prefix sum calculation `pre[right] - pre[left - 1]` takes $O(1)$ constant time. Thus, the overall time complexity is strictly linear.
 
Space Complexity 
 
O(N) 
 
We use two arrays, `f` and `pre`, both of size `N`. This requires $O(N)$ extra space. *(Note: This can theoretically be optimized to O(maxJump) space using a sliding window sum, but O(N) is well within standard limits).*

---

# Code

```python
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        f, pre = [0] * n, [0] * n
        f[0] = 1
        
        # since we start dynamic programming from i=minJump, we need to precompute the prefix sums for the part [0, minJump) 
        for i in range(minJump):
            pre[i] = 1
            
        for i in range(minJump, n):
            left, right = i - maxJump, i - minJump
            
            if s[i] == "0":
                total = pre[right] - (0 if left <= 0 else pre[left - 1])
                f[i] = int(total != 0)
                
            pre[i] = pre[i - 1] + f[i]

        return bool(f[n - 1])
```