# 1331. Rank Transform of an Array

**Difficulty:** Easy  
**Problem Link:** [LeetCode 1331](https://leetcode.com/problems/rank-transform-of-an-array/description/)

---

## Problem
Given an array of integers `arr`, replace each element with its rank.

The rank represents how large the element is. The rank has the following rules:
* Rank is an integer starting from `1`.
* The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
* Rank should be as small as possible.

Example:

Input: `arr = [40, 10, 20, 30]`  
Output: `[4, 1, 2, 3]`  
Explanation: 40 is the largest element. 10 is the smallest. 20 is the second smallest. 30 is the third smallest.

---

# Approach

To assign the correct rank to each element without losing their original positions, we can use a combination of **Sorting** and **Hashing (Dictionary)**.

Steps:

1. **Sort a Copy:** We create a sorted copy of the original array (`sorted_arr`). This allows us to process the numbers from smallest to largest.
2. **Assign Ranks:** We iterate through the `sorted_arr`.
   * We initialize a `rank` variable to `1`.
   * We store the rank of each number in a dictionary called `num_to_rank`.
   * If we encounter a number that is strictly greater than the previous number in the sorted array, we increment the `rank` by `1`. This ensures that duplicate numbers receive the exact same rank.
3. **Transform the Original Array:** Finally, we iterate through the original `arr`. For each element, we look up its calculated rank in the `num_to_rank` dictionary and replace the element with this rank.

---

# Example Walkthrough

Consider `arr = [37, 12, 28, 9, 100, 56, 80, 5, 12]`

1. **Sort the array:**
   `sorted_arr = [5, 9, 12, 12, 28, 37, 56, 80, 100]`
2. **Build the Dictionary (num_to_rank):**
   * `5` $\rightarrow$ rank 1
   * `9` $\rightarrow$ rank 2
   * `12` $\rightarrow$ rank 3
   * `12` $\rightarrow$ (already seen, rank stays 3)
   * `28` $\rightarrow$ rank 4
   * `37` $\rightarrow$ rank 5
   * `56` $\rightarrow$ rank 6
   * `80` $\rightarrow$ rank 7
   * `100` $\rightarrow$ rank 8
   * `num_to_rank = {5: 1, 9: 2, 12: 3, 28: 4, 37: 5, 56: 6, 80: 7, 100: 8}`
3. **Transform Original Array:**
   Replace each element in `[37, 12, 28, 9, 100, 56, 80, 5, 12]` using the dictionary:
   Result: `[5, 3, 4, 2, 8, 6, 7, 1, 3]`

---

# Complexity Analysis

Time Complexity

O(N \log N)

Where `N` is the number of elements in the array. Sorting the array takes $O(N \log N)$ time. The subsequent iterations to build the dictionary and transform the original array take $O(N)$ time. The dominant operation is the sorting, making the overall time complexity $O(N \log N)$.

Space Complexity

O(N)

We create a sorted copy of the array which takes $O(N)$ space. The dictionary `num_to_rank` will store at most $N$ unique key-value pairs, which also takes $O(N)$ space. Therefore, the overall auxiliary space is $O(N)$.

---

# Code

```python
from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # Store the rank for each number in arr
        num_to_rank = {}
        sorted_arr = sorted(arr)
        rank = 1
        
        for i in range(len(sorted_arr)):
            # Increment rank only if the current number is strictly greater than the previous
            if i > 0 and sorted_arr[i] > sorted_arr[i - 1]:
                rank += 1
            num_to_rank[sorted_arr[i]] = rank
            
        # Replace elements in the original array with their calculated ranks
        for i in range(len(arr)):
            arr[i] = num_to_rank[arr[i]]
            
        return arr
```