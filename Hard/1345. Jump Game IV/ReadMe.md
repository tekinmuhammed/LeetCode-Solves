# 1345. Jump Game IV

**Difficulty:** Hard
**Problem Link:** [LeetCode 1345](https://leetcode.com/problems/jump-game-iv/description/)

---

## Problem 
Given an array of integers `arr`, you are initially positioned at the first index of the array.

In one step you can jump from index `i` to index:
* `i + 1` where: `i + 1 < arr.length`. 
* `i - 1` where: `i - 1 >= 0`.
* `j` where: `arr[i] == arr[j]` and `i != j`.

Return the **minimum number of steps** to reach the last index of the array.

---

# Approach 

The problem asks for the minimum number of steps to reach a target in an unweighted graph where nodes are array indices. The standard and most efficient algorithm for finding the shortest path in an unweighted graph is **Breadth-First Search (BFS)**.

Steps:

1. **Edge Case:** If the array length is 1 or less, we are already at the end. Return `0`. 
2. **Build the Graph (Value to Indices Map):**  
   * We iterate through the array and create a hash map (`graph`) where the keys are the array values and the values are lists of indices where these values appear. This allows us to handle the $O(1)$ lookup for the teleportation jumps `arr[i] == arr[j]`.
3. **Initialize BFS:**
   * We use an array `curs` to represent the current layer of nodes we are exploring (starting with index `0`).
   * We maintain a `visited` set to ensure we don't process the same index twice.
   * `step` counter tracks the depth/number of jumps.
4. **Level-by-Level Traversal (BFS):** 
   * For every node in the current layer, check if it's the last index (`n - 1`). If so, return the `step`. 
   * **Explore Same Value Jumps:** Look up all indices that share the same value as the current node. Add unvisited indices to the next layer (`nex`) and mark them as visited. 
   * **CRITICAL OPTIMIZATION (`graph[arr[node]].clear()`):** Once we have evaluated all jumps for a specific value, we **must** clear the list in the hash map. If we don't, an array like `[7, 7, 7, 7, ..., 7]` would cause an $O(N^2)$ Time Limit Exceeded (TLE) error as the algorithm would repeatedly iterate through the same large list. 
   * **Explore Adjacent Jumps:** Check `node - 1` and `node + 1`. If they are valid bounds and unvisited, add them to `nex` and mark them.
5. **Move to Next Layer:** Once the current layer is fully processed, replace `curs` with `nex` and increment `step`.

---

# Example Walkthrough 

Consider `arr = [100, -23, -23, 404, 100, 23, 23, 23, 3, 404]`
Length `n = 10`. Start at index `0` (value `100`).

* **Graph creation:** 
  * `100: [0, 4]`
  * `-23: [1, 2]`
  * `404: [3, 9]`
  * ...and so on.
* **Step 0:** `curs = [0]` (value `100`). 
* **Step 1:** Pop `0`.  
  * Same value jumps: index `4` (value `100`). Add `4` to `nex`. Clear `graph[100]`.
  * Adjacent jumps: `0 + 1 = 1`. Add `1` to `nex`.
  * Next layer: `curs = [4, 1]`.
* **Step 2:**
  * Process `4` (value `100`): Same value list is empty (cleared!). Adjacent jumps: `3`, `5`. Add to `nex`.
  * Process `1` (value `-23`): Same value jumps: `2`. Add to `nex`. Clear `graph[-23]`. Adjacent jump: `0` (visited), `2` (already added).
  * Next layer: `curs = [3, 5, 2]`.
* **Step 3:**
  * Process `3` (value `404`): Same value jump: `9` (value `404`). Add `9` to `nex`. Clear `graph[404]`.
  * ... 
* **Step 4:** 
  * Next layer `curs` will contain `9`.
  * Process `9`: It is `n - 1`. Return `step = 3`.

Path: `Index 0 -> Index 4 -> Index 3 -> Index 9`. Minimum jumps: 3.

--- 

# Complexity Analysis 

Time Complexity 

O(N) 

Where `N` is the length of the array. Building the hash map takes $O(N)$ time. During the BFS, every index is added to the `curs` layer at most once because of the `visited` set. Furthermore, because we clear the hash map entry (`graph[arr[node]].clear()`) after using it, the edges representing same-value jumps are processed exactly once across the entire algorithm. Thus, the total time is strictly linear. 

Space Complexity 

O(N) 

We store a hash map `graph` containing all indices, taking $O(N)$ space. The `visited` set and BFS layers (`curs`, `nex`) can also contain up to `N` elements in the worst case. Overall space complexity is $O(N)$.

---

# Code 

```python
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0

        graph = {}
        for i in range(n):
            if arr[i] in graph:
                graph[arr[i]].append(i)
            else:
                graph[arr[i]] = [i]

        curs = [0]  # store current layers 
        visited = {0}
        step = 0

        # when current layer exists 
        while curs:
            nex = []

            # iterate the layer 
            for node in curs:
                # check if reached end 
                if node == n-1:
                    return step

                # check same value 
                for child in graph[arr[node]]:
                    if child not in visited:
                        visited.add(child)
                        nex.append(child)

                # clear the list to prevent redundant search 
                graph[arr[node]].clear()

                # check neighbors 
                for child in [node-1, node+1]:
                    if 0 <= child < len(arr) and child not in visited:
                        visited.add(child)
                        nex.append(child)

            curs = nex
            step += 1

        return -1
```