# 2410. Maximum Matching of Players With Trainers

**Difficulty:** Medium  
**Link:** [LeetCode 2410](https://leetcode.com/problems/maximum-matching-of-players-with-trainers)

---

## Problem Description

You are given two integer arrays:

- `players`: representing the strength of each player.
- `trainers`: representing the training capacity of each trainer.

Each player can be matched with at most one trainer **whose training capacity is greater than or equal to the player's strength**.

Return the **maximum** number of matchings you can make.

---

## Example

### Input
```python
players = [4, 7, 9]
trainers = [8, 2, 5, 8]
```

### Output
```python
2
```

### Explanation

- Match player 4 with trainer 5

- Match player 7 with trainer 8

- Player 9 cannot be matched

### Constraints

- `1 <= players.length, trainers.length <= 10^5`

- `1 <= players[i], trainers[i] <= 10^9`

### Approach & Explanation

This is a classic **two-pointer greedy algorithm** problem.

### Key Strategy:

- Sort both `players` and `trainers`.

- Traverse both arrays using two pointers `i` and `j`.

- For each player, find the next trainer with capacity ≥ player’s strength.

- If a match is found, increase the count and move both pointers.

### Time and Space Complexity

- **Time Complexity:**

- - `O(n log n)` for sorting players and trainers.

- - `O(n)` for two-pointer traversal.

- **Space Complexity:**

- - `O(1)` extra space (in-place sort and constant pointers).

### Tags
`Greedy`, `Two-Pointers`, `Sorting`, `Matching`

### Summary
This problem is a perfect example of **greedy matching**, where sorting helps align compatible elements efficiently.
Using two pointers ensures we don’t revisit any player or trainer, keeping the solution optimal and clean.