# 3751. Total Waviness of Numbers in Range I

**Difficulty:** Medium
**Problem Link:** [LeetCode 3751](https://leetcode.com/problems/total-waviness-of-numbers-in-range-i/description/)
---

## Problem
You are given two positive integers `num1` and `num2`.

The **waviness** of a number is defined as the number of local extrema (peaks or valleys) in the sequence of its digits. Specifically, a digit `b` surrounded by digits `a` and `c` forms a wave if it is strictly greater than both (`a < b > c`) or strictly less than both (`a > b < c`).

Calculate and return the **total waviness** of all integers in the inclusive range `[num1, num2]`.
 
--- 
 
# Approach 
 
Since this is "Version I" of the problem, the range `[num1, num2]` is small enough to allow for a direct **Simulation / Brute-Force** approach.

We can solve this efficiently by breaking the logic into two parts:
1. **Calculate Waviness for a Single Number:**
   * Convert the number `n` into a string `s` to easily access its digits.
   * We need to evaluate every contiguous triplet of digits. Instead of using a clunky `for` loop with index math, we can use Python's highly optimized `zip(s, s[1:], s[2:])`. This effectively creates a sliding window of size 3, binding the elements to `a, b, c`.
   * For each triplet, we check the wave condition: `(a < b > c)` for a peak or `(a > b < c)` for a valley. 
   * In Python, boolean values `True` and `False` mathematically evaluate to `1` and `0`. We can simply `sum()` these boolean comparisons to get the total waviness of the number.
2. **Aggregate the Range:**
   * Iterate through every number in the range `[num1, num2 + 1]`.
   * Apply our `waviness` function to each number and sum the results.
 
--- 
 
# Example Walkthrough 
 
Let's calculate the waviness of the number `13241`:

* Convert to string: `"13241"`
* Triplet 1 (`a='1', b='3', c='2'`):
  * `1 < 3 > 2` $\rightarrow$ Peak! Evaluates to `True` (1).
* Triplet 2 (`a='3', b='2', c='4'`):
  * `3 > 2 < 4` $\rightarrow$ Valley! Evaluates to `True` (1).
* Triplet 3 (`a='2', b='4', c='1'`):
  * `2 < 4 > 1` $\rightarrow$ Peak! Evaluates to `True` (1).

Total waviness for `13241` = `1 + 1 + 1 = 3`.

The main function simply runs this calculation for every number between `num1` and `num2` and adds them all up.
 
--- 
 
# Complexity Analysis 
 
Time Complexity 
 
O(N \times D) 
 
Where `N` is the total number of integers in the range (`num2 - num1 + 1`) and `D` is the maximum number of digits in `num2`. Converting a number to a string and iterating through its digits takes $O(D)$ time. We do this for all $N$ numbers. Since $D$ is typically very small (e.g., $\le 10$), this is highly efficient for reasonable ranges.

Space Complexity

O(D)

The auxiliary space is bound by the string conversion of the number and the memory required to hold the `zip` iterator elements. Both take $O(D)$ space, where $D$ is the number of digits in the current number.
 
--- 
 
# Code

```python
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def waviness(n: int) -> int:
            s = str(n)
            # Use zip to create a sliding window of 3 digits
            # Booleans evaluate to 1 (True) or 0 (False) in sum()
            return sum(
                (a < b > c) or (a > b < c) for a, b, c in zip(s, s[1:], s[2:])
            )

        # Sum the waviness of all numbers in the inclusive range
        return sum(waviness(n) for n in range(num1, num2 + 1))
```