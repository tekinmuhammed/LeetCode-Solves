# 717. 1-bit and 2-bit Characters — Explanation & Analysis

**Difficulty:** Easy  
**Link:** [LeetCode 717](https://leetcode.com/problems/1-bit-and-2-bit-characters/description/)

## ✔️ Problem Summary
You are given a binary array `bits` representing characters:

- **0** → one-bit character  
- **10** or **11** → two-bit character

You must determine whether the **last character** is a **1-bit character**.

---

## 💡 Key Insight
Traverse the array from left to right:

- If you encounter a `1`, it must form a **2-bit character**, so jump ahead by 2.
- If you encounter a `0`, it is a **1-bit character**, so move ahead by 1.
- Stop early at `n − 1` because the last bit is evaluated separately.

Finally:

- If your pointer stops **exactly at the last index**, then the last character is a 1-bit character.
- Otherwise, it was paired in a 2-bit character.

---

## ⏱️ Time & Space Complexity
| Metric | Complexity |
|--------|------------|
| **Time** | `O(n)` |
| **Space** | `O(1)` |

Very efficient: single pass, constant memory.

---

## 🧠 Example
`bits = [1, 0, 0]`

- index 0: `1` → skip 2 → index = 2  
- index 2 is the last index → **True**

`bits = [1, 1, 1, 0]`

- index 0: `1` → skip to 2  
- index 2: `1` → skip to 4  
- passed the last bit → **False**

---

## ✅ Code Implementation (Your Code)
```python
class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0
        n = len(bits)

        while i < n - 1:  # last bit is checked separately
            if bits[i] == 1:
                i += 2   # 2-bit character
            else:
                i += 1   # 1-bit character

        return i == n - 1
```

### 📌 Why This Solution Works Perfectly

- Correctly models the 1-bit & 2-bit rules

- Avoids unnecessary list slicing or recursion

- Ensures the final decision is based on pointer alignment with the last index