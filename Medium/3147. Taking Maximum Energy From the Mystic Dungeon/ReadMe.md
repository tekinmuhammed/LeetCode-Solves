# 3147. Taking Maximum Energy From the Mystic Dungeon  

## Difficulty: Medium  

## Problem Link  
[LeetCode - 3147. Taking Maximum Energy From the Mystic Dungeon](https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/)  

## Tags  
`Dynamic Programming` `Array` `Greedy`  

---

## Problem Description  
You are in a mystical dungeon represented by an array `energy`, where `energy[i]` indicates the energy gain or loss at room `i`.  

You can start from **any room** and move forward in steps of size `k`, collecting energy as you go (i.e., from room `i`, you can move to room `i + k`, `i + 2k`, etc., as long as the index is valid).  

Your goal is to **maximize the total energy** you can collect.

---

## Approach  

This is a **Dynamic Programming** problem that can be solved efficiently by working **backwards** from the end of the array.

### Intuition  
For each index `i`, we want to know the **maximum total energy** we can get starting from that room and moving forward in steps of size `k`.

If we move backwards from the end:  
- If `i + k` is within bounds, then  
  \[
  dp[i] = energy[i] + dp[i + k]
  \]  
- Otherwise, we can only take the energy of the current room:  
  \[
  dp[i] = energy[i]
  \]  

Finally, the answer is the **maximum value** in the `dp` array, because we can start from any room.

---

## Code Implementation  

```python
class Solution(object):
    def maximumEnergy(self, energy, k):
        """
        :type energy: List[int]
        :type k: int
        :rtype: int
        """
        n = len(energy)
        dp = [0] * n
        
        # dp[i] = max energy starting from room i and moving by k steps
        for i in range(n - 1, -1, -1):
            if i + k < n:
                dp[i] = energy[i] + dp[i + k]
            else:
                dp[i] = energy[i]
        
        return max(dp)
```

### Complexity Analysis

- **Time Complexity:** `𝑂(𝑛)` — we iterate once through the array backward.

- **Space Complexity:** `𝑂(𝑛)` — for the dp array.

### Example

**Input**
```python
energy = [5, 2, -10, -5, 1]
k = 3
```

**Output**
```python
3
```

### Explanation

- Start at index 1 (value = 2) → next valid step: index 4 (value = 1)

- Total = 2 + 1 = 3
This is the maximum possible total energy.