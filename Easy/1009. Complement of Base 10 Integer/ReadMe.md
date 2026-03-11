# 1009. Complement of Base 10 Integer

**Difficulty:** Easy  
**Problem Link:** [LeetCode 1009](https://leetcode.com/problems/complement-of-base-10-integer/description/)

---

## Problem Description

The **complement** of an integer is the integer you get when you flip all the `0`'s to `1`'s and all the `1`'s to `0`'s in its binary representation.

For example, The integer `5` is `"101"` in binary and its **complement** is `"010"` which is the integer `2`.

Given an integer `n`, return its complement.

---

## Approach: Bitmasking and XOR

Standard bitwise NOT (`~`) in most languages (including Python) operates on signed integers using two's complement, which flips leading zeros as well. To get the complement for only the significant bits, we use a **bitmask**.

### Key Ideas:
1.  **Edge Case:** If $n = 0$, the binary is `"0"`, so the complement is `"1"`.
2.  **Constructing the Mask:** We need a mask that has the same number of bits as $n$, but all bits are set to `1`. 
    - Example: If $n = 5$ (`101`), we need a mask `7` (`111`).
3.  **XOR Operation:** The XOR operation ($n \oplus mask$) flips bits where the mask has a `1`. Since our mask is all `1`s, it effectively flips every bit of $n$.



---

## Code

```python
class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Edge case: 0 is a special case in binary representation
        if n == 0:
            return 1
        
        mask = 0
        temp = n
        
        # Build a mask of 1s with the same bit-length as n
        # For n = 5 (101), mask will become 7 (111)
        while temp > 0:
            mask = (mask << 1) | 1
            temp >>= 1
        
        # XOR n with mask to flip all bits
        return n ^ mask
```

---

## Example Walkthrough

**Input:** `n = 5`

1.  Binary of `5` is `101`.
2.  **Mask Construction:**
    - `temp = 5` (101), `mask` becomes `1`
    - `temp = 2` (10), `mask` becomes `3` (11)
    - `temp = 1` (1), `mask` becomes `7` (111)
3.  **XOR Operation:**
    - `5 (101) ^ 7 (111)`
    - Result: `010` (Binary) $\rightarrow$ **2** (Decimal).

**Output:** `2`

---

## Complexity Analysis

* **Time Complexity:** $O(\log n)$
    - The number of iterations in the `while` loop is equal to the number of bits in $n$, which is $\lfloor \log_2 n \rfloor + 1$.
* **Space Complexity:** $O(1)$
    - We only use a few integer variables (`mask`, `temp`) regardless of the input size.

---

## Tags
`Bit-Manipulation`, `Math`, `Logic`