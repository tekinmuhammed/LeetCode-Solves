# 1665. Minimum Initial Energy to Finish Tasks

**Difficulty:** Hard  
**Problem Link:** [LeetCode 1665](https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/description/)

---

## Problem
You are given an array `tasks` where `tasks[i] = [actual_i, minimum_i]`:
* `actual_i` is the actual amount of energy you spend to finish the $i^{th}$ task.
* `minimum_i` is the minimum amount of energy you require to begin the $i^{th}$ task.

For example, if the task is `[10, 12]` and your current energy is `11`, you cannot start this task. However, if your current energy is `13`, you can complete this task, and your energy will be `3` afterwards.

You can finish the tasks in **any order**.

Return the **minimum initial amount of energy** you need to finish all the tasks.

---

# Approach

This problem is beautifully solved using a **Greedy approach combined with Reverse Thinking**.

To minimize the initial energy, if we were simulating from the beginning, we would want to execute tasks that have the largest "free energy gap" (the difference between `minimum` and `actual`) first. These tasks require a high threshold to start but consume very little, leaving plenty of energy for subsequent tasks.

Instead of trying to find the starting energy from the beginning, your code ingeniously calculates it **backwards**:
1. **Sort Ascending by Gap:** We sort the tasks based on the difference `minimum - actual` in *ascending* order. This order represents the exact **reverse** of the optimal execution order. We are essentially looking at the last task to be executed, then the second to last, all the way up to the first.
2. **Work Backwards:** We maintain a running total, `ans`, which represents the energy we *must have* after finishing the remaining tasks. Initially, at the very end of all tasks, we need `0` energy.
3. **Update Requirement:** For each task in this reversed sequence, we ask: *"How much energy did I need before starting this task?"*
   * To have `ans` energy left after consuming `actual` energy, we must have started with at least `ans + actual`.
   * However, the task itself dictates that we must have at least `minimum` energy just to start it.
   * Therefore, the energy required before this task is the maximum of these two constraints: `max(ans + actual, minimum)`.

---

# Example Walkthrough

Consider the tasks: `[[1, 2], [2, 4], [4, 8]]`

1. **Calculate Gaps (`minimum - actual`):**
   * Task 0: `2 - 1 = 1`
   * Task 1: `4 - 2 = 2`
   * Task 2: `8 - 4 = 4`

2. **Sort Ascending:** 
   The tasks are already sorted by gap: `[[1, 2], [2, 4], [4, 8]]`

3. **Simulate Backwards:**
   * **Start:** `ans = 0`
   * **Process `[1, 2]` (The last task to be executed):** 
     `ans = max(0 + 1, 2) = 2`
   * **Process `[2, 4]`:** 
     `ans = max(2 + 2, 4) = 4`
   * **Process `[4, 8]` (The first task to be executed):** 
     `ans = max(4 + 4, 8) = 8`

**Result:** `8` is the minimum initial energy required.

---

# Complexity Analysis

Time Complexity

O(N log N)

Sorting the `tasks` array takes $O(N \log N)$ time, where `N` is the number of tasks. The subsequent iteration through the array takes $O(N)$ time. The overall time complexity is dominated by the sorting step.

Space Complexity

O(1) auxiliary

We only use a single integer variable `ans` to keep track of the result. (Note: Depending on the language implementation, the sorting algorithm itself might use $O(N)$ memory, such as Python's Timsort, but the algorithm's auxiliary space is considered O(1)).

---

# Code

```python
class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[1] - x[0])
        ans = 0
        for task in tasks:
            ans = max(ans + task[0], task[1])
        return ans
```