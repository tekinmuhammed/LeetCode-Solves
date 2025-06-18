# 🎨 LeetCode 3160 - Find the Number of Distinct Colors Among the Balls

**Difficulty:** Medium  
**Problem Link:** [LeetCode 3160](https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/)

---

## 🧩 Problem Description

You are given:
- An integer `limit` (total number of balls),
- A list of `queries`, where each query is a pair `[x, y]` meaning:
  - Paint ball number `x` with color `y`.

After each query, return the number of **distinct colors** currently used among all balls.

---

## 🔍 Example

### Input:
```python
limit = 4
queries = [[1, 5], [2, 6], [1, 7], [3, 7]]
```

### Output:
```python
[1, 2, 2, 2]
```

### Explanation:
- Ball 1 → Color 5 → distinct colors = {5}

- Ball 2 → Color 6 → distinct colors = {5,6}

- Ball 1 → Color 7 → now color 5 disappears → distinct colors = {6,7}

- Ball 3 → Color 7 (already exists) → no change

### 🧠 Approach & Intuition

We need to maintain:

1. `ball_colors`: current color assigned to each ball.

2. `color_frequency`: how many balls have a given color.

3. `distinct_colors_count`: updated after every query.

##### Steps:

- If the ball was previously painted, reduce the count of its old color.

- If the color count drops to 0, `decrement distinct_colors_count`.

- Update the ball’s new color.

- If it’s the first time this color is seen, increase `distinct_colors_count`.

### ⏱️ Complexity
- **Time Complexity:** `O(n)`, where `n` is the number of queries.

- **Space Complexity:** `O(n)`, for tracking color usage and ball colors.

### 🏷️ Tags
`hash-map`, `frequency-counter`, `simulation`, `tracking`, `arrays`