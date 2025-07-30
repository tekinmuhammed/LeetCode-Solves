# 3405. Count the Number of Arrays with K Matching Adjacent Elements

**Difficulty:** Hard  
**Problem Link:** [LeetCode 3405](https://leetcode.com/problems/count-the-number-of-arrays-with-k-matching-adjacent-elements/)

---

## Problem Description

Given integers `n`, `m`, and `k`, your task is to count how many arrays of length `n` can be formed where:
- Each element is between `1` and `m` (inclusive),
- Exactly `k` pairs of **adjacent** elements are equal.

Since the answer can be large, return it **modulo** `10⁹ + 7`.

---

## Example

### Input:
```python
n = 4, m = 2, k = 1
```
### Output:
```python
6
```
---

## Constraints

- `2 <= n <= 10⁵`
- `1 <= m <= 10⁵`
- `0 <= k <= n - 1`

---

## Approach

To solve this problem efficiently under the large constraints, we use **combinatorics** and **modular arithmetic**:

1. **Combinatorics Insight**:
   - We need exactly `k` adjacent equal pairs → choose `k` positions out of the `n - 1` possible adjacent positions.
   - There are `C(n - 1, k)` ways to choose which adjacent elements are equal.

2. **Value Assignment**:
   - Assign the **first element** in `m` ways.
   - Each **new group** (i.e., adjacent unequal pair) must be different from the previous → `m - 1` choices.
   - We need `n - k` groups in total, so we raise `(m - 1)` to the power `n - k - 1`.

3. **Final Formula**:
Total Arrays = C(n - 1, k) * m * (m - 1)^(n - k - 1)

---

### Time and Space Complexity

- **Time Complexity:**

- - Preprocessing factorials: `O(MX)`

- - Query execution: `O(log MOD)` due to modular exponentiation and inverse.

- **Space Complexity:** `O(MX)` for factorials and inverse factorials.

### Tags

`Combinatorics`, `Math`, `Dynamic-Programming`, `Modular-Arithmetic`, `Prefix-Products`

### Notes

- This problem emphasizes understanding group patterns in arrays.

- The key is to divide the array into **equal** and **non-equal transitions**.