# LeetCode 869 - Reordered Power of 2

## 📝 Problem Description

You are given an integer `n`.  
You need to determine if the digits of `n` can be **rearranged** to form a number that is a **power of two**.

---

## 💡 Example

### Example 1
**Input**
```python
n = 1
```

**Output**
```python
True
```

**Explanation:** 1 is 2^0.

### Example 2
**Input**
```python
n = 10
```

**Output**
```python
False
```

**Explanation:** No rearrangement of 10 is a power of two.

### Example 3
**Input**
```python
n = 46
```

**Output**
```python
True
```

**Explanation:** Rearranging 46 → 64 which is 2^6.

### 📊 Complexity

- **Time Complexity:** `O(1)`
We precompute digit patterns for powers of two up to `2^30` (since `n` ≤ 10^9).
Sorting digits of `n` and comparing with the set is constant time for fixed digit length.

- **Space Complexity:** `O(1)`
The set of precomputed digit patterns is constant in size.

### ✅ Key Points

- We precompute all possible digit combinations of powers of two within the integer range.

- Sorting digits allows for easy comparison regardless of digit order.

- Works because permutation check reduces to checking if sorted digit strings match.