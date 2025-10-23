# 3461. Check If Digits Are Equal in String After Operations I

**Problem Link:** [LeetCode 3461](https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/description/)  
**Difficulty:** Easy

## 🧩 Problem Description

You are given a string `s` consisting only of digits (`0-9`).

At each step:
- Replace the string `s` with a new string where each digit `s[i]` becomes  
  `(int(s[i]) + int(s[i + 1])) % 10`,  
  for all `i` from `0` to `len(s) - 2`.

You repeat this operation until only **two digits remain**.

Your task is to determine **whether the final two digits are equal**.

Return:
- `True` if the final two digits are the same.
- `False` otherwise.

---

## 💡 Intuition

The operation reduces the string length by one in every iteration:
- Start with `n` digits,
- After 1 step → `n - 1` digits,
- Continue until only 2 digits remain.

At each step, every new digit is derived from the **sum of two adjacent digits modulo 10**.  
The process is **deterministic**, meaning that regardless of the input size, we always end up with exactly two digits — making the problem tractable even for longer strings.

The key idea:
- Continuously transform the string by summing adjacent digits mod 10.
- Stop when the string length is 2.
- Check if both digits are equal.

---

## ⚙️ Approach

1. Initialize `s` as the input string.
2. While the length of `s` is greater than 2:
   - Create a new list `new_s`.
   - For each index `i`, compute `(int(s[i]) + int(s[i + 1])) % 10`.
   - Append the result to `new_s`.
   - Update `s` with the joined string `"".join(new_s)`.
3. When only two digits remain, compare `s[0]` and `s[1]`.

---

## 💻 Code Implementation

```python
class Solution(object):
    def hasSameDigits(self, s):
        """
        :type s: str
        :rtype: bool
        """
        while len(s) > 2:
            new_s = []
            for i in range(len(s) - 1):
                new_s.append(str((int(s[i]) + int(s[i + 1])) % 10))
            s = "".join(new_s)
        
        return s[0] == s[1]
```

### 🧠 Example Walkthrough
**Example 1:**
```python
Input: s = "1234"
| Step  | s      | Explanation                        |
| ----- | ------ | ---------------------------------- |
| 0     | "1234" | Start                              |
| 1     | "357"  | (1+2)%10=3, (2+3)%10=5, (3+4)%10=7 |
| 2     | "82"   | (3+5)%10=8, (5+7)%10=2             |
| Final | "82"   | Two digits left → 8 ≠ 2 → False    |

✅ Output: False
```

**Example 2:**
```python
Input: s = "565"
| Step  | s     | Explanation                     |
| ----- | ----- | ------------------------------- |
| 0     | "565" | Start                           |
| 1     | "11"  | (5+6)%10=1, (6+5)%10=1          |
| Final | "11"  | Two digits left → 1 == 1 → True |

✅ Output: True
```

## ⏱️ Complexity Analysis

- **Time Complexity:**	`O(n²)`	Because each iteration reduces the string by 1, forming a total of n + (n−1) + (n−2) + ... = O(n²) digit additions.

- **Space Complexity:**	`O(n)`	For temporary storage in `new_s` during each iteration.

## ✅ Summary

- Each step sums adjacent digits modulo 10.

- The process continues until only 2 digits remain.

- Result is `True` if both digits are equal, otherwise `False`.

- Simple iterative simulation; easy to implement and reason about.

### 🧾 Key Takeaways

- The problem showcases iterative transformation and reduction.

- Perfect example of using modular arithmetic to constrain digit operations.

- Elegant and clean approach without requiring recursion or advanced data structures.

### Tags
`LeetCode-Easy`