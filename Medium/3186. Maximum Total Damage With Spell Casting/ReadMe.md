# 3186. Maximum Total Damage With Spell Casting  

## Difficulty  
Medium  

## Problem Link  
[LeetCode - 3186. Maximum Total Damage With Spell Casting](https://leetcode.com/problems/maximum-total-damage-with-spell-casting/)  

## Tags  
`Dynamic Programming` `Hash Map` `Sorting`  

---

## Problem Description  
You are given an integer array `power`, where each element represents the power level of a spell.  

You can cast a spell multiple times if it appears multiple times in the list, but **casting a spell of power `x` makes it impossible to cast any spell with power in `[x - 2, x + 2]`** (since they interfere with each other).  

Your goal is to find the **maximum total damage** you can achieve, where total damage equals the sum of all chosen powers multiplied by their frequencies.

---

## Approach  

This problem is similar to the classic **“House Robber”** dynamic programming problem, but with a **distance constraint of 2** between consecutive spells.

### Step-by-step Explanation  

1. **Count the frequency** of each spell power using `Counter`.  
   Each power contributes `power[i] * frequency[i]` total damage if chosen.  

2. **Sort unique spell powers** to process them in increasing order.  

3. **Dynamic Programming (DP)**  
   - `dp[i]` represents the **maximum total damage** we can get considering spell powers up to index `i`.  
   - For each spell `unique[i]`:  
     - If we skip it → `dp[i] = dp[i-1]`  
     - If we choose it → add its damage plus the best non-conflicting previous state.  

   The non-conflicting previous spell must have `unique[i] - unique[j] > 2`.

   So:  
   \[
   dp[i] = \max(dp[i-1], \text{damage}[i] + dp[j])
   \]  
   where `j` is the last index before `i` such that `unique[i] - unique[j] > 2`.

---

## Code Implementation  

```python
from collections import Counter

class Solution(object):
    def maximumTotalDamage(self, power):
        """
        :type power: List[int]
        :rtype: int
        """
        count = Counter(power)
        unique = sorted(count.keys())

        n = len(unique)
        dp = [0] * n

        for i in range(n):
            damage = unique[i] * count[unique[i]]
            
            # Find last non-conflicting spell (difference > 2)
            j = i - 1
            while j >= 0 and unique[i] - unique[j] <= 2:
                j -= 1
            
            if i == 0:
                dp[i] = damage
            else:
                dp[i] = max(dp[i-1], damage + (dp[j] if j >= 0 else 0))

        return dp[-1]
```

### Complexity Analysis
- **Time Complexity:**
- - 𝑂(𝑛2) — because for each `i`, we may look backward to find `j`.

- - (This can be optimized to O(n) using binary search or prefix DP.)

- **Space Complexity:**
- - 𝑂(𝑛) — for the `dp` array.

### Example
**Input**
```python
power = [1, 1, 3, 5, 5, 5, 7]
```

**Output**
```python
21
```

**Explanation**

- Choose power = 1 → total = 2

- Skip 3 (conflicts with 1)

- Choose power = 5 (3 instances) → total = 15

- Choose power = 7 → total = 7

- Final total damage = 2 + 15 + 7 = 21

### Notes
This problem highlights the importance of **state dependency in dynamic programming** — similar to “House Robber”, but generalized for a variable exclusion range.