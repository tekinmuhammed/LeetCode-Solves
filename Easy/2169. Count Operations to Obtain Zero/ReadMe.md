# 🔢 2169. Count Operations to Obtain Zero

**Difficulty:** Easy  
**Problem Link:** [LeetCode 2169](https://leetcode.com/problems/count-operations-to-obtain-zero/description/)

## 🧩 Problem Description
You are given two non-negative integers `num1` and `num2`.

In one **operation**, you must:
- Subtract the smaller number from the larger number.

Return the **number of operations** required to make **either `num1` or `num2` equal to 0**.

---

## 💡 Example

### Example 1
**Input:**
```python
num1 = 5, num2 = 2
```

**Output:**
```python
3
```

**Explanation:**
```python
(5, 2) → (3, 2) → (1, 2) → (1, 1) → (0, 1)

After 3 operations, one number becomes zero.
```
---

## 🧠 Intuition

The problem resembles the **Euclidean Algorithm** used to find the greatest common divisor (GCD).

Instead of performing **one subtraction at a time**, we can observe that:
- Subtracting `b` from `a` repeatedly until `a < b` is equivalent to doing:
```python
a = a % b
```

- And the number of such subtractions is:
```python
a // b
```

Thus, we can **count all those operations at once** instead of looping through them individually.

---

## 🧩 Implementation

```python
class Solution:
  def countOperations(self, num1: int, num2: int) -> int:
      # If either is zero, no operations are needed
      if num1 == 0 or num2 == 0:
          return 0

      ops = 0
      a, b = num1, num2

      # Repeat until one of the numbers becomes zero
      while a != 0 and b != 0:
          if a >= b:
              # Instead of subtracting one by one, count all at once
              ops += a // b
              a = a % b
          else:
              ops += b // a
              b = b % a

      return ops
```

### 🧮 Step-by-Step Example
##### Example
**Input:**
```python
num1 = 10, num2 = 4
```

**Process:**

| Step | a  | b | a >= b | ops added   | New a | New b | Total ops |
| ---- | -- | - | ------ | ----------- | ----- | ----- | --------- |
| 1    | 10 | 4 | ✅      | 10 // 4 = 2 | 2     | 4     | 2         |
| 2    | 2  | 4 | ❌      | 4 // 2 = 2  | 2     | 0     | 4         |


**✅ Output = 4**

### Explanation:
```python
(10,4) → (6,4) → (2,4) → (2,2) → (0,2)
```

It took 4 total operations.

### ⏱️ Complexity Analysis
| Type                 | Complexity                                              |
| -------------------- | ------------------------------------------------------- |
| **Time Complexity**  | `O(log(min(num1, num2)))` — same as Euclidean Algorithm |
| **Space Complexity** | `O(1)` — constant space used                            |

### 🧭 Summary
| Feature              | Description                                           |
| -------------------- | ----------------------------------------------------- |
| **Problem Type**     | Simulation / Math                                     |
| **Core Concept**     | Optimized Euclidean subtraction                       |
| **Approach**         | Replace repeated subtraction with division and modulo |
| **Time Complexity**  | `O(log n)`                                            |
| **Space Complexity** | `O(1)`                                                |

### 🧠 Key Insight
This problem can be solved much faster by noticing its connection to the GCD algorithm, where each step corresponds to a series of valid subtractions.

```python
countOperations(num1, num2)
⟶ number of steps Euclidean algorithm takes to reach 0
```