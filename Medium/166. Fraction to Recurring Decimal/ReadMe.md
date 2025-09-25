# 166. Fraction to Recurring Decimal

**Difficulty:** Medium
**Problem Link:** [LeetCode 368](https://leetcode.com/problems/fraction-to-recurring-decimal/description/)

---

## Problem Description
Given two integers `numerator` and `denominator`, return the fraction in **string format**.  

- If the fractional part is **repeating**, enclose the repeating part in parentheses.  
- If `numerator` is `0`, return `"0"`.  
- The result must handle both positive and negative fractions.  

---

### Example 1
**Input:**  
```python
numerator = 1, denominator = 2
```

**Output:**  
```python
"0.5"
```

---

### Example 2
**Input:**  
```python
numerator = 2, denominator = 3
```

**Output:**  
```python
"0.(6)"
```

---

### Example 3
**Input:**  
```python
numerator = 4, denominator = 333
```

**Output:**  
```python
"0.(012)"
```

---

## Approach
1. **Handle sign**: If the result should be negative, add `"-"` at the beginning.  
2. **Integer part**: Compute the division `numerator // denominator`.  
3. **Remainder handling**:  
   - If remainder = 0 → return integer part only.  
   - Otherwise, continue to decimal part.  
4. **Recurring cycle detection**:  
   - Use a dictionary `seen` to store remainders and their positions in the result.  
   - If the same remainder reappears, it means a repeating cycle is found.  
   - Insert `"("` at the position and append `")"` at the end.  
5. Build the final string.  

---

## Complexity Analysis
- **Time Complexity:** `O(n)` where `n` is the length of the repeating cycle.  
- **Space Complexity:** `O(n)` for storing remainders in the dictionary.  

---

## Code Implementation
```python
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
            return "0"

        res = []

        # Handle sign
        if (numerator < 0) ^ (denominator < 0):
            res.append("-")

        # Work with absolute values
        numerator, denominator = abs(numerator), abs(denominator)

        # Integer part
        res.append(str(numerator // denominator))
        remainder = numerator % denominator
        if remainder == 0:
            return "".join(res)

        res.append(".")

        # Decimal part with remainder tracking
        seen = {}
        while remainder != 0:
            if remainder in seen:
                res.insert(seen[remainder], "(")
                res.append(")")
                break

            seen[remainder] = len(res)
            remainder *= 10
            res.append(str(remainder // denominator))
            remainder %= denominator

        return "".join(res)
```

### Tags

`LeetCode-Medium`