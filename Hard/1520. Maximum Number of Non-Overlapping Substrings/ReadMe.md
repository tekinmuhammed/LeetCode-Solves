# 1520. Maximum Number of Non-Overlapping Substrings

**Difficulty:** Hard  
**Problem Link:** [LeetCode 1520](https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/description/)

---

## Problem
Given a string `s` of lowercase letters, you need to find the maximum number of **non-overlapping** substrings of `s` that meet the following conditions:

1. If a substring contains a certain character `c`, it must also contain **all occurrences** of `c` in the original string `s`.
2. The substrings must be non-overlapping.
3. You must maximize the number of substrings. If there are multiple valid solutions, return the one where the total length of the substrings is minimized.

Example:

Input  
s = "adefaddaccc"  

Output  
["e", "f", "ccc"]  

Explanation  
The valid substrings are "adefadda", "e", "f", and "ccc". 
Since we want the maximum number of non-overlapping substrings, we select "e", "f", and "ccc".

---

# Approach

This problem can be broken down into two main phases: **Interval Generation/Expansion** and **Greedy Interval Scheduling**.

1. **Find Initial Boundaries:** 
   First, we determine the initial `left` (first occurrence) and `right` (last occurrence) indices for each of the 26 lowercase English letters in the string `s`. 

2. **Expand Intervals to Make Them Valid:** 
   An interval for a character `c` initially spans from its first to its last occurrence. However, if there are *other* characters inside this interval, we must also include *their* first and last occurrences to satisfy the problem's condition. 
   * We iterate through the initial interval of each character.
   * If we find a character whose boundaries extend beyond our current `left` or `right`, we update our boundaries to encompass this new character as well.
   * Whenever we expand our boundary, we must restart our check from the new `left` to ensure all newly included characters are also fully enclosed.

3. **Greedy Scheduling:** 
   Once we have the valid, fully expanded intervals for all characters, the problem reduces to the classic **Interval Scheduling Maximization Problem**. 
   * We sort the intervals primarily by their `right` endpoints in ascending order. If two intervals end at the same place, we prefer the one that starts *later* (i.e., the shorter interval) by sorting the `left` endpoint in descending order.
   * We iterate through the sorted intervals and greedily pick the ones that do not overlap with our previously picked interval.

---

# Code

```python
class Seg:
    def __init__(self, left=-1, right=-1):
        self.left = left
        self.right = right

    def __lt__(self, rhs):
        return (
            self.left > rhs.left
            if self.right == rhs.right
            else self.right < rhs.right
        )


class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        seg = [Seg() for _ in range(26)]
        # Preprocess the left and right endpoints.
        for i in range(len(s)):
            char_idx = ord(s[i]) - ord("a")
            if seg[char_idx].left == -1:
                seg[char_idx].left = seg[char_idx].right = i
            else:
                seg[char_idx].right = i

        for i in range(26):
            if seg[i].left != -1:
                j = seg[i].left
                while j <= seg[i].right:
                    char_idx = ord(s[j]) - ord("a")
                    if (
                        seg[i].left <= seg[char_idx].left
                        and seg[char_idx].right <= seg[i].right
                    ):
                        pass
                    else:
                        seg[i].left = min(seg[i].left, seg[char_idx].left)
                        seg[i].right = max(seg[i].right, seg[char_idx].right)
                        j = seg[i].left
                    j += 1

        # Greedily select intervals.
        seg.sort()
        ans = list()
        end = -1
        for segment in seg:
            left, right = segment.left, segment.right
            if left == -1:
                continue
            if end == -1 or left > end:
                end = right
                ans.append(s[left : right + 1])

        return ans
```

---

# Example Walkthrough

Let's trace `s = "abbac"`

1. **Initial Boundaries:**
   * 'a': [0, 3]
   * 'b': [1, 2]
   * 'c': [4, 4]

2. **Expand Intervals:**
   * Checking 'a' [0, 3]: It contains 'b'. The boundaries for 'b' are [1, 2], which is strictly inside [0, 3]. No expansion needed. 'a' remains [0, 3].
   * Checking 'b' [1, 2]: It contains only 'b'. No expansion needed. 'b' remains [1, 2].
   * Checking 'c' [4, 4]: It contains only 'c'. No expansion needed. 'c' remains [4, 4].

3. **Greedy Selection (Sorting by `right`):**
   * Sorted Valid Intervals: `[1, 2]` ('b'), `[0, 3]` ('a'), `[4, 4]` ('c')
   * Pick `[1, 2]` $\rightarrow$ "bb" (end = 2)
   * Check `[0, 3]`: `left=0` is NOT `> end=2`. Skip.
   * Check `[4, 4]`: `left=4` is `> end=2`. Pick $\rightarrow$ "c" (end = 4)

Result: `["bb", "c"]`

---

# Complexity Analysis

Time Complexity

$\mathcal{O}(N)$

- Finding initial endpoints takes $\mathcal{O}(N)$.
- Expanding intervals: Even though there is a nested loop (re-evaluating `j`), a boundary can be pushed to the left at most 26 times. In the worst case, checking and expanding intervals across 26 characters takes $\mathcal{O}(26 \times N)$, which simplifies to $\mathcal{O}(N)$.
- Sorting the intervals takes $\mathcal{O}(26 \log 26) = \mathcal{O}(1)$.
- Creating the final answer strings takes at most $\mathcal{O}(N)$.
- Overall time complexity is strictly linear, $\mathcal{O}(N)$.

Space Complexity

$\mathcal{O}(1)$

The extra space used for the intervals array is exactly 26, which is constant. We also do not create dynamic arrays inside the loops. Aside from the memory allocated for the final string array answer, the auxiliary space is $\mathcal{O}(1)$.