# 3783. Mirror Distance of an Integer

**Difficulty:** Easy  
**Problem Link:** [LeetCode 3783](https://leetcode.com/problems/mirror-distance-of-an-integer/)

---

## Problem Description

Given an integer `n`, find its **mirror distance**. The mirror of an integer is defined as the integer formed by reversing the order of its digits. The mirror distance is the **absolute difference** between the original integer and its mirror.

For example, the mirror of `123` is `321`, and the mirror distance is $|123 - 321| = 198$.

---

## Approach: Integer Reversal and Absolute Difference

The solution consists of two simple mathematical steps: reversing the digits of the integer and then calculating the absolute difference from the original number.

### Key Ideas:
1.  **Reversing Digits (Mathematical Way):** - To reverse an integer without converting it to a string, we can use a `while` loop with the modulo (`%`) and integer division (`//`) operators.
    - We extract the last digit using `n % 10` and append it to our result `res = res * 10 + digit`.
2.  **Handling Leading Zeros:** The mathematical reversal naturally handles cases where the original number ends in zero. For instance, `120` becomes `021` (which is stored as `21` in integer format).
3.  **Absolute Difference:** We use the `abs()` function to ensure the distance is always non-negative, regardless of whether the original number or its mirror is larger.



---

## Code

```python
class Solution:
    def reverse(self, n: int) -> int:
        """
        Reverses the digits of an integer n.
        """
        res = 0
        while n > 0:
            # Extract the last digit and shift result to the left
            res = res * 10 + n % 10
            # Remove the last digit from n
            n //= 10
        return res

    def mirrorDistance(self, n: int) -> int:
        """
        Calculates the absolute difference between n and its mirror.
        """
        # Calculate mirror distance: |n - reverse(n)|
        return abs(n - self.reverse(n))
```

---

## Example Walkthrough

**Input:** `n = 456`

1.  **Reversing 456:**
    - `res = 0 * 10 + 6 = 6`, `n = 45`
    - `res = 6 * 10 + 5 = 65`, `n = 4`
    - `res = 65 * 10 + 4 = 654`, `n = 0`
    - Reversed value = `654`.
2.  **Distance Calculation:**
    - `abs(456 - 654) = abs(-198) = 198`.

**Output:** `198`

---

## Complexity Analysis

* **Time Complexity:** $O(\log_{10} n)$
    - The number of iterations in the `while` loop is equal to the number of digits in `n`. Since a number `n` has approximately $\log_{10} n$ digits, the complexity is logarithmic.
* **Space Complexity:** $O(1)$
    - We only use a few constant-sized integer variables (`res`) to perform the calculation.

---

## Tags
Math, Logic, Easy-Logic, Reversal