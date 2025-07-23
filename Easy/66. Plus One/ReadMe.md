# ➕ LeetCode 66 - Plus One

**Difficulty:** Easy  

**Problem Link:** [LeetCode 66](https://leetcode.com/problems/plus-one)

---

## 📘 Problem Description

You are given a **large integer** represented as an array of digits. Each element in the array contains a single digit, and the digits are stored such that the **most significant digit is at the head** of the list.

You must **add one** to this number and return the resulting array of digits.

---

## 🧪 Example

### Input:
```python
digits = [1, 2, 3]
```

### Output:
```python
[1, 2, 4]
```

### Explanation:

- `123 + 1 = 124`

### Input:
```python
digits = [9, 9, 9]
```

### Output:
```python
[1, 0, 0, 0]
```

### 🚀 Approach

We iterate **backwards** through the list:

- If the digit is less than `9`, we can simply add `1` and return the result.

- If the digit is `9`, we set it to `0` and continue the loop to handle the carry.

- If all digits were `9`, we return `[1] + [0]*n`.

This simulates how manual addition with carry works.

### ⏱️ Complexity

- **Time Complexity:** `O(n)`

- **Space Complexity:** `O(1)` (ignoring output list)

### 🏷️ Tags
`array`, `math`, `simulation`, `leetcode-easy`