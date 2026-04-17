# 3761. Minimum Absolute Distance Between Mirror Pairs

**Difficulty:** Medium
**Problem Link:** [LeetCode 3761](https://leetcode.com/problems/minimum-absolute-distance-between-mirror-pairs/description/)

---

## Problem Description 

You are given an array of integers `nums`. A **mirror pair** is defined as two indices $(i, j)$ such that $i \neq j$ and `nums[i]` is the **mirror** of `nums[j]`. A mirror of a number is obtained by reversing its digits (e.g., the mirror of 123 is 321, and the mirror of 10 is 1).

Your goal is to find the **minimum absolute distance** $|i - j|$ between any mirror pair in the array. If no mirror pairs exist, return -1.

---

## Approach: One-Pass Hash Map (Reverse-Storage) 

To find the minimum distance efficiently, we can use a hash map to store the indices of numbers we have already seen. However, instead of storing the number itself, we store its **mirror** to facilitate an immediate match when we encounter the counterpart.

### Key Ideas:
1.  **Mirror Identification:** A number $A$ and a number $B$ form a mirror pair if $B = \text{reverse}(A)$.
2.  **Look-ahead Storage:** As we iterate through the array:
    - We check if the current number `num` exists in our dictionary `prev`. If it does, it means we previously encountered a number whose mirror is the current `num`.
    - We then calculate the distance $i - \text{prev}[num]$ and update our minimum answer.
    - Crucially, we store the mirror of the current number: `prev[reverse(num)] = i`. This sets up a "trap" for any future occurrence of its mirror image.
3.  **Handling Leading Zeros:** By converting the reversed string back to an integer (`int(str(num)[::-1])`), we naturally handle cases like "10" becoming "1", which is standard for integer-based mirror problems.

---

## Code

```python
class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        # prev maps a "target mirror value" to its most recent index
        prev = dict()
        ans = float('inf')
        
        for i, num in enumerate(nums):
            # Check if current number matches a previously stored mirror requirement
            if num in prev:
                ans = min(ans, i - prev[num])
            
            # Store the mirror of the current number to be found by future elements
            mirror_val = int(str(num)[::-1])
            prev[mirror_val] = i
            
        return -1 if ans == float('inf') else ans
```

---

## Example Walkthrough

**Input:** `nums = [12, 45, 21, 54]`

1.  **i = 0, num = 12:** `12` not in `prev`. Store `prev[21] = 0`.
2.  **i = 1, num = 45:** `45` not in `prev`. Store `prev[54] = 1`.
3.  **i = 2, num = 21:** `21` **is** in `prev`. `ans = min(inf, 2 - 0) = 2`. Store `prev[12] = 2`.
4.  **i = 3, num = 54:** `54` **is** in `prev`. `ans = min(2, 3 - 1) = 2`. Store `prev[45] = 3`.

**Output:** `2`

---

## Complexity Analysis

* **Time Complexity:** $O(N \times D)$
    - $N$ is the number of elements in `nums`.
    - $D$ is the maximum number of digits in an element (to perform the string reversal and integer conversion). In most cases, $D$ is small (e.g., $\le 10$ for 32-bit integers), effectively making this $O(N)$.
* **Space Complexity:** $O(N)$
    - In the worst case, we store the mirror of every unique number in the hash map.

---

## Tags
`Hash-Table`, `String`, `Math`, `Array`, `Minimum-Distance`