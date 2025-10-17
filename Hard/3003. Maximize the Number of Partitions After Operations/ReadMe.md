# 🧩 3003. Maximize the Number of Partitions After Operations

**Difficulty:** Hard  
**Problem Link:** [LeetCode 3003](https://leetcode.com/problems/maximize-the-number-of-partitions-after-operations/description/)


## 💡 Problem Description
You are given a string `s` and an integer `k`.  
Your task is to **split the string** into the maximum number of partitions such that:
- Each partition contains **at most `k` distinct characters**.
- You can **change at most one character** in the entire string.

Return the **maximum number of partitions** you can achieve.

---

## 🧠 Approach

This is a **Dynamic Programming + Bitmasking** problem.

We simulate the process of traversing the string and deciding how to form valid partitions under the distinct-character limit.  
At each position, we can choose whether to:
1. Keep the character as is.
2. Change it to any other character (only once allowed).

---

### 🔹 Key Idea
We maintain a **bitmask** to represent which characters are present in the current partition.  
Each bit from 0–25 corresponds to letters `'a'`–`'z'`.

If the bitmask exceeds `k` distinct bits, we must **start a new partition**.

We define a recursive DP function with memoization:

```python
dp(i, can_change, mask)
```

| Parameter | Meaning |
|------------|----------|
| `i` | Current index in the string |
| `can_change` | Boolean — whether we still have the right to change one character |
| `mask` | Bitmask representing the unique characters in the current partition |

---

### 🔹 Recurrence

At position `i`, we have two options:

1. **Keep the current character**  
   - Compute new mask `mask | (1 << (ord(s[i]) - ord('a')))`
   - If bit count exceeds `k`, start a new partition.
   - Otherwise, continue the current one.

2. **Change the current character** (only if `can_change == True`)  
   - Try replacing it with all 26 possible letters.
   - For each new character, recompute mask and apply same logic.
   - Mark `can_change = False` afterward.

---

### 🔹 Base Case
If `i == len(s)`, there are no more characters — return 0 (no new partitions).

### 🔹 Final Answer
The recursion counts *splits* between partitions,  
so we add `+1` at the end to count the final partition.

---

## 🧩 Code Implementation

```python
import functools

class Solution:
    """
    3003. Maximize the Number of Partitions After Operations
    """
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        n = len(s)

        @functools.lru_cache(None)
        def dp(i: int, can_change: bool, mask: int) -> int:
            if i == n:
                return 0

            bit_cur_char = 1 << (ord(s[i]) - ord('a'))
            res = 0

            # --- Option A: Keep current character ---
            new_mask = mask | bit_cur_char
            if new_mask.bit_count() > k:
                res = 1 + dp(i + 1, can_change, bit_cur_char)
            else:
                res = dp(i + 1, can_change, new_mask)

            # --- Option B: Change character (if available) ---
            if can_change:
                for j in range(26):
                    bit_brute_char = 1 << j
                    new_mask_changed = mask | bit_brute_char

                    if new_mask_changed.bit_count() > k:
                        res = max(res, 1 + dp(i + 1, False, bit_brute_char))
                    else:
                        res = max(res, dp(i + 1, False, new_mask_changed))

            return res

        return dp(0, True, 0) + 1
```

### 🧪 Example
**Input:**
```python
s = "accca"
k = 2
```

### Explanation:

- Without any change: `"ac" | "cc" | "a"` → 3 partitions

- If we change the second `'c'` → `'b'`, `"ab" | "cc" | "a"` → still 3

- If we change one `'c'` → `'a'`, we can form `"aa" | "cca"` → 2
✅ Best result = **3 partitions**

## Output:
```python
3
```

### ⏱️ Complexity Analysis

- **Time Complexity:**	`O(26 * n * 2 * 2^k)` (since each step explores up to 26 replacements)
- **Space Complexity:**	`O(n * 2 * 2^k)` due to memoization

### 🏁 Summary

- ✅ Uses DP + bitmask to handle distinct character constraint
- ✅ Smart memoization avoids redundant recomputation
- ✅ Carefully considers one-time modification option
- ✅ Produces optimal partition count efficiently

## Tags: 
`Dynamic-Programming`, `Bitmask`, `Recursion`, `Memoization`, `String-Processing`