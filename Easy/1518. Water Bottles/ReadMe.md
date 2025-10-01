# 1518. Water Bottles  

## Difficulty: Easy  
## Problem Link  
[LeetCode - 1518. Water Bottles](https://leetcode.com/problems/water-bottles/)  

## Tags  
`Math` `Simulation`  

---

## Problem Description  
You have `numBottles` full water bottles. You can exchange `numExchange` empty bottles for one full bottle of water.  

Each time you drink a full bottle, it becomes empty. You can then exchange empty bottles to get new full bottles.  

Return the **maximum number of water bottles you can drink**.  

---

## Approach  

- Start with `numBottles` full bottles, keep track of both:  
  - `total`: total bottles drunk  
  - `empty`: empty bottles collected  
- While you have enough empty bottles to exchange (`empty >= numExchange`):  
  - Exchange them for new full bottles  
  - Update the counters accordingly  
- Continue until no more exchanges are possible.  
- Return the total count.  

---

## Code Implementation  

```python
class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        total = numBottles
        empty = numBottles
        
        while empty >= numExchange:
            new_full = empty // numExchange
            total += new_full
            empty = empty % numExchange + new_full
        
        return total
```

### Complexity Analysis
**Time Complexity:**
- `𝑂(log⁡𝑛𝑢𝑚𝐸𝑥𝑐ℎ𝑎𝑛𝑔𝑒(𝑛𝑢𝑚𝐵𝑜𝑡𝑡𝑙𝑒𝑠))` since the number of exchanges reduces empty bottles each iteration.

**Space Complexity:**
- `𝑂(1)` constant extra space.

### Example
**Input:**
```python
numBottles = 9, numExchange = 3
```

**Process:**
```python
Drink 9 → empty = 9
Exchange 9 // 3 = 3 → drink 3 → total = 12 → empty = 3
Exchange 3 // 3 = 1 → drink 1 → total = 13 → empty = 1
```

**Output:**
```python
13
```