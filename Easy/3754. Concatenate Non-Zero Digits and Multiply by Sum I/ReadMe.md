# 3754. Concatenate Non-Zero Digits and Multiply by Sum I

**Difficulty:** Easy
**Problem Link:** [LeetCode 3754](https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-i/description/)

---

## Problem
You are given an integer `n`. You need to perform the following operations:
1. Calculate the sum of all the digits of `n`.
2. Form a new integer by concatenating all the **non-zero** digits of `n` in their original relative order.
3. Return the product of the sum and the newly formed integer.

---

# Approach

This solution uses a straightforward **String Manipulation and Math** approach, allowing us to compute both required values in a single, efficient pass.

Steps:

1. **Initialization:** We initialize `sum = 0` to keep track of the sum of the digits, and `x = 0` to mathematically build our new number without zeros.
2. **Iterate Through Digits:** We convert the integer `n` into a string (`str(n)`) to easily iterate through its digits from left to right.
3. **Accumulate Sum:** For each character, we convert it back to an integer `d` and add it to our `sum`.
4. **Build the Non-Zero Number:** If the digit `d` is greater than `0` (meaning it's not a zero), we append it to our new number `x`. Instead of using string concatenation, we use a mathematical approach: `x = x * 10 + d`. This shifts the existing digits of `x` one decimal place to the left and adds the new digit to the ones place.
5. **Result:** Finally, we return the product of our built number `x` and the accumulated `sum`.

---

# Example Walkthrough

Consider `n = 104203`

* **Initialization:** `x = 0`, `sum = 0`
* **Iteration:**
  * `d = 1`: `sum = 1`, `d > 0` $\rightarrow$ `x = 0 * 10 + 1 = 1`
  * `d = 0`: `sum = 1 + 0 = 1`, `d == 0` $\rightarrow$ `x` remains `1`
  * `d = 4`: `sum = 1 + 4 = 5`, `d > 0` $\rightarrow$ `x = 1 * 10 + 4 = 14`
  * `d = 2`: `sum = 5 + 2 = 7`, `d > 0` $\rightarrow$ `x = 14 * 10 + 2 = 142`
  * `d = 0`: `sum = 7 + 0 = 7`, `d == 0` $\rightarrow$ `x` remains `142`
  * `d = 3`: `sum = 7 + 3 = 10`, `d > 0` $\rightarrow$ `x = 142 * 10 + 3 = 1423`
* **Final Calculation:** `x * sum` = `1423 * 10` = `14230`.

Return `14230`.

---

# Complexity Analysis

Time Complexity

O(D)

Where `D` is the number of digits in the integer `n`. Converting the number to a string and iterating through its characters takes linear time relative to the number of digits. Since `D` is very small for standard constraints (e.g., up to 10 or 18 digits for typical integer limits), this executes extremely fast.

Space Complexity

O(D)

Converting the integer `n` to a string requires allocating memory proportional to the number of digits to store the string representation. Aside from that, we only use a few integer variables (`x`, `sum`, `d`), meaning the auxiliary space is strictly bounded by $O(D)$.

---

# Code

```python
class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = 0
        sum = 0
        for c in str(n):
            d = int(c)
            sum += d
            if d > 0:
                x = x * 10 + d
        return x * sum
```