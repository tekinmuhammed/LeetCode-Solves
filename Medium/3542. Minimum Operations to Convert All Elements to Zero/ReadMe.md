# ⚙️ 3542. Minimum Operations to Convert All Elements to Zero

**Difficulty:** Medium  
**Problem Link:** [LeetCode 3542](https://leetcode.com/problems/minimum-operations-to-convert-all-elements-to-zero/description/)

## 🧩 Problem Description
You are given an integer array `nums`.

In one operation, you can:
- **Choose any positive integer `x`** and **subtract `x` from all elements** in a contiguous subarray of `nums`, such that **every element in that subarray is greater than or equal to `x`**.

Return the **minimum number of operations** required to make **all elements in `nums` equal to zero**.

---

## 💡 Example

### Example 1
**Input:**
```python
nums = [3, 3, 1, 2, 2]
```

**Output:**
```python
3
```

**Explanation:**
Possible sequence of operations:
1. Subtract `1` from the first 4 elements → `[2, 2, 0, 1, 2]`
2. Subtract `1` from the first 2 elements → `[1, 1, 0, 1, 2]`
3. Subtract `1` from all non-zero elements → `[0, 0, 0, 0, 0]`

Total = **3 operations**

---

## 🧠 Intuition

This problem is about recognizing **how many new “height levels” appear** as we scan through the array.

Each **increase in value** (compared to the previous minimum) represents the need for **a new operation** — since you’ll eventually have to perform at least one subtraction to “lower” this new peak.

We can simulate this idea using a **monotonic stack**:
- The stack keeps track of **current distinct increasing heights**.
- When a smaller number appears, we **pop** higher ones (since their effect ends).
- When a new larger number appears, we **push** it and **increment** our operation count.

This efficiently counts how many new "height levels" need separate subtraction operations.

---

## 🧩 Implementation

```python
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        s = []      # monotonic stack
        res = 0     # number of operations
        
        for a in nums:
            # If the current number is smaller, higher “levels” end here
            while s and s[-1] > a:
                s.pop()
            
            # Ignore zeros — no operations needed
            if a == 0:
                continue
            
            # If this height is new, we need a new operation
            if not s or s[-1] < a:
                res += 1
                s.append(a)
        
        return res
```

## 🧮 Step-by-Step Example
#### Example
**Input:**
```python
nums = [1, 3, 2, 0, 4]
Step	a	Stack (s)	Action	res
1	1	[1]	push 1	1
2	3	[1,3]	push 3 (new height)	2
3	2	[1,2]	pop 3, push 2	2
4	0	[]	pop all	2
5	4	[4]	push 4 (new start)	3
```

- ✅ Result = 3 operations

### ⏱️ Complexity Analysis
| Type                 | Complexity                               |
| -------------------- | ---------------------------------------- |
| **Time Complexity**  | `O(n)` — each element pushed/popped once |
| **Space Complexity** | `O(n)` — worst case stack usage          |

### 🧭 Summary
| Concept              | Description                                      |
| -------------------- | ------------------------------------------------ |
| **Problem Type**     | Greedy / Monotonic Stack                         |
| **Core Idea**        | Each new “increasing height” = one new operation |
| **Approach**         | Track distinct ascending values while scanning   |
| **Time Complexity**  | `O(n)`                                           |
| **Space Complexity** | `O(n)`                                           |

### 🧠 Key Insight
Think of the array as a **mountain landscape** —
Every time you **climb to a new height**, it means you’ll eventually need an extra operation to flatten that region down to zero.

### ✅ In short:
Each distinct increase in the sequence (after removing larger previous values) adds one to the total operation count.