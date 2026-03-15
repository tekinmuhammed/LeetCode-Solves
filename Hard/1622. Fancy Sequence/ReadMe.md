# 1622. Fancy Sequence 

**Difficulty:** Hard   
**Problem Link:** [LeetCode 1622](https://leetcode.com/problems/fancy-sequence/description/)

---

## Problem Description 

Implement the `Fancy` class:
- `Fancy()`: Initializes the object with an empty sequence.
- `append(val)`: Appends an integer `val` to the end of the sequence.
- `addAll(inc)`: Increments all existing values in the sequence by an integer `inc`.
- `multAll(m)`: Multiplies all existing values in the sequence by an integer `m`.
- `getIndex(idx)`: Gets the current value at index `idx` (0-indexed) modulo $10^9 + 7$. If the index is greater or equal to the length of the sequence, return `-1`.

---

## Approach: Mathematical Transformation (Lazy Updates) 

Updating every element in a list during `addAll` or `multAll` would lead to $O(N)$ time complexity per operation, which is too slow ($O(Q \times N)$ total). Instead, we use a **linear transformation** approach: $y = (a \cdot x) + b$.

### Key Ideas: 
1.  **Global Trackers:** We maintain two variables, `mul` ($a$) and `add` ($b$), which represent the cumulative transformations applied to the sequence.
2.  **Reverse Engineering on Append:** When a new value $v$ is appended, we don't store $v$ directly. Instead, we store a value $x$ such that when the current $a$ and $b$ are applied, it results in $v$:
    $$v \equiv (a \cdot x + b) \pmod M$$
    Solving for $x$:
    $$x \equiv (v - b) \cdot a^{-1} \pmod M$$
3.  **Modular Inverse:** To calculate $a^{-1} \pmod M$, we use **Fermat's Little Theorem** because the modulo $10^9 + 7$ is a prime number:
    $$a^{M-2} \equiv a^{-1} \pmod M$$
4.  **Transformation Updates:**
    - `addAll(inc)`: Only updates $b$: $b = (b + inc) \pmod M$.
    - `multAll(m)`: Updates both $a$ and $b$: $a = (a \cdot m) \pmod M$ and $b = (b \cdot m) \pmod M$.



---

## Code 

```python
class Fancy(object):

    def __init__(self):
        self.MOD = 10**9 + 7
        self.arr = []
        self.mul = 1
        self.add = 0

    def append(self, val):
        # Calculate modular inverse of current global multiplier
        inv = pow(self.mul, self.MOD - 2, self.MOD)
        # Store value in a way that current (a*x + b) results in 'val'
        stored = (val - self.add) % self.MOD
        stored = (stored * inv) % self.MOD
        self.arr.append(stored)

    def addAll(self, inc):
        # Update global addition constant
        self.add = (self.add + inc) % self.MOD

    def multAll(self, m):
        # Update both global multiplier and addition constant
        self.mul = (self.mul * m) % self.MOD
        self.add = (self.add * m) % self.MOD

    def getIndex(self, idx):
        if idx >= len(self.arr):
            return -1
        # Apply current cumulative linear transformation to the stored value
        return (self.arr[idx] * self.mul + self.add) % self.MOD
```

---

## Complexity Analysis 

* **Time Complexity:** 
    - `append`: $O(\log M)$ due to the `pow()` function for modular inverse.
    - `addAll`: $O(1)$.
    - `multAll`: $O(1)$.
    - `getIndex`: $O(1)$.
* **Space Complexity:** $O(N)$
    - We store each element of the sequence exactly once in the list `arr`.

---

## Tags 
`Math`, `Design`, `Modular-Arithmetic`, `Fermat's-Little-Theorem`, `Data-Structures`