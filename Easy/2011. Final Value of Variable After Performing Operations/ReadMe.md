# ⚙️ 2011. Final Value of Variable After Performing Operations

**Difficulty:** Easy  
**Problem Link:** [LeetCode 2011](https://leetcode.com/problems/final-value-of-variable-after-performing-operations/description)

## 💡 Problem Description
You are given a list of strings `operations`, where each operation is one of the following:
- `"++X"` or `"X++"` → increases the value of variable `X` by 1  
- `"--X"` or `"X--"` → decreases the value of variable `X` by 1  

Initially, `X = 0`.  
After performing **all** operations in the list, return the **final value of X**.

---

## 🧠 Approach

The problem is straightforward — we simulate the changes to `X` by checking each operation string.

1. Initialize `X = 0`.
2. Loop through each string in `operations`:
   - If the string contains `'+'`, increment `X`.
   - Otherwise, decrement `X`.
3. Return the final value of `X`.

---

## 🧩 Code Implementation

```python
class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        X = 0
        for op in operations:
            if '+' in op:
                X += 1
            else:
                X -= 1
        return X
```

### 🧪 Example
**Input:**
```python
operations = ["--X","X++","X++"]
```

### Process:

- "--X" → X = -1

- "X++" → X = 0

- "X++" → X = 1

### Output:
```python
1
```

### ⏱️ Complexity Analysis

- **Time Complexity:**	`O(n)` — iterate through each operation once
- **Space Complexity:**	`O(1)` — only one integer variable used

### 🏁 Summary
 ✅ Simple simulation problem
✅ String check using '+' in op for conciseness
✅ Works for both prefix and postfix increment/decrement forms

### Tags: 
`String`, `Simulation`
