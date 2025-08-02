# 🎯 LeetCode 2054 - Two Best Non-Overlapping Events

**Difficulty:** Hard  
**Problem Link:** [LeetCode 2054](https://leetcode.com/problems/two-best-non-overlapping-events/)

---

## 📘 Problem Description

You are given a list of events. Each event is represented as a list of:
- `[startTime, endTime, value]`.

You may attend **at most two non-overlapping events**.  
Return the **maximum total value** you can achieve.

> Two events are **non-overlapping** if the start time of one is after the end time of the other.

---

## 🧪 Example

### Input:
```python
events = [[1,3,4],[2,4,3],[3,5,1]]
```

### Output:
```python
7
```

## Explanation:

- Choose events [1,3,4] and [3,5,1] → total = 4 + 3 = 7

## 🚀 Approach

1. **Sort events by their `end time`**
To help with binary search for compatible events.

2. Precompute:
- A list of `end_times`

- `max_values[i]` = maximum value among first `i` events (ending before or at event `i`)

3. For each event:
- Use **binary search** (`bisect_right`) to find the latest event that ends before this one starts.

- Add their values if found. Track the best total value.

## ⏱️ Complexity

- **Time Complexity:** `O(n log n)`

- - Sorting: `O(n log n)`

- - Binary search for each event: `O(log n)`

- Space Complexity: O(n)

## 🏷️ Tags

`greedy`, `sorting`, `binary-search`, `intervals`, `dp-like`, `leetcode-hard`