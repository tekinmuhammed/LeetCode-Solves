# 🔧 LeetCode 2594 - Minimum Time to Repair Cars

**Difficulty:** Medium  
**Problem Link:** [LeetCode 2594](https://leetcode.com/problems/minimum-time-to-repair-cars)

---

## 📝 Problem Description

You are given:
- An array `ranks` where `ranks[i]` is the time it takes for the i-th mechanic to repair **1 car**.
- An integer `cars`, representing the total number of cars that need to be repaired.

Each mechanic can repair multiple cars. The time taken by a mechanic to repair `n` cars is `ranks[i] * n²`.

👉 **Goal:** Find the **minimum time** needed to repair all cars using all mechanics optimally.

---

## 🔍 Example

```python
Input: ranks = [4, 2, 3, 1], cars = 10  
Output: 16  
Explanation: The optimal strategy may involve distributing cars like [0, 2, 3, 5] across the mechanics.
```

### 💡 Key Insight

Since the time taken to repair cars increases quadratically, we must:

- **Minimize the total time** needed to repair all `cars`.

- Use **binary search on time** to efficiently find the minimum time that suffices.

### 🔨 Approach

1. **Binary search** the answer between `left = 1` and `right = min(ranks) * cars^2`.

2. For each `mid`, simulate how many cars each mechanic can repair in that time using:

```python
repaired_by_i = floor(sqrt(time / ranks[i]))
```

3. If the total cars repaired is ≥ `cars`, the time is sufficient.

4. Narrow down search accordingly.

### ⏱️ Complexity

- **Time Complexity:** `O(n * log(max_time))`, where `max_time = min(ranks) * cars^2`

- **Space Complexity:** `O(1)`

### 🏷️ Tags
`binary-search`, `greedy`, `math`, `optimization`, `medium`