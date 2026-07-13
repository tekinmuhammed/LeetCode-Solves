# 1291. Sequential Digits

**Difficulty:** Medium
**Problem Link:** [LeetCode 1291](https://leetcode.com/problems/sequential-digits/description/)

---
  
## Problem 
An integer has **sequential digits** if and only if each digit in the number is one more than the previous digit.

Return a **sorted** list of all the integers in the range `[low, high]` inclusive that have sequential digits.

Example:
Input: `low = 100`, `high = 300`
Output: `[123, 234]`
 
--- 
 
# Approach 

Instead of iterating through every single number between `low` and `high` (which would be extremely slow), this solution uses **Precomputation** with a **Breadth-First Search (BFS)** style queue to generate *all* possible sequential digits beforehand. 

Since there are only 45 valid sequential digit numbers in total (e.g., `12`, `123`, `123456789`), we can generate all of them once when the class is loaded, and then simply filter them for each test case.

Steps:

1. **Class-Level Precomputation:**
   * We initialize a list `q = [1, 2, 3, 4, 5, 6, 7, 8, 9]`.
   * We iterate over `q`. In Python, iterating over a list while appending to it makes it act like a BFS queue.
2. **Generating Sequential Numbers:**
   * For each number `x` in the queue, we find its last digit: `d = x % 10`.
   * If the last digit is less than `9`, we can append the next sequential digit.
   * We form the new number mathematically: `x * 10 + d + 1`. (For example, if `x = 12`, `d = 2`. The new number is `12 * 10 + 3 = 123`).
   * We append this new number to `q`, which guarantees that the list remains perfectly sorted as it grows.
3. **Filtering (The Function):**
   * When `sequentialDigits(l, h)` is called, the `q` list already contains all 45 valid numbers in sorted order.
   * We simply use a list comprehension to return the numbers that fall within the `[l, h]` range.
 
--- 
 
# Example Walkthrough 
 
Let's look at how the `q` list is built initially:

* `q` starts as `[1, 2, 3, 4, 5, 6, 7, 8, 9]`.
* Loop reads `1`: Last digit is `1`. Less than 9. Appends `1 * 10 + 2 = 12`.
* Loop reads `2`: Last digit is `2`. Less than 9. Appends `23`.
* ...
* Loop reads `8`: Last digit is `8`. Less than 9. Appends `89`.
* Loop reads `9`: Last digit is `9`. Not less than 9. Skips.
* Loop reads `12` (which was just appended!): Last digit is `2`. Appends `123`.
* ...
* This continues until it builds the maximum possible sequential number: `123456789`.
* Final `q` size is exactly 45 elements.

If the query is `low = 100`, `high = 300`:
* We iterate over our 45-element list and pick `123` and `234`.
 
--- 
 
# Complexity Analysis 

Time Complexity

O(1)

The generation of the 45 numbers happens exactly once at the class level (during import/load time). When the `sequentialDigits` function is actually called, it only filters a fixed-size array of 45 elements. Therefore, the time taken per query is strictly $O(1)$ constant time.

Space Complexity

O(1)

The `q` list permanently stores exactly 45 integers, regardless of the input sizes of `low` and `high`. The space complexity is thus strictly $O(1)$.

---

# Code

```python
class Solution:
    # Precompute all possible sequential digits using a BFS-like approach
    q = [*range(1, 10)]

    for x in q:
        d = x % 10
        if d < 9:
            # Shift the number left and append the next sequential digit
            q.append(x * 10 + d + 1)

    def sequentialDigits(self, l: int, h: int) -> list[int]:
        # Filter the precomputed list based on the given range
        return [x for x in self.q if l <= x <= h]
```