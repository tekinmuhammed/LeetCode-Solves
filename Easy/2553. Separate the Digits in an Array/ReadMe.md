# 2553. Separate the Digits in an Array

**Difficulty:** Easy  
**Problem Link:** [LeetCode 2553](https://leetcode.com/problems/separate-the-digits-in-an-array/description/)

---

## Problem
Given an array of positive integers `nums`, return an array `answer` that consists of the digits of each integer in `nums` after separating them in the same order they appear in `nums`.

To be clear, the digits of the integer `10921` are `1`, `0`, `9`, `2`, and `1`.

Example:

Input  
nums = [13, 2583, 77]

Output  
[1, 3, 2, 5, 8, 3, 7, 7]

Explanation  
- The separation of 13 is 1, 3.
- The separation of 2583 is 2, 5, 8, 3.
- The separation of 77 is 7, 7.
- `answer = [1, 3, 2, 5, 8, 3, 7, 7]`.

---

# Approach

We can solve this problem by mathematically extracting the digits of each number. 

While converting each number to a string and iterating over its characters is a common shortcut in Python, using standard mathematical operations (modulo and integer division) is often a great way to demonstrate an understanding of core computer science fundamentals.

Steps:

1. **Iterate Through the Array:** Loop over every integer `x` in the given `nums` array.
2. **Extract Digits Mathematically:** 
   * Use a `while` loop that runs as long as `x > 0`.
   * Use the modulo operator (`x % 10`) to get the last digit of the number and append it to a temporary list `tmp`.
   * Use integer division (`x //= 10`) to chop off the last digit from the number.
3. **Correct the Order:** Because we extract digits from the end to the beginning (least significant to most significant), the `tmp` list holds the digits in reverse order. We reverse `tmp` using slicing (`tmp[::-1]`).
4. **Append to Result:** Add the corrected digits from `tmp` to the main `res` array using `extend()`.

---

# Example Walkthrough

Let's trace the code with `nums = [13, 2583]`:

* **First number: 13**
  * `13 > 0`: `13 % 10 = 3`. Append `3`. `x` becomes `1`. (`tmp = [3]`)
  * `1 > 0`: `1 % 10 = 1`. Append `1`. `x` becomes `0`. (`tmp = [3, 1]`)
  * Reverse `tmp` -> `[1, 3]`. Extend `res`. 
  * `res = [1, 3]`

* **Second number: 2583**
  * `2583 % 10 = 3`. Append `3`. `x` becomes `258`.
  * `258 % 10 = 8`. Append `8`. `x` becomes `25`.
  * `25 % 10 = 5`. Append `5`. `x` becomes `2`.
  * `2 % 10 = 2`. Append `2`. `x` becomes `0`.
  * `tmp = [3, 8, 5, 2]`. 
  * Reverse `tmp` -> `[2, 5, 8, 3]`. Extend `res`.
  * `res = [1, 3, 2, 5, 8, 3]`

---

# Complexity Analysis

Time Complexity

O(K)

Where `K` is the total number of digits across all elements in the `nums` array. We process every single digit exactly once during the while loop and once more during the reversal, making the time complexity strictly linear with respect to the total digit count.

Space Complexity

O(K)

We use an array `res` to store all `K` digits. The temporary array `tmp` holds at most the digits of the largest single number, which takes negligible extra space. The overall space is bounded by the output size.

---

# Code

```python
from typing import List

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for x in nums:
            tmp = []
            while x > 0:
                tmp.append(x % 10)
                x //= 10
            res.extend(tmp[::-1])
        return res
```