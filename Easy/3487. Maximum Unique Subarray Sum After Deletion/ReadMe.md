# 3487. Maximum Unique Subarray Sum After Deletion

**Difficulty:** Easy  
**Problem Link:** [LeetCode 3487](https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion/)

---

## Problem Description

You are given an integer array `nums`. Your task is to delete **at most one** element from `nums` so that all remaining **positive integers are unique**.

Your goal is to **maximize the sum** of all positive integers after the (optional) deletion.

Return the **maximum possible sum** after at most one deletion.

---

### Example 1

**Input:**
```python
nums = [2, 2, 1]
```

**Output:**
```python
3
```

### Explanation:

- If we remove one of the `2`s, we are left with `[2, 1]` which are unique positives.

- Sum = 2 + 1 = 3

### Example 2

**Input:**

```python
nums = [-1, -1, -1]
```

**Output:**
```python
-1
```

### Explanation:

- All values are negative.

- Best we can do is keep the single maximum: -1

### Approach

- The goal is to **maximize the sum of unique positive numbers**, possibly by deleting at most one element to make the set unique.

- Negative numbers don’t contribute to the score, but if all numbers are negative or zero, the result is the maximum element.

### Strategy:

1. **Filter positive numbers.**

2. **If all numbers are non-positive**, return the **maximum** (best of the worst).

3. Otherwise:

- Use a `set` to collect positive unique numbers.

- Return the sum of that set.

> Since we are allowed to delete at most one element, removing a duplicate is always enough to make the set unique (at worst, one conflict to resolve).

### Complexity

- **Time Complexity:** `O(n)`
One pass to filter and sum, one pass to get max.

- **Space Complexity:** `O(n)`
For the set of unique positive numbers.

### Tags

`HashSet`, `Greedy`, `Array`, `Math`

### Key Insight

- Only **one deletion** is allowed, so keeping one copy of each positive number ensures we meet the constraint.

- Negative numbers can be ignored unless **all elements are non-positive**, in which case we return the largest among them.