# 1353. Maximum Number of Events That Can Be Attended

**Difficulty:** Medium  
**Link:** [LeetCode 1353](https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/)

---

## Problem Description

You are given an array of events where `events[i] = [startDay_i, endDay_i]`. You can attend only **one event per day**.

Return the **maximum number of events** you can attend.

---

## Constraints

- `1 <= events.length <= 10⁵`
- `1 <= startDay_i <= endDay_i <= 10⁵`

---

## Example

### Input:
```python
events = [[1,2],[2,3],[3,4]]
```

### Output:
`3`

### Explanation:
**Attend:**

- Day 1 → event [1,2]

- Day 2 → event [2,3]

- Day 3 → event [3,4]

### Approach & Intuition
This is a **greedy + min-heap** (priority queue) problem.

### Key Observations:

1. You can only attend one event per day.

2. You want to **always attend the event that ends the earliest**, to leave room for future events.

### Algorithm

1. **Sort events by start day.**

2. Use a **min-heap** to keep track of events' end days that are currently available.

3. Iterate day by day:

- Add all events that start on this day to the heap.

- Remove events from the heap that have already expired.

- Attend the event that ends earliest (pop from heap).

4. Increment the day and continue until no events remain.

### Time and Space Complexity

- **Time Complexity:** `O(N log N)`

- - Sorting events: O(N log N)

- - Heap operations (push/pop): O(log N) per event

- **Space Complexity:** `O(N)`

- - For the min-heap

### Tags
`Greedy`, `Heap`, `Priority-Queue`, `Sorting`, `Scheduling`

### Notes

- Using a min-heap ensures that we always attend the event that frees up the schedule the soonest.

- This approach handles overlapping events efficiently.