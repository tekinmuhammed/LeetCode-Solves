# 3443. Maximum Manhattan Distance After K Changes

**Difficulty:** Medium  
**Problem Link:** [LeetCode 3443](https://leetcode.com/problems/maximum-manhattan-distance-after-k-changes)

---

## Problem Description

You are given a string `s` of directions consisting of characters `'N'`, `'S'`, `'E'`, and `'W'`.  
You can change at most `k` of the directions to any other direction.

You need to return the **maximum Manhattan distance** from the origin `(0, 0)` that can be achieved by following the path described in `s` after making at most `k` changes.

- **Manhattan distance** between two points `(x1, y1)` and `(x2, y2)` is defined as: `abs(x1 - x2) + abs(y1 - y2)`.

---

## Example

### Input:
```python
s = "NESW", k = 1
```

### Output:
```python
3
```

### Explanation:

After changing one direction (e.g., change 'S' to 'N'), we can increase the distance.

### Constraints
- `1 <= s.length <= 10⁵`

- `0 <= k <= s.length`

### Approach

- Track the net effect of directions on latitude (`N`/`S`) and longitude (`E`/`W`).

- At each step `i`, compute the current Manhattan distance from the origin.

- Since we can make up to `k` changes, we can add up to `2 * k` units of distance.

- However, the final distance cannot exceed `i + 1`, since that’s the number of steps taken.

- So the maximum distance is:

```python
max_distance = min(current_distance + 2 * k, steps_taken)
```

- We take the maximum of such values across all steps.

### Time and Space Complexity

- **Time Complexity:** `O(n)` – One pass through the string.

- **Space Complexity:** `O(1)` – Constant space usage.

### Tags
`Greedy`, `Prefix-Sum`, `Manhattan-Distance`, `Simulation`

### Notes

- We simulate movement step-by-step and compute potential maximum distance under `k` allowed changes.

- Adding `2*k` is valid because each direction change can improve both latitude and longitude movement (e.g., turning an 'S' into an 'N').