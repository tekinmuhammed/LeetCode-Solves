# 2402. Meeting Rooms III

**Difficulty:** Hard  
**Link:** [LeetCode 2402](https://leetcode.com/problems/meeting-rooms-iii)

---

## Problem Description

You are given:
- `n` meeting rooms labeled from `0` to `n - 1`,
- A list of `meetings`, where each meeting is defined by its `[start, end]` time.

Each meeting must be assigned to a room:
- If multiple rooms are free at the meeting's `start` time, assign it to the **room with the smallest number**.
- If **no rooms are available**, the meeting waits until the earliest room becomes free. Then it takes place immediately, preserving its original **duration**.

Return the **ID of the room that hosted the most meetings**.  
If there’s a tie, return the room with the **smallest number**.

---

## Example

### Input
```python
n = 2
meetings = [[0,10],[1,5],[2,7],[3,4]]
```

### Output
```python
0
```

### Explanation

- Room 0 gets meeting [0,10]

- Room 1 gets [1,5]

- Room 1 gets [5,7]

- Room 1 gets [7,10]

Room 1 hosted 3 meetings, room 0 hosted 1.

### Constraints

- `1 <= n <= 100`

- `1 <= meetings.length <= 10⁵`

- `0 <= start < end <= 10⁹`

- Meetings are sorted by their `start` time.

### Approach & Intuition

**Naive Simulation with Greedy Assignment**

1. **Track Availability:**

- `times[i]` represents the next available time for room `i`.

2. **Iterate Over Meetings:**

- For each meeting, check if any room is available by its `start` time.

- If yes, assign it to the room with the **smallest index.**

- If not, find the room that becomes free the earliest (`minind`) and **delay the meeting** until that room is free.

3. **Count Assignments:**

- Maintain an `array ans[i]` to track how many meetings each room has handled.

4. **Return Result:**

- Return the index with the maximum meeting count.

### Time and Space Complexity

- **Time Complexity:** `O(m * n)`, where `m = len(meetings)`

- We check each room (up to `n`) for every meeting.

- Can be optimized to **O(m log n)** using a priority queue (heap).

- **Space Complexity:** `O(n)`

- For tracking room usage and availability.

### Optimization Note

This implementation is naive but valid. For performance on large inputs:

- Use two heaps:

- - One for **available rooms** (sorted by index).

- - One for **busy rooms** (sorted by availability time).

- This reduces complexity to **O(m log n).**

### Tags
`Greedy`, `Simulation`, `Priority-Queue`, `Scheduling`, `Intervals`

### Summary
This problem simulates real-world meeting room allocation with constraints.
Although the current approach uses linear search, it's effective for small `n`.
For larger inputs, it’s recommended to use a heap-based strategy for better performance.