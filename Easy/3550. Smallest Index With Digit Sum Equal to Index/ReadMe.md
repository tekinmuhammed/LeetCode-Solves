# 3550. Smallest Index With Digit Sum Equal to Index

**Difficulty:** Easy 
**Problem Link:** [LeetCode 3550](https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/description/)
---

## Problem
Given a 0-indexed integer array `nums`, return the **smallest index** `i` such that the sum of the digits of `nums[i]` is equal to `i`. If no such index exists, return `-1`.

Example:

Input  
nums = [10, 23, 11, 4]  

Output  
2  

Explanation  
- For i = 0, nums[0] = 10, digit sum = 1 + 0 = 1. (1 != 0)
- For i = 1, nums[1] = 23, digit sum = 2 + 3 = 5. (5 != 1)
- For i = 2, nums[2] = 11, digit sum = 1 + 1 = 2. (2 == 2) -> Match!
The smallest index where the condition holds is 2.

---

# Approach

The problem requires checking a simple condition for each element in the array starting from the first element.

Steps:
1. **Digit Sum Helper**: We define a helper function `get_digit_sum(num)` that calculates the sum of the digits of a given number. It repeatedly extracts the last digit using `divmod(num, 10)` (which returns the quotient and the remainder simultaneously) and adds it to a running total until the number becomes 0.
2. **Linear Search**: We iterate through the array `nums` from left to right using `enumerate` to track both the index `i` and the value `num`.
3. **Check Condition**: For each element, we calculate its digit sum. If the digit sum equals the current index `i`, we immediately return `i`. 
4. **First Match Guarantee**: Because we iterate starting from index `0` upwards, the first match we encounter is guaranteed to be the *smallest* valid index.
5. **No Match**: If the loop finishes evaluating all elements without finding a match, we return `-1`.

---

# Code

```python
class Solution:
    def smallestIndex(self, nums: list[int]) -> int:
        def get_digit_sum(num: int) -> int:
            total = 0

            while num:
                num, digit = divmod(num, 10)
                total += digit

            return total

        for i, num in enumerate(nums):
            if get_digit_sum(num) == i:
                return i

        return -1
```

---

# Example Walkthrough

Let's trace `nums = [15, 20, 2, 4]`

1. **i = 0, num = 15**:
   * `get_digit_sum(15)` -> `1 + 5 = 6`
   * Does `6 == 0`? No.
2. **i = 1, num = 20**:
   * `get_digit_sum(20)` -> `2 + 0 = 2`
   * Does `2 == 1`? No.
3. **i = 2, num = 2**:
   * `get_digit_sum(2)` -> `2`
   * Does `2 == 2`? **Yes!**

Return `2`. The loop terminates early, saving us from unnecessarily checking `nums[3]`.

---

# Complexity Analysis

Time Complexity

$\mathcal{O}(N \cdot D)$

Where $N$ is the number of elements in `nums` and $D$ is the maximum number of digits in any single element. Mathematically, $D = \mathcal{O}(\log_{10}(\max(nums)))$. Since standard integers usually have at most 9 to 10 digits, $D$ is effectively a small constant. Thus, the time complexity simplifies to $\mathcal{O}(N)$ in practical terms.

Space Complexity

$\mathcal{O}(1)$

The algorithm only uses a few integer variables (`total`, `num`, `digit`, `i`). No additional data structures that scale with the input size are allocated, so the space complexity is strictly constant.