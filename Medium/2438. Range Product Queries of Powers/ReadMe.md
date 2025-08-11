# LeetCode 2438 - Range Product Queries of Powers

## 📝 Problem Description

You are given:
- An integer `n`
- An array of queries `queries`, where each query is of the form `[left, right]`.

First, represent `n` as the **sum of distinct powers of two**.  
Then for each query `[left, right]`, compute the **product** of the powers in the range from `left` to `right` (inclusive), and return the result modulo `10^9 + 7`.

---

## 💡 Example

### Example 1
**Input**
```python
n = 15
queries = [[0, 1], [2, 2], [0, 3]]
```

**Step-by-step**

- `n = 15` → Binary: `1111` → Powers: `[1, 2, 4, 8]`

- Query `[0, 1]`: `1 * 2 = 2`

- Query `[2, 2]`: `4`

- Query `[0, 3]`: `1 * 2 * 4 * 8 = 64`

**Output**
```python
[2, 4, 64]
```

### 📊 Complexity

- **Time Complexity:**

- - Extracting powers: `O(log n)`

- - Each query: `O(r - l + 1)`

- - Total worst case: `O(log n + Q * log n)`

- **Space Complexity:** `O(log n)`

- - We store the powers of two that make up `n`.

### ✅ Key Points

- We use bitwise operations to extract powers of two from `n`.

- The modulo operation `10^9 + 7` prevents integer overflow.

- Queries are processed by multiplying powers in the specified index range.