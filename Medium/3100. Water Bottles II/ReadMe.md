# 3100. Water Bottles II  

## Difficulty  
Medium  

## Problem Link  
[LeetCode - 3100. Water Bottles II](https://leetcode.com/problems/water-bottles-ii/)  

## Tags  
`Math` `Simulation`  

---

## Problem Description  
You start with `numBottles` full water bottles. Each time you drink a full bottle, it becomes empty.  

Initially, you can exchange `numExchange` empty bottles for one full bottle of water. **After each exchange, the required number of empty bottles to exchange increases by 1.**  

Return the **maximum number of water bottles you can drink**.  

---

## Approach  

- Start with `numBottles` full bottles.  
- Keep track of:  
  - `total`: number of bottles drunk  
  - `empty`: number of empty bottles collected  
- While you can exchange (`empty >= numExchange`):  
  - Perform an exchange → drink 1 new bottle  
  - Increase total count  
  - Update empty bottles (`empty -= numExchange; empty += 1`)  
  - Increase the required exchange cost (`numExchange += 1`)  
- Stop when you cannot exchange anymore.  
- Return `total`.  

---

## Code Implementation  

```python
class Solution(object):
    def maxBottlesDrunk(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        total = numBottles
        empty = numBottles
        
        while empty >= numExchange:
            empty -= numExchange
            total += 1
            empty += 1
            numExchange += 1
        
        return total
```

### Complexity Analysis
**Time Complexity:** 
- 𝑂(𝑘), where k is the number of exchanges until bottles run out (bounded by total bottles).

**Space Complexity:**
- 𝑂(1) constant extra space.

### Example
**Input:**
```python
numBottles = 13, numExchange = 6
```

**Process:**
```python
Drink 13 → empty = 13
Exchange 6 → drink 1 → total = 14 → empty = 8 → next exchange = 7
Exchange 7 → drink 1 → total = 15 → empty = 2 → next exchange = 8
```

**Output:**
```python
15
```