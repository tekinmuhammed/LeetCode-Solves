# 788. Rotated Digits 

**Difficulty:** Easy
**Problem Link:** [LeetCode 788](https://leetcode.com/problems/rotated-digits/description/)

---

## Problem Description 

An integer `x` is **good** if after rotating each digit individually by 180 degrees, we get a valid integer that is different from `x`. Each digit must be rotated - we cannot choose to leave it as is.

The rules for rotating digits are:
*   **0, 1, and 8** rotate to themselves.
*   **2 and 5** rotate to each other.
*   **6 and 9** rotate to each other.
*   **3, 4, and 7** do not rotate to any digit and become invalid.

Given an integer `n`, return the number of **good** integers in the range `[1, n]`.

---

## Approach: Digit-by-Digit Analysis 

To determine if a number is "good," we need to check every digit within it. A number qualifies if it meets two specific conditions:
1.  **Validity:** It must not contain any digits that become invalid upon rotation (`3`, `4`, or `7`).
2.  **Transformation:** It must contain at least one digit that changes into a different digit (`2`, `5`, `6`, or `9`). If it only contains `0`, `1`, and `8`, the number remains the same after rotation and is not considered "good."

### Key Ideas: 
*   **Iterative Check:** We loop through every integer from $1$ to $n$.
*   **String Conversion:** Converting the number to a string allows us to inspect each digit easily.
*   **Flag Logic:** 
    *   `valid`: Becomes `False` if we hit a `3`, `4`, or `7`.
    *   `changed`: Becomes `True` if we find at least one `2`, `5`, `6`, or `9`.

---

## Code  
```python
class Solution(object):
    def rotatedDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        good_count = 0
        
        # Check every number from 1 to n
        for num in range(1, n + 1):
            s = str(num)
            is_valid = True
            has_changed = False
            
            for ch in s:
                # If the digit is 3, 4, or 7, the whole number is invalid
                if ch in '347':
                    is_valid = False
                    break
                # If the digit is 2, 5, 6, or 9, the number will change after rotation
                if ch in '2569':
                    has_changed = True
            
            # A number is "good" if it only contains valid digits AND 
            # at least one digit that causes the number to change
            if is_valid and has_changed:
                good_count += 1
        
        return good_count
```

---

## Example Walkthrough 

**Input:** `n = 10`

1.  **1:** Only contains `1`. Valid, but `has_changed` is False. (Not Good)
2.  **2:** Contains `2`. Valid, `has_changed` is True. (**Good**)
3.  **3:** Contains `3`. Invalid. (Not Good)
4.  **5:** Contains `5`. Valid, `has_changed` is True. (**Good**)
5.  **6:** Contains `6`. Valid, `has_changed` is True. (**Good**)
6.  **8:** Only contains `8`. Valid, but `has_changed` is False. (Not Good)
7.  **9:** Contains `9`. Valid, `has_changed` is True. (**Good**)
8.  **10:** Contains `1` and `0`. Valid, but `has_changed` is False. (Not Good)

**Total Good Numbers:** 4 (2, 5, 6, 9)

---

## Complexity Analysis 

* **Time Complexity:** $O(n \cdot \log_{10} n)$
    - We iterate through $n$ numbers.
    - For each number, we check its digits. The number of digits in $n$ is $\lfloor \log_{10} n \rfloor + 1$.
* **Space Complexity:** $O(\log_{10} n)$
    - The string representation of the number requires space proportional to the number of digits.

---

## Tags
`String`, `Math`, `Enumeration`, `Logic`