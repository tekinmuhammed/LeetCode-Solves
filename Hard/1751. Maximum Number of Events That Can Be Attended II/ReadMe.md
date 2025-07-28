# 1751. Maximum Number of Events That Can Be Attended II

**Difficulty:** Hard  
**Link:** [LeetCode 1751](https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/)

---

## Problem Description

You are given an array of events where `events[i] = [startDay_i, endDay_i, value_i]`. You can attend **at most `k` non-overlapping events**.

Return the **maximum sum of values** that can be obtained by attending events, given that:

- You may **not attend two events that overlap in time** (i.e., their date ranges intersect),
- You may attend **at most `k` events**.

---

## Constraints

- `1 <= k <= events.length <= 10⁴`
- `1 <= startDay_i <= endDay_i <= 10⁹`
- `1 <= value_i <= 10⁶`

---

## Example

### Input:
```python
events = [[1,3,4],[2,4,3],[3,5,1]]
k = 1
```

### Output:
```python
4
```

### Explanation:

Attend the first event only, which gives the maximum value `4`.

### Approach & Intuition

This problem combines **interval scheduling** with **dynamic programming and binary search**.

We aim to maximize the total value by selecting at most `k` non-overlapping events.

### Algorithm

1. **Sort** the events based on their start day.

2. Use **binary search** to find the next non-overlapping event after attending a current event.

3. Use **memoized DFS (top-down DP)** to store the maximum value at each state:
`dp[count][cur_index]` – the max value from index `cur_index` with `count` events left.

4. At each step:

- **Skip** the current event and move to the next.

- **Take** the current event: add its value + result of next available event.

### Time and Space Complexity

- **Time Complexity:** `O(k * N log N)`

- - `N` is the number of events.

- - Each state uses binary search → `log N`.

- - Total states: `O(k * N)`

- **Space Complexity:** `O(k * N)`

- - DP table stores intermediate results for memoization.

### Tags

`Dynamic-Programming`, `Binary-Search`, `DFS`, `Memoization`, `Greedy-Scheduling`

### Notes

- Binary search is used to efficiently find the next non-overlapping event.

- Top-down memoized recursion avoids recomputing overlapping subproblems.