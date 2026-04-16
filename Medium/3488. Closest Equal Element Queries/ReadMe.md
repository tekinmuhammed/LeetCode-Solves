# 3488. Closest Equal Element Queries

**Difficulty:** Medium  
**Problem Link:** [LeetCode 3488](https://leetcode.com/problems/closest-equal-element-queries/)

---

## Problem Description

You are given an integer array `nums` and a list of `queries` where each query is an index. For each query index `i`, find the minimum distance to another element in the array that has the same value as `nums[i]`.

The array is treated as **circular**, meaning the distance between indices `i` and `j` is $\min(|i - j|, n - |i - j|)$. If no other element with the same value exists, return `-1`.

---

## Approach: Hashing + Binary Search + Circular Padding

To find the closest equal element efficiently for multiple queries, we can pre-calculate the positions of each number and use binary search.

### Key Ideas:
1.  **Grouping Positions:** We use a hash map (`defaultdict`) to store a sorted list of indices for each unique number in the array.
2.  **Handling Circularity via Padding:** Instead of using complex modulo logic for every query, we pad each list of positions:
    -   Add `pos[-1] - n` to the start: This represents the "previous" occurrence if we wrapped around the end.
    -   Add `pos[0] + n` to the end: This represents the "next" occurrence if we wrapped around the beginning.
3.  **Binary Search:** For a given query index, we find its location in the sorted `pos_list` using `bisect_left`.
4.  **Neighbor Comparison:** Once we have the index in the sorted list, the closest equal elements are the immediate neighbors in the padded list. The distance is simply the difference between the query index and these neighbors.
5.  **Edge Case:** If a number appears only once in the array, its padded `pos_list` will have a length of 3. In this case, there is no "other" equal element, so we return `-1`.

---

## Code

```python
from collections import defaultdict
import bisect

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        nums_pos = defaultdict(list)

        # Step 1: Group all indices for each number
        for i in range(n):
            nums_pos[nums[i]].append(i)

        # Step 2: Pad position lists to handle circular distances easily
        for pos in nums_pos.values():
            first_val = pos[0]
            last_val = pos[-1]
            pos.insert(0, last_val - n)
            pos.append(first_val + n)

        # Step 3: Process queries
        for i in range(len(queries)):
            query_idx = queries[i]
            val = nums[query_idx]
            pos_list = nums_pos[val]
            
            # If length is 3, it only contains (last-n, original, first+n) 
            # meaning the element was unique in the original array
            if len(pos_list) == 3:
                queries[i] = -1
                continue
            
            # Find the position of the query index in the sorted list
            pos = bisect.bisect_left(pos_list, query_idx)
            
            # The closest neighbors are at pos-1 and pos+1
            queries[i] = min(
                pos_list[pos + 1] - pos_list[pos],
                pos_list[pos] - pos_list[pos - 1]
            )

        return queries
```

---

## Example Walkthrough

**Input:** `nums = [1, 2, 1, 1, 2], queries = [0, 1]`

1.  **Positions:** - `1: [0, 2, 3]` $\rightarrow$ Padded: `[-2, 0, 2, 3, 5]`
    - `2: [1, 4]` $\rightarrow$ Padded: `[-1, 1, 4, 6]`
2.  **Query 0 (Index 0, Value 1):**
    - Neighbors of 0 in `[-2, 0, 2, 3, 5]` are -2 and 2.
    - Distances: `0 - (-2) = 2` and `2 - 0 = 2`. Min is 2.
3.  **Query 1 (Index 1, Value 2):**
    - Neighbors of 1 in `[-1, 1, 4, 6]` are -1 and 4.
    - Distances: `1 - (-1) = 2` and `4 - 1 = 3`. Min is 2.

---

## Complexity Analysis

* **Time Complexity:** $O(N + Q \log K)$
    - $O(N)$ to build the position map.
    - Each query takes $O(\log K)$ where $K$ is the frequency of the number being queried.
* **Space Complexity:** $O(N)$
    - To store the `nums_pos` dictionary containing all indices of the array.

---

## Tags
Array, Hash-Table, Binary-Search, Circular-Array, Pre-computation