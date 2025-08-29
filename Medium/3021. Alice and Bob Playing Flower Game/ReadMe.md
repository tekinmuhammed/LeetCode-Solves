# 3021. Alice and Bob Playing Flower Game

**Difficulty:** Easy  
**Link:** [LeetCode 3021](https://leetcode.com/problems/alice-and-bob-playing-flower-game/)

---

## Problem Description
Alice and Bob are playing a game with flowers.  
- Alice chooses a flower with `n` petals.  
- Bob chooses a flower with `m` petals.  
- Alice wins if the total number of petals is odd; otherwise, Bob wins.  

Return the number of scenarios where **Alice wins**.

---

## Example

### Input:
```python
n = 3
m = 2
```

### Output: 
```python
3
```

### Explanation:

- Alice has 3 options, Bob has 2 options → total 6 possible outcomes.

- Exactly half of them (3) lead to an odd total → Alice wins.

### Constraints

- 1 <= n, m <= 10^5

### Approach

**Key Idea:**

- The total number of possible pairs is `n * m`.

- Since half of them result in an odd sum, Alice's winning scenarios = `(n * m) // 2`.

- This avoids simulation and gives a direct mathematical solution.

### Time and Space Complexity

- **Time Complexity:** `O(1)`

- **Space Complexity:** `O(1)`

### Tags

`Math`, `Parity`, `Game-Theory`

### Notes

- The problem reduces to counting odd/even combinations rather than simulating the game.

- This is a pure mathematical solution and extremely efficient.