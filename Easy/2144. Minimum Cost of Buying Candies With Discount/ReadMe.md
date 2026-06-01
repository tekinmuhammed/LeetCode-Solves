# 2144. Minimum Cost of Buying Candies With Discount

**Difficulty:** Easy
**Problem Link:** [LeetCode 2144](https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/description/)

--- 
 
## Problem 
A shop is selling candies. For every two candies sold, the shop gives a **third candy for free**. 
 
The customer can choose any candy to take for free, but the cost of the chosen candy must be less than or equal to the **minimum cost** of the two candies bought.
* For example, if there are `4` candies with costs `1`, `2`, `3`, and `4`, and the customer buys candies with costs `2` and `3`, they can take the candy with cost `1` for free, but not the candy with cost `4`.

Given a **0-indexed** integer array `cost`, where `cost[i]` denotes the cost of the $i^{th}$ candy, return the **minimum cost** of buying all the candies.
 
--- 
 
# Approach 
 
To minimize the total cost, we should aim to get the most expensive candies possible for free. This is a classic **Greedy Algorithm** scenario.

If we buy the two absolute most expensive candies in the shop, we are allowed to take the third most expensive candy for free. If we repeat this logic, we should group the candies in threes, paying for the top two of each group and getting the third one free.
 
Steps: 
 
1. **Sort Descending:** Sort the `cost` array in descending order (`-x`). This puts the most expensive candies at the beginning.
2. **Iterate and Apply Discount:** We iterate through the sorted array. 
   * The candy at index `0` is paid.
   * The candy at index `1` is paid.
   * The candy at index `2` is **free**.
   * The candy at index `3` is paid... and so on.
3. **Modular Arithmetic:** Notice the pattern: any candy at an index where `(index + 1)` is a multiple of 3 is free. In 0-indexed terms, if `i % 3 == 2`, the candy is free. Therefore, we simply add the cost of all candies to our total `res` **unless** `i % 3 == 2`.
 
--- 
 
# Example Walkthrough 
 
Consider `cost = [6, 5, 7, 9, 2, 2]`

1. **Sort Descending:** `cost = [9, 7, 6, 5, 2, 2]`
2. **Iterate:**
   * `i = 0` (cost 9): `0 % 3 != 2` $\rightarrow$ Pay 9. Total = `9`.
   * `i = 1` (cost 7): `1 % 3 != 2` $\rightarrow$ Pay 7. Total = `16`.
   * `i = 2` (cost 6): `2 % 3 == 2` $\rightarrow$ **Free!** Total = `16`.
   * `i = 3` (cost 5): `3 % 3 != 2` $\rightarrow$ Pay 5. Total = `21`.
   * `i = 4` (cost 2): `4 % 3 != 2` $\rightarrow$ Pay 2. Total = `23`.
   * `i = 5` (cost 2): `5 % 3 == 2` $\rightarrow$ **Free!** Total = `23`.

Return `23`. 
 
--- 
 
# Complexity Analysis 
 
Time Complexity 
 
O(N \log N) 
 
Where `N` is the number of candies. The time complexity is completely dominated by the sorting step. The subsequent loop to calculate the sum takes $O(N)$ time.
 
Space Complexity 
 
O(1) auxiliary 
 
The logic itself uses only a few integer variables (`res`, `n`, `i`), meaning it takes $O(1)$ auxiliary space. *(Note: Python's `sort()` method, Timsort, takes $O(N)$ space under the hood).*
 
--- 
 
# Code

```python
from typing import List

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(key=lambda x: -x)
        res = 0
        n = len(cost)
        for i in range(n):
            if i % 3 != 2:
                res += cost[i]
        return res
```