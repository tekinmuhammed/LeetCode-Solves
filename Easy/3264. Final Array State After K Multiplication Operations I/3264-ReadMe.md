# 🟨 LeetCode 3264 - Final Array State After K Multiplication Operations I

**Difficulty:** Easy  
**Problem Link:** [LeetCode 3264](https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/)

---

## 📘 Problem Description

You are given:

- An integer array `nums`
- An integer `k`
- An integer `multiplier`

You need to perform `k` operations. In each operation:

- Find the **smallest element** in `nums`.
- Multiply it by `multiplier`.
- Replace the original value with the result.

Return the final state of the array after performing all `k` operations.

---

## 🧪 Example

### Input
```python
nums = [1, 2, 3]
k = 3
multiplier = 2
```

### Output
```python
[4, 4, 6]
```

### Explanation

**Operations:**

1. Multiply 1 → `[2, 2, 3]`

2. Multiply 2 → `[4, 2, 3]`

3. Multiply 2 → `[4, 4, 3]`

Final result: `[4, 4, 3]` → sorted gives `[4, 4, 6]`

### 🚀 Approach

We simulate the `k` operations directly:

1. For each operation, find the **index of the smallest number** in the list.

2. Multiply that number by `multiplier`.

3. Update the list.

4. Repeat this process `k` times.

Although this is not the most optimal approach, it works within the constraints for small input sizes.

### ⏱️ Complexity

- **Time Complexity:** `O(k * n)`

- - For each of the `k` steps, we search for the minimum in the list (`O(n)`).

- **Space Complexity:** `O(1)`

- - In-place operations, no extra space used.

### 🏷️ Tags
`array`, `greedy`, `simulation`, `leetcode-easy`