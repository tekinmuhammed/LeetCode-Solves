# 1306. Jump Game III

**Difficulty:** Medium
**Problem Link:** [LeetCode 1306](https://leetcode.com/problems/jump-game-iii/description/)

---

## Problem 
Given an array of non-negative integers `arr`, you are initially positioned at `start` index of the array. When you are at index `i`, you can jump to `i + arr[i]` or `i - arr[i]`, check if you can reach to **any** index with value 0.

Notice that you can not jump outside of the array at any time.

---

# Approach 

This problem can be modeled as a graph traversal where each index is a node, and the directed edges are the possible jumps (`i + arr[i]` and `i - arr[i]`). We need to find if there is a path from the `start` node to any node with a value of `0`.

The provided solution uses an **Iterative Depth-First Search (DFS)** approach using a `stack`.

Steps: 

1. **Initialization:** 
   * Create a `visited` set to keep track of the indices we have already explored. This is crucial to prevent infinite loops (e.g., jumping back and forth between two indices).
   * Initialize a `stack` with the `start` index.
2. **DFS Traversal:**
   * While the `stack` is not empty, pop the top index `i`.
   * **Boundary & Cycle Check:** If the index `i` is out of bounds (`i < 0` or `i >= len(arr)`) or if it has already been explored (`i in visited`), we `continue` to the next element in the stack.
   * **Target Check:** If the value at the current index `arr[i]` is `0`, we have successfully found a valid path. Return `True`.
   * **Mark & Explore:** Add the current index `i` to the `visited` set. Then, push the two possible next destinations (`i + arr[i]` and `i - arr[i]`) onto the `stack`.
3. **Termination:** If the `stack` becomes empty and we haven't returned `True`, it means all reachable indices have been explored and no `0` was found. Return `False`.

---

# Example Walkthrough 

Consider `arr = [4, 2, 3, 0, 3, 1, 2]` and `start = 5`.

* **Initialization:** `stack = [5]`, `visited = {}`
* **Step 1:** Pop `5`. `arr[5] = 1`. Not 0.
  * Add to visited: `visited = {5}`
  * Push next jumps: `5 + 1 = 6`, `5 - 1 = 4`.
  * `stack = [6, 4]`
* **Step 2:** Pop `4`. `arr[4] = 3`. Not 0.
  * Add to visited: `visited = {5, 4}`
  * Push next jumps: `4 + 3 = 7`, `4 - 3 = 1`.
  * `stack = [6, 7, 1]`
* **Step 3:** Pop `1`. `arr[1] = 2`. Not 0.
  * Add to visited: `visited = {5, 4, 1}`
  * Push next jumps: `1 + 2 = 3`, `1 - 2 = -1`.
  * `stack = [6, 7, 3, -1]`
* **Step 4:** Pop `-1`. Out of bounds! `continue`.
* **Step 5:** Pop `3`. `arr[3] = 0`.
  * Target found! Return `True`.

---

# Complexity Analysis 

Time Complexity 

O(N) 

Where `N` is the length of the array `arr`. In the worst-case scenario, we might visit every single index in the array exactly once. The `visited` set ensures we never process the same index twice, guaranteeing a linear time bound.

Space Complexity 

O(N)

The space complexity is $O(N)$ because, in the worst-case scenario, the `visited` set will store all `N` indices, and the `stack` can also grow proportionally to `N` if there are many valid jump paths pending exploration.

---

# Code 

```python
class Solution(object):
    def canReach(self, arr, start):
        visited = set()
        stack = [start]

        while stack:
            i = stack.pop()

            if i < 0 or i >= len(arr) or i in visited:
                continue

            if arr[i] == 0:
                return True

            visited.add(i)

            stack.append(i + arr[i])
            stack.append(i - arr[i])

        return False
```