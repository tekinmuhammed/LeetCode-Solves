# 1356. Sort Integers by The Number of 1 Bits

**Difficulty:** Easy  
**Problem Link:** [LeetCode 1356](https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/description/)

---

## Problem

Given an integer array `arr`, sort the integers by:

1. The number of `1` bits in their binary representation.
2. If two numbers have the same number of `1` bits, sort them by their numerical value.

Return the sorted array.

---

## Example

Input

```
arr = [0,1,2,3,4,5,6,7,8]
```

Binary representations

```
0 → 0000 → 0 ones
1 → 0001 → 1 one
2 → 0010 → 1 one
3 → 0011 → 2 ones
4 → 0100 → 1 one
5 → 0101 → 2 ones
6 → 0110 → 2 ones
7 → 0111 → 3 ones
8 → 1000 → 1 one
```

Sorted output

```
[0,1,2,4,8,3,5,6,7]
```

---

# Approach

We sort the array using a **custom key function**.

Sorting rule:

```
key = (number_of_1_bits, number_itself)
```

This works because Python sorts tuples lexicographically:

- First by `number_of_1_bits`
- If equal, then by `number_itself`

---

# Your Solution

```python
class Solution(object):
    def sortByBits(self, arr):
        arr.sort(key=lambda x: (bin(x).count('1'), x))
        return arr
```

### How It Works

For each number `x`:

```
bin(x).count('1')
```

- `bin(x)` converts number to binary string
- `.count('1')` counts how many `1` bits exist

Example:

```
bin(5) → '0b101'
count('1') → 2
```

So key for `5` becomes:

```
(2, 5)
```

---

# Optimized Version (Python 3.10+)

```python
arr.sort(key=lambda x: (x.bit_count(), x))
```

`x.bit_count()` is faster because it works at the bit level instead of string conversion.

---

# Complexity Analysis

Let:

```
n = length of arr
m = number of bits per number (at most 32)
```

Time Complexity:

```
O(n log n)
```

Sorting dominates the complexity.

Counting bits:

- `bin(x).count('1')` → O(m)
- `x.bit_count()` → O(1) (hardware-level optimized)

Overall still:

```
O(n log n)
```

Space Complexity:

```
O(1)
```