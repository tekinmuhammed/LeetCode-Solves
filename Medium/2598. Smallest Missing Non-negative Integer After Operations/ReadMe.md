# 🧩 2598. Smallest Missing Non-negative Integer After Operations

## 💡 Problem Description
You are given an integer array `nums` and an integer `value`.

In **one operation**, you can:
- choose any index `i`, and
- increase or decrease `nums[i]` by `value` any number of times (including zero).

After any number of operations, determine the **smallest non-negative integer (MEX)** that **cannot** be represented in the array.

Return this smallest missing integer.

---

## 🧠 Approach

We are allowed to modify any element by adding or subtracting multiples of `value`.  
Thus, the only thing that matters is the **remainder** of each element when divided by `value`.

### 🔹 Step 1. Normalize using modulo
Convert each element to its remainder modulo `value`.  
For example, if `value = 3`:

```python
nums = [1, 5, 7, 2]
remainders = [1, 2, 1, 2] # (5 % 3 = 2, 7 % 3 = 1)
```

This tells us how many numbers we can create that fall into each remainder bucket.

---

### 🔹 Step 2. Use a frequency counter
We count how many times each remainder occurs using `Counter`.

Example:
```python
count = {1: 2, 2: 2}
```

---

### 🔹 Step 3. Construct the smallest missing number (MEX)
We simulate constructing integers starting from `mex = 0`.  
For each `mex`, we check if we can "use up" a remainder:

- `remainder = mex % value`
- If `count[remainder] > 0`, we can form `mex` → decrement the count and move on.
- Otherwise, the current `mex` cannot be formed — this is the **answer**.

This process guarantees finding the smallest missing integer.

---

## 🧩 Code Implementation

```python
from collections import Counter

class Solution(object):
    def findSmallestInteger(self, nums, value):
        """
        :type nums: List[int]
        :type value: int
        :rtype: int
        """
        # Step 1: Normalize each number with modulo
        count = Counter(x % value for x in nums)
        
        # Step 2: Find smallest missing non-negative integer
        mex = 0
        while True:
            remainder = mex % value
            if count[remainder] > 0:
                count[remainder] -= 1
                mex += 1
            else:
                return mex
```

### 🧪 Example

**Input:**
```python
nums = [1, 2, 3, 4, 5]
value = 2
```

**Process:**
```python
Remainders: [1, 0, 1, 0, 1]
Counts: {1: 3, 0: 2}

mex = 0 → remainder = 0 → count[0]-- → mex = 1  
mex = 1 → remainder = 1 → count[1]-- → mex = 2  
mex = 2 → remainder = 0 → count[0]-- → mex = 3  
mex = 3 → remainder = 1 → count[1]-- → mex = 4  
mex = 4 → remainder = 0 → count[0] = 0 → return 4
```

**Output:**
```python
4
```

### ⏱️ Complexity Analysis

- **Time Complexity:**	`O(n + M)` → one pass to count + up to M iterations until the MEX is found

- **Space Complexity:**	`O(value)` → remainder counter of size `value`

### 🏁 Summary

✅ Reduce problem to modular equivalence classes
✅ Greedily construct smallest missing integer using counts
✅ Efficient, elegant O(n) solution with modulo arithmetic