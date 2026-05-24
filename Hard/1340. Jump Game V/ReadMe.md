# 1340. Jump Game V

**Difficulty:** Hard  
**Problem Link:** [LeetCode 1340](https://leetcode.com/problems/jump-game-v/description/)

---

## Problem
Given an array of integers `arr` and an integer `d`. In one step you can jump from index `i` to index:
* `i + x` where: `i + x < arr.length` and `0 < x <= d`.
* `i - x` where: `i - x >= 0` and `0 < x <= d`.

In addition, you can only jump from index `i` to index `j` if `arr[i] > arr[j]` and `arr[i] > arr[k]` for all indices `k` between `i` and `j` (more strictly, you cannot jump over or onto elements that are greater than or equal to the current element).

You can choose any index of the array as your starting point.

Return the **maximum number of indices** you can visit.

---

# Approach

This problem is a classic example of finding the longest path in a Directed Acyclic Graph (DAG). Because you can only jump from a higher element to a strictly lower element, it is impossible to jump back and form a cycle. 

To solve this efficiently, we use **Depth-First Search (DFS) with Memoization** (also known as Top-Down Dynamic Programming).

Steps:

1. **State Definition:** We use a dictionary `seen` where `seen[pos]` stores the maximum number of jumps we can make starting from index `pos`.
2. **Base Case & Memoization:** In our `dfs(pos)` function, if `pos` is already in `seen`, we simply return its value to avoid redundant calculations.
3. **Explore Left Jumps:**
   * We iterate to the left (`i = pos - 1`) up to a maximum distance of `d`.
   * **Blocking Rule:** If we encounter a building `arr[i]` that is taller than or equal to our current building `arr[pos]`, we must `break` (or stop the `while` loop). We cannot jump over it to reach smaller buildings further away.
   * For every valid jump, we recursively call `dfs(i)` and update our current max jumps: `seen[pos] = max(seen[pos], seen[i] + 1)`.
4. **Explore Right Jumps:**
   * We repeat the exact same logic iterating to the right (`i = pos + 1`) up to distance `d`.
5. **Global Search:** Since we can start at *any* index, we iterate through all indices from `0` to `len(arr) - 1`, calling `dfs(i)` on each.
6. **Result:** The answer is simply the maximum value stored in our `seen` dictionary.

---

# Example Walkthrough

Consider `arr = [6, 4, 1, 4, 6]`, `d = 2`.

* We evaluate starting at each index. Let's trace evaluating index `4` (value `6`).
* **From index 4 (value 6):**
  * Try left jump 1 step: Index `3` (value `4`). `6 > 4`, valid jump!
    * Recursively call `dfs(3)`.
    * **From index 3 (value 4):**
      * Try left jump 1 step: Index `2` (value `1`). `4 > 1`, valid jump!
        * Recursively call `dfs(2)`.
        * **From index 2 (value 1):** Both left and right jumps are blocked (no smaller elements). Max jumps = `1`.
      * `dfs(3)` updates: `1 + 1 = 2`. (No other valid jumps). Max jumps = `2`.
  * Try left jump 2 steps: Index `2` (value `1`). `6 > 1`, valid jump!
    * Recursively call `dfs(2)`. It returns `1` (from cache).
  * `dfs(4)` compares: jump to index 3 gives `2 + 1 = 3` jumps. Jump to index 2 gives `1 + 1 = 2` jumps. Max is `3`.
* By storing these results in the `seen` dictionary, we prevent recalculating `dfs(3)` or `dfs(2)` when we evaluate paths starting from index `0`.

---

# Complexity Analysis

Time Complexity

O(N \times d)

Where `N` is the length of the array. Because we memoize the results in the `seen` dictionary, the `dfs` logic is fully executed exactly once for each of the `N` indices. During this execution, we look at most `d` steps to the left and `d` steps to the right. Therefore, the total time complexity is bounded by $O(N \times d)$.

Space Complexity

O(N)

The space complexity is $O(N)$ due to the `seen` dictionary storing the result for each of the `N` indices, as well as the call stack for the DFS recursion, which can go at most `N` levels deep in the worst case (e.g., a strictly decreasing array).

---

# Code

```python
from typing import List

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        seen = dict()

        def dfs(pos):
            if pos in seen:
                return
            
            # Base case: we can always just visit the starting index itself
            seen[pos] = 1

            # Check valid jumps to the left
            i = pos - 1
            while i >= 0 and pos - i <= d and arr[pos] > arr[i]:
                dfs(i)
                seen[pos] = max(seen[pos], seen[i] + 1)
                i -= 1
                
            # Check valid jumps to the right
            i = pos + 1
            while i < len(arr) and i - pos <= d and arr[pos] > arr[i]:
                dfs(i)
                seen[pos] = max(seen[pos], seen[i] + 1)
                i += 1

        # Evaluate the maximum jumps starting from every possible index
        for i in range(len(arr)):
            dfs(i)

        return max(seen.values())
```