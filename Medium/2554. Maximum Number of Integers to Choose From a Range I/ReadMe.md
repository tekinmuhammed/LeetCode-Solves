# 📊 LeetCode 2554 - Maximum Number of Integers to Choose From a Range I

**Difficulty:** Easy  
**Problem Link:** [LeetCode 2554](https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i)

---

## 📘 Problem Description

You are given three inputs:

- An integer `n` (upper bound of the range `[1, n]`)
- A list of banned numbers
- An integer `maxSum` (maximum total sum allowed)

Select as many integers as possible from `[1, n]` such that:

- None of the selected numbers are in the `banned` list.
- The total sum of selected numbers does **not** exceed `maxSum`.

---

## 🧪 Example

### Input:
```python
banned = [1, 6, 5]
n = 5
maxSum = 6
```

## Output:
```python
2
```

## Explanation:

- Allowed numbers from 1 to 5 are `[2, 3, 4]`.

- The best we can do without exceeding `maxSum = 6` is: `[2, 3]`, which sums to 5.

- So the answer is 2 numbers.

## 🚀 Approach

- Convert `banned` list to a set for O(1) lookup.

- Iterate from 1 to `n`:

- - If a number is not banned and doesn't make the `current_sum` exceed `maxSum`, include it.

- Keep track of how many valid numbers are added.

## ⏱️ Complexity

- **Time Complexity:** `O(n)`

- **Space Complexity:** `O(b)`, where `b` is the number of banned elements

## 🏷️ Tags

`greedy`, `simulation`, `banned-elements`, `prefix-sum`, `leetcode-easy`