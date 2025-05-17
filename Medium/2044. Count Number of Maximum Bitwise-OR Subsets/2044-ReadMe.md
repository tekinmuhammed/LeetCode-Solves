# LeetCode 2044 - Count Number of Maximum Bitwise-OR Subsets

## 🔗 Problem Link
[LeetCode 2044 - Count Number of Maximum Bitwise-OR Subsets](https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/)

## 🧠 Problem Description 

Given an integer array `nums`, return the number of non-empty subsets whose **bitwise OR** is equal to the maximum bitwise OR of all subsets. 

The bitwise OR of a subset is the result of bitwise OR-ing all of its elements.

## 🧪 Example 

```python
Input: nums = [3, 1]
Output: 2 
```
# Explanation: 
## Subsets: [3], [1], [3,1]
## Bitwise ORs: 3, 1, 3 => Maximum OR = 3
## There are 2 subsets with OR = 3: [3], [3,1]

## 💡 Approach
Use Depth-First Search (DFS) to generate all possible subsets.

Keep track of the current OR value for each subset.

Update:

* `max_or` whenever a higher OR value is found.
* `count for` how many times the `max_or` occurs.

## 🧮 Complexity

**Time Complexity:** O(2^n)

**Space Complexity:** O(n) 

## 📌 Tags
`bitwise-operations`, `dfs`, `backtracking`, `subsets`, `recursion`