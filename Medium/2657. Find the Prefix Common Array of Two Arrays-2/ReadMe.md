# 2657. Find the Prefix Common Array of Two Arrays

**Difficulty:** Medium  
**Problem Link:** [LeetCode 2657](https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/description/)

---

## Problem
You are given two **0-indexed** integer permutations `A` and `B` of length `n`.

A **prefix common array** of `A` and `B` is an array `C` such that `C[i]` is equal to the count of numbers that are present at or before the index `i` in both `A` and `B`.

Return the prefix common array of `A` and `B`.

Example:

Input  
A = [1,3,2,4], B = [3,1,2,4]

Output  
[0,2,3,4]

Explanation  
- At i = 0: no number is common, so C[0] = 0.
- At i = 1: 1 and 3 are common in both prefixes, so C[1] = 2.
- At i = 2: 1, 2, and 3 are common, so C[2] = 3.
- At i = 3: 1, 2, 3, and 4 are common, so C[3] = 4.

---

# Approach

This solution utilizes a straightforward **simulation (brute-force)** approach to construct the prefix common array. 

Instead of keeping track of previously seen elements using extra data structures like hash sets or frequency arrays, it strictly evaluates the definition of a "prefix" at every single step.

Steps:

1. **Initialize Result Array:** We create a `prefix_common_array` of size `n` initialized to `0`.
2. **Iterate Through Prefixes:** We use an outer loop with `current_index` to define the boundary of our current prefix (from index `0` to `current_index`).
3. **Compare Elements within Prefix:** 
   * For the current prefix, we loop through every element in `A` up to `current_index` (using `a_index`).
   * For each of these elements, we loop through every element in `B` up to `current_index` (using `b_index`).
4. **Count Matches:** If `A[a_index] == B[b_index]`, we have found a common element in the current prefix. We increment our `common_count` and immediately `break` out of the inner loop to prevent counting the same matching pair multiple times.
5. **Store and Continue:** Once all comparisons for the current prefix are done, we store the `common_count` in our result array and move on to the next, slightly larger prefix.

---

# Example Walkthrough

Consider `A = [1, 3, 2]`, `B = [3, 1, 2]`

* **`current_index = 0` (Prefix length 1):**
  * Sub-arrays: `A[0..0] = [1]`, `B[0..0] = [3]`
  * Compare `A[0]` (1) with `B[0]` (3). No match.
  * `common_count = 0` -> `C = [0]`

* **`current_index = 1` (Prefix length 2):**
  * Sub-arrays: `A[0..1] = [1, 3]`, `B[0..1] = [3, 1]`
  * `a_index = 0` (1): Matches `B[1]` (1). `count = 1`.
  * `a_index = 1` (3): Matches `B[0]` (3). `count = 2`.
  * `common_count = 2` -> `C = [0, 2]`

* **`current_index = 2` (Prefix length 3):**
  * Sub-arrays: `A[0..2] = [1, 3, 2]`, `B[0..2] = [3, 1, 2]`
  * `a_index = 0` (1): Matches `B[1]` (1). `count = 1`.
  * `a_index = 1` (3): Matches `B[0]` (3). `count = 2`.
  * `a_index = 2` (2): Matches `B[2]` (2). `count = 3`.
  * `common_count = 3` -> `C = [0, 2, 3]`

---

# Complexity Analysis

Time Complexity

O(N^3)

We have three nested loops. The outer loop runs `N` times. For each iteration `i` of the outer loop, the inner loops perform `i * i` comparisons. The sum of squares $1^2 + 2^2 + 3^2 + ... + N^2$ mathematically resolves to $O(N^3)$. This is a brute-force approach, which is acceptable for small constraints but could be optimized to $O(N)$ using Hash Sets or frequency arrays for larger inputs.

Space Complexity

O(N)

The only extra space used is the `prefix_common_array` of size `N` to store the final results. We do not use any additional data structures, so the auxiliary space is strictly bounded by the output requirement.

---

# Code

```python
class Solution:
    def findThePrefixCommonArray(self, A: list, B: list) -> list:
        n = len(A)
        prefix_common_array = [0] * n

        # Loop through each index to calculate common elements for each prefix
        for current_index in range(n):
            common_count = 0

            # Compare elements in A and B within the range of current prefix
            for a_index in range(current_index + 1):
                for b_index in range(current_index + 1):

                    # Check if elements match, and count if they do
                    if A[a_index] == B[b_index]:
                        common_count += 1
                        break  # Prevent counting duplicates

            # Store the count of common elements for the current prefix
            prefix_common_array[current_index] = common_count

        # Return the final list with counts of common elements in each prefix
        return prefix_common_array
```