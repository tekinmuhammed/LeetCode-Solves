# 3439. Reschedule Meetings for Maximum Free Time I

**Difficulty:** Medium  
**Link:** [LeetCode 3439](https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i)

---

## Problem Description

You are given:
- `eventTime`: the total duration of a time window.
- Two arrays, `startTime` and `endTime`, representing `n` non-overlapping meetings already scheduled.
- An integer `k` representing the number of **consecutive meetings** you are allowed to **reschedule**.

Your goal is to **reschedule exactly `k` consecutive meetings** (move them out of the time window), and maximize the **total free time** within the window `[0, eventTime]`.

Return the **maximum free time** possible.

---

## Constraints

- `1 <= k <= startTime.length <= 10⁵`
- `0 <= startTime[i] < endTime[i] <= eventTime <= 10⁹`
- Meetings are sorted by `startTime` and do not overlap.

---

## Example

### Input
```python
eventTime = 10
k = 2
startTime = [1, 3, 6]
endTime = [2, 5, 8]
```

### Output
```python
7
```

### Explanation

- Remove meetings [3,5] and [6,8].

- Remaining meeting: [1,2]

- Free time: `[0,1]` + `[2,10]` = 1 + 8 = 9, but you must **remove exactly 2** meetings.

- The maximum achievable free time when **removing 2 consecutive** meetings is 7.

### Approach & Intuition

We must **remove exactly k consecutive meetings** to maximize free time.

#### Idea:

-  The total meeting time within `[0, eventTime]` is fixed.

- We **slide a window of size `k`** over all possible consecutive meetings to remove.

- For each window:

- - Compute how much **free time** it would create.

- - Track the maximum.

We use **prefix sums** to quickly compute the total duration of the meetings inside each window.

### Time and Space Complexity

- **Time Complexity:** `O(n)`

- - One pass to compute prefix sum.

- - One pass to evaluate all possible windows of size `k`.

- **Space Complexity:** `O(n)`

- - For the prefix sum array.

### Tags

`Greedy`, `Sliding-Window`, `Prefix-Sum`, `Optimization`

### Notes

- The key to solving this efficiently is using **prefix sums** for constant-time range sum queries.

- Sliding window technique helps scan through all valid groups of `k` meetings to remove.