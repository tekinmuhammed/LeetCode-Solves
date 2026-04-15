# 2515. Shortest Distance to Target String in a Circular Array

**Difficulty:** Easy
**Problem Link:** [LeetCode 2515](https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/description/)

---

## Problem Description

You are given a **circular array** of strings `words` and a string `target`. You are also given a `startIndex`.

A **circular array** means that the end of the array connects back to the beginning. You can move one step to the left or right at each index.

Return the **shortest distance** needed to reach the string `target`. If the string `target` does not exist in `words`, return `-1`.

---

## Approach: Linear Scan with Circular Distance Logic

Since the array is circular, for any given index $i$ where `words[i] == target`, there are two ways to reach it from `startIndex`:
1.  **Direct Distance:** Moving linearly through the array.
2.  **Wrap-around Distance:** Moving in the opposite direction through the boundary of the array.

### Key Ideas:
1.  **Linear Distance ($d$):** The absolute difference between the current index and the start index: $d = |i - startIndex|$.
2.  **Circular Distance:** Since the total number of elements is $n$, the distance going the "other way" around the circle is $n - d$.
3.  **Minimization:** For every occurrence of the `target`, we take $\min(d, n - d)$. The overall answer is the minimum of these values across all occurrences.



---

## Code

```python
class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        """
        :type words: List[str]
        :type target: str
        :type startIndex: int
        :rtype: int
        """
        n = len(words)
        # Initialize ans with n, as the max possible distance in a circular array is n // 2
        ans = n 
        
        for i, word in enumerate(words):
            if word == target:
                # Calculate the direct distance
                d = abs(i - startIndex)
                # Compare direct distance with the wrap-around distance (n - d)
                ans = min(ans, d, n - d)
        
        # If ans was never updated, the target was not found
        return ans if ans < n else -1
```

---

## Example Walkthrough

**Input:** `words = ["hello", "i", "am", "leetcode", "hello"], target = "hello", startIndex = 1`

1.  **Array length ($n$):** 5. `startIndex = 1`.
2.  **Occurrence at $i=0$:**
    - $d = |0 - 1| = 1$.
    - Wrap-around: $5 - 1 = 4$.
    - $\min(1, 4) = 1$. `ans = 1`.
3.  **Occurrence at $i=4$:**
    - $d = |4 - 1| = 3$.
    - Wrap-around: $5 - 3 = 2$.
    - $\min(3, 2) = 2$. `ans` stays `1`.

**Output:** `1`

---

## Complexity Analysis

* **Time Complexity:** $O(n)$
    - We perform a single pass through the `words` array to find all occurrences of the `target`.
* **Space Complexity:** $O(1)$
    - We only use a few integer variables to track indices and the minimum distance.

---

## Tags
`Array`, `String`, `Circular-Array`, `Linear-Scan`, `Math`