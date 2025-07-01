# 🍬 LeetCode 2929 - Distribute Candies Among Children II

**Difficulty:** Medium  
**Problem Link:** [LeetCode 2929](https://leetcode.com/problems/distribute-candies-among-children-ii)

---

## 📘 Problem Description

We need to find how many ways we can **distribute `n` candies** to **3 children** such that:
- Each child gets **at most `limit`** candies.
- All candies are distributed (i.e., the total must be exactly `n`).

Return the total number of such valid distributions.

---

## 💡 Mathematical Insight

This is a classic **integer partition with upper bounds** problem.

### Step 1: Unbounded Integer Partitions

The total number of **non-negative integer solutions** to:

> `x + y + z = n`

... is:

> **C(n + 2, 2)** = `(n + 2)(n + 1) / 2`

This assumes **no upper bound** on the number of candies per child.

---

### Step 2: Inclusion-Exclusion to Apply the Limit

We subtract the **invalid cases** where any child gets more than `limit` candies.

Let’s define:

- **total** = number of unbounded distributions.
- **over1** = subtract when **one child** exceeds the limit.
- **over2** = add back when **two children** exceed the limit (since subtracted twice).
- **over3** = subtract again if **all three** exceed the limit.

This is done via **inclusion-exclusion principle**.

---

### 🧮 Example
```python
Input: n = 5, limit = 2

Valid distributions:
(1,2,2), (2,1,2), (2,2,1), (1,1,3) ❌ (invalid), etc.

Output: 6
```

### ⏱️ Time & Space Complexity

- **Time Complexity:** `O(1)`

- **Space Complexity:** `O(1)`

### 🏷️ Tags
`combinatorics`, `math`, `inclusion-exclusion`, `dp-(optional)`