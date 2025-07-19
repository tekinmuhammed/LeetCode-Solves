# 3440. Reschedule Meetings for Maximum Free Time II

**Difficulty:** Hard  
**Link:** [LeetCode 3440](https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-ii)

---

## Problem Description

You are given a list of **non-overlapping** meetings with their `startTime` and `endTime`, all scheduled within a time window `[0, eventTime]`. You're allowed to **remove at most one meeting** and **reschedule it anywhere**, with the goal of maximizing the **longest free time segment** in the schedule.

Return the **maximum free time** that can be achieved by moving **at most one** meeting.

---

## Constraints

- `1 <= startTime.length <= 10⁵`
- `0 <= startTime[i] < endTime[i] <= eventTime <= 10⁹`
- Meetings are sorted by `startTime` and do not overlap.

---

## Example

### Input
```python
eventTime = 10
startTime = [1, 3, 6]
endTime = [2, 5, 8]
```

### Output
```python
5
```

### Explanation

- Initially, free intervals: [0,1], [2,3], [5,6], [8,10] → max = 2.

- By rescheduling meeting [3,5] to a better time, the gap between [2,6] becomes larger, so the longest free time increases to **5**.

### Approach & Intuition

We are allowed to **move at most one meeting** to any location in the event timeline.
To maximize the **longest free time**, we simulate:

- **Original forward gaps** — and track the worst-case meeting to remove (from left to right).

- **Reverse gaps** — do the same from right to left.

- At each position, we consider whether **removing that meeting** and **joining neighboring gaps** would create a longer free segment.

The algorithm uses:

- Two passes:

1. Forward (left to right): track maximum gap created by removing a meeting.

2. Backward (right to left): same idea, ensuring all possible gaps are considered.

- Updates the result with the largest possible free time segment encountered.

### Time and Space Complexity

- **Time Complexity:** `O(n)`

- One forward and one backward pass over the meetings.

- **Space Complexity:** `O(1)`

- Only constant auxiliary variables used.

### Tags

`Greedy`, `Sliding-Window`, `Optimization`, `Intervals`, `Two-Pointers`

### Notes

- This is an optimization version of [3440 Part I](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/3439.%20Reschedule%20Meetings%20for%20Maximum%20Free%20Time%20I) but more complex due to the flexible rescheduling constraint.

- Forward and backward traversal ensures **all meeting removals are evaluated symmetrically.**