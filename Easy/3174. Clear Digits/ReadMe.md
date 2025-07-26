# 🔡 LeetCode 3174 - Clear Digits

**Difficulty:** Easy  
**Problem Link:** [LeetCode 3174](https://leetcode.com/problems/clear-digits)

---

## 📘 Problem Description

You are given a string `s` consisting of lowercase letters and digits.

The string represents a sequence of operations. When a **digit** appears, it **removes the closest preceding letter** (if any).

Return the final string after applying all the operations.

---

## 🧪 Example

### Input:

```python
s = "abc3d2"
```

### Output:
```python
"a"
```

### Explanation:

- `"abc"` → stack: `['a', 'b', 'c']`

- `'3'` → removes `'c'` → stack: `['a', 'b']`

- `'d'` → stack: `['a', 'b', 'd']`

- `'2'` → removes `'d'` → stack: `['a', 'b']`

Final result = `"ab"`

### 🚀 Approach

We use a **stack** to simulate the operations:

- If the character is a **letter**, push it to the stack.

- If it's a **digit**, and there's a letter on top of the stack, pop it (simulate removal).

- Digits themselves are never added to the stack.

Return the joined stack as the final result.

### ⏱️ Complexity

- **Time Complexity**: `O(n)`

- **Space Complexity**: `O(n)`

### 🏷️ Tags

`stack`, `string`, `simulation`, `leetcode-easy`