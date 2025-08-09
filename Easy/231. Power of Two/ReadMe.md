# LeetCode 231 - Power of Two

## 📝 Problem Description

Given an integer `n`, determine if it is a **power of two**.  
An integer `n` is a power of two if there exists an integer `x` such that:

`n == 2^x`

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

**Explanation:** 2^0 = 1

### Example 2
**Input**
```python
n = 16
```

**Output**
```python
True
```

**Explanation:** 2^4 = 16

###Example 3
**Input**
```python
n = 3
```

**Output**
```python
False
```

### 📊 Complexity

- **Time Complexity:** `O(1)`
Bitwise operations take constant time.

- **Space Complexity:** `O(1)`
No extra memory used.

### ✅ Key Points

- A number that is a power of two has exactly one bit set in binary representation.

- `(n & (n - 1)) == 0` checks if there is only one bit set.

- We ensure `n > 0` to exclude zero and negative numbers.