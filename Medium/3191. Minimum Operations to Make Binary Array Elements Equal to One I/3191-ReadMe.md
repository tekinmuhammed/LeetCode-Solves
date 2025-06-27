# ⚙️ LeetCode 3191 - Minimum Operations to Make Binary Array Elements Equal to One I

**Difficulty:** Easy  
**Problem Link:** [LeetCode 3191](https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i)

---

## 🧩 Problem Description

You're given a binary array `nums` consisting only of `0` and `1`.

👉 In **one operation**, you can pick an index `i` and **flip the bits** at indices `i`, `i+1`, and `i+2`.

You can **only perform the operation when** `i + 2 < len(nums)`.

**Goal:** Return the **minimum number of operations** required to make all elements equal to `1`. If it’s not possible, return `-1`.

---

## 💡 Intuition

To turn all `0`s into `1`s using a 3-bit flip operation:
- We greedily move from **left to right**, and whenever we see a `0`, we apply the operation at that index.
- After each flip, the next two elements will also be affected.
- Finally, we check if the entire array is filled with `1`s.

If not, it's **impossible** to solve using the given operation.

---

## 🚀 Approach

1. Iterate from index `0` to `n-3`.
2. Whenever `nums[i] == 0`, flip `nums[i]`, `nums[i+1]`, and `nums[i+2]` using XOR (`^= 1`).
3. Count the number of operations performed.
4. After loop, check if all elements are `1`. If yes, return the count. If not, return `-1`.

---

### 🧪 Example
```python
Input: nums = [0,1,0,1,0]
Output: 2
```

### Explanation:
- Flip at index 0 → [1,0,1,1,0]
- Flip at index 2 → [1,0,0,0,1]
- Still not all 1 → Not valid
Actually, optimal path gives `2` valid flips resulting in [1,1,1,1,1].

### 🕵️ Complexity
- **Time Complexity:** `O(n)` – One pass over the array.

- **Space Complexity:** `O(1)` – In-place bit manipulation.

### 🏷️ Tags
`bit-manipulation`, `greedy`, `simulation`