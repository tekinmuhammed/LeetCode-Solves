# 3498. Reverse Degree of a String

**Difficulty:** Easy  
**Problem Link:** [LeetCode 3498](https://leetcode.com/problems/reverse-degree-of-a-string/description/) *(Note: Link based on standard LeetCode URL structure)*

---

## Problem
Given a string `s` consisting of lowercase English letters, calculate its **Reverse Degree**. 

The "reverse alphabetical weight" of a character is defined by its reverse position in the alphabet. For example:
* 'a' = 26
* 'b' = 25
* ...
* 'z' = 1

The Reverse Degree of a string is the sum of the reverse alphabetical weight of each character multiplied by its **1-based index** (position) in the string. Return the total sum.

Example:

Input  
s = "abc"  

Output  
148  

Explanation  
- 'a' is at position 1. Weight = 26. Value = 1 * 26 = 26.
- 'b' is at position 2. Weight = 25. Value = 2 * 25 = 50.
- 'c' is at position 3. Weight = 24. Value = 3 * 24 = 72.
Total = 26 + 50 + 72 = 148.

---

# Approach

The problem requires a straightforward string traversal with some basic arithmetic based on character ASCII values.

Steps:
1. **Initialize a counter (`ans`)**: Set it to 0 to accumulate the total score.
2. **Iterate with 1-based indexing**: Use Python's `enumerate(s, start=1)` to loop through the string, getting both the 1-based index `i` and the character `ch` simultaneously.
3. **Calculate the reverse weight**: 
   * `ord(ch) - ord("a")` maps 'a' to 0, 'b' to 1, ..., 'z' to 25.
   * Subtracting this value from `26` gives the exact reverse weight: `26 - 0 = 26` (for 'a'), `26 - 25 = 1` (for 'z').
4. **Accumulate**: Multiply the calculated weight by the index `i` and add it to `ans`.
5. **Return**: Once the loop is complete, return `ans`.

---

# Code

```python
class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0
        for i, ch in enumerate(s, start=1):
            ans += (26 - (ord(ch) - ord("a"))) * i
        return ans
```

---

# Example Walkthrough

Let's trace the string `s = "zz"`

1. **Iteration 1**:
   * `i = 1`, `ch = 'z'`
   * Base value of 'z': `ord('z') - ord('a') = 25`
   * Reverse weight: `26 - 25 = 1`
   * Product: `1 * 1 = 1`
   * `ans = 0 + 1 = 1`

2. **Iteration 2**:
   * `i = 2`, `ch = 'z'`
   * Base value of 'z': `ord('z') - ord('a') = 25`
   * Reverse weight: `26 - 25 = 1`
   * Product: `1 * 2 = 2`
   * `ans = 1 + 2 = 3`

Result: `3`

---

# Complexity Analysis

Time Complexity

$\mathcal{O}(N)$

Where $N$ is the length of the string `s`. We iterate through the characters of the string exactly once. The operations inside the loop (ASCII conversion, subtraction, multiplication) take constant time $\mathcal{O}(1)$.

Space Complexity

$\mathcal{O}(1)$

The algorithm uses a single integer variable `ans` to keep track of the sum. It does not allocate any additional data structures that scale with the size of the input, making the space complexity strictly constant.