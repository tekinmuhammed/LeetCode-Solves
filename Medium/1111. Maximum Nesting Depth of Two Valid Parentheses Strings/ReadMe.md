# 1111. Maximum Nesting Depth of Two Valid Parentheses Strings

**Difficulty:** Medium  
**Problem Link:** [LeetCode 1111](https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/description/)

---

## Problem
A string is a valid parentheses string (denoted VPS) if and only if it consists of `"("` and `")"` characters only, and meets standard matching rules. The nesting depth `depth(S)` of any VPS `S` is the maximum number of nested parentheses at any point.

You are given a VPS `seq`. You must split `seq` into two disjoint subsequences `A` and `B`, such that `A` and `B` are both VPS's, and the maximum of their depths (`max(depth(A), depth(B))`) is **minimized**.

Return an `answer` array (of length equal to the length of `seq`) where `answer[i]` is `0` if `seq[i]` is assigned to `A`, and `1` if `seq[i]` is assigned to `B`. If there are multiple solutions, return any of them.

Example:

Input  
seq = "(()())"  

Output  
[0, 1, 1, 1, 1, 0] (or [1, 0, 0, 0, 0, 1])

Explanation  
The depth of the string is 2. To minimize the maximum depth of the split strings, we can assign the outer parentheses to group 0 and the inner parentheses to group 1. Both resulting strings will have a maximum depth of 1.

---

# Approach

To minimize the maximum depth of the two separated strings, we need to distribute the nesting depth as evenly as possible between group `A` and group `B`. 

The simplest and most elegant way to achieve this is to distribute the parentheses based on the parity (odd/even) of their current depth:
* Parentheses at an **odd** depth go to group `1`.
* Parentheses at an **even** depth go to group `0`.

Steps:
1. Initialize a running depth counter `d = 0`.
2. Iterate through each character in the string.
3. If the character is an open parenthesis `(`, it increases the nesting level. We increment `d` first, and then assign it to a group based on `d % 2`.
4. If the character is a close parenthesis `)`, it belongs to the *current* nesting level before closing it. We assign it to a group based on `d % 2`, and then decrement `d`.
5. This guarantees that matching pairs are assigned to the same group, and the depth is split perfectly in half.

---

# Code

```python
class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        ans = []
        d = 0
        for c in seq:
            if c == "(":
                d += 1
                ans.append(d % 2)
            if c == ")":
                ans.append(d % 2)
                d -= 1
        return ans
```

---

# Example Walkthrough

Let's trace `seq = "(()())"`

* **Initial state**: `d = 0`, `ans = []`
* **c = '('**: `d` becomes 1. `1 % 2 = 1`. `ans = [1]`
* **c = '('**: `d` becomes 2. `2 % 2 = 0`. `ans = [1, 0]`
* **c = ')'**: `2 % 2 = 0`. `ans = [1, 0, 0]`. `d` becomes 1.
* **c = '('**: `d` becomes 2. `2 % 2 = 0`. `ans = [1, 0, 0, 0]`
* **c = ')'**: `2 % 2 = 0`. `ans = [1, 0, 0, 0, 0]`. `d` becomes 1.
* **c = ')'**: `1 % 2 = 1`. `ans = [1, 0, 0, 0, 0, 1]`. `d` becomes 0.

Result: `[1, 0, 0, 0, 0, 1]`

*(Note: The result string logic maps group A to 1 and B to 0 for odd/even depths, which is a perfectly valid alternative to the example output.)*

---

# Complexity Analysis

Time Complexity

$\mathcal{O}(N)$

We iterate through the string `seq` of length $N$ exactly once. Checking characters and appending to a list both take $\mathcal{O}(1)$ time. 

Space Complexity

$\mathcal{O}(N)$

We create an array `ans` of size $N$ to store the result. Since returning this array is required by the problem statement, the auxiliary space (excluding the output array) is $\mathcal{O}(1)$, but the overall space complexity is considered $\mathcal{O}(N)$.