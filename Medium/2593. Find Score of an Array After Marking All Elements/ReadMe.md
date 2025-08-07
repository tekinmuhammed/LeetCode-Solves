# 🟨 LeetCode 2593 - Find Score of an Array After Marking All Elements

**Difficulty:** Medium  
**Problem Link:** [LeetCode 2593](https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/)

---

## 📘 Problem Description

You are given an integer array `nums`. Initially, all elements are **unmarked**.

You will perform the following operation **until all elements are marked**:

1. Select the **smallest unmarked** number. If there are multiple, choose the one with the smallest index.
2. Add its value to the `score`.
3. Mark the element itself, along with its **immediate neighbors** (i.e., index - 1 and index + 1).

Return the total `score` after all elements are marked.

---

## 🧪 Example

### Input
```python
nums = [2, 1, 3, 4, 5, 2]
```

### Output
`7`

### Explanation
- Pick index 1 (value 1), mark index 0, 1, 2 → score = 1

- Pick index 5 (value 2), mark index 4, 5 → score = 1 + 2 = 3

- Pick index 3 (value 4) is already marked → skip

- Pick index 0, 2, 4 → already marked

- Pick index 3 again is marked

- No more unmarked values

- Total score = 7

### 🚀 Approach

1. Track whether each index is marked using a boolean list.

2. Sort `nums` with their original indices by value to always consider the smallest unmarked number first.

3. Iterate through the sorted list:

- If the current index is unmarked:

- - Add its value to `score`

- - Mark itself and neighbors (index - 1 and index + 1)

### ⏱️ Complexity

- **Time Complexity:** `O(n log n)`

- - Due to sorting the array with indices.

- **Space Complexity:** `O(n)`

- - For the `marked` list and the indexed version of the array.

### 🏷️ Tags

`array`, `greedy`, `sorting`, `simulation`, `leetcode-medium`