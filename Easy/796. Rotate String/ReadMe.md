# 796. Rotate String 

**Difficulty:** Easy
**Problem Link:** [LeetCode 796](https://leetcode.com/problems/rotate-string/description/)

---

## Problem Description 

Given two strings `s` and `goal`, return `true` if and only if `s` can become `goal` after some number of **shifts** on `s`.

A **shift** on `s` consists of moving the leftmost character of `s` to the rightmost position.
- For example, if `s = "abcde"`, then it will be `"bcdea"` after one shift.

---

## Approach: Simulation of Rotations 

The most direct way to solve this is to simulate the shifting process. Since the string has a length of $n$, there are only $n$ unique rotations possible. If none of these $n$ rotations match the `goal`, then it is impossible.

### Key Ideas: 
1.  **Length Validation:** If the lengths of `s` and `goal` are different, it's impossible for one to be a rotation of the other. We return `False` immediately.
2.  **Simulation:** We use a loop that runs `len(s)` times. In each iteration:
    - We perform a single left shift: `s = s[1:] + s[0]`.
    - We check if the current state of `s` equals `goal`.
3.  **Alternative (Trick) Approach:** While simulation works, a common "cleaner" trick is to check if `goal` is a substring of `s + s`. For example, if `s = "abcde"`, `s + s = "abcdeabcde"`. All possible rotations of "abcde" are contained within this doubled string.



---

## Code 

```python
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        # If lengths are different, s can never become goal
        if len(s) != len(goal):
            return False
            
        length = len(s)

        # Try all possible rotations of the string (at most 'length' times)
        for _ in range(length):
            # Perform one rotation: take the first char and put it at the end
            s = s[1:] + s[0]
            
            # Check if current rotation matches goal
            if s == goal:
                return True
                
        return False
```

---

## Example Walkthrough 

**Input:** `s = "abcde", goal = "cdeab"`

1.  **Initial:** `s = "abcde"`.
2.  **Rotation 1:** `s[1:]("bcde") + s[0]("a")` $\rightarrow$ `"bcdea"`. Not goal.
3.  **Rotation 2:** `s[1:]("cdea") + s[0]("b")` $\rightarrow$ `"cdeab"`. **Match!**

**Output:** `True`

---

## Complexity Analysis 

* **Time Complexity:** $O(n^2)$
    - We loop $n$ times.
    - In each iteration, string slicing and concatenation create a new string, which takes $O(n)$ time.
* **Space Complexity:** $O(n)$
    - We store the new rotated string in each step.

---

## Tags 
`String`, `Simulation`, `String-Manipulation`, `Easy-Logic`