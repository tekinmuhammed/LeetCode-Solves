# 3000. Maximum Area of Longest Diagonal Rectangle  

**Difficulty:** Easy  
**Link:** [LeetCode 3000](https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/)  

---

## Problem Description  

You are given a list of rectangles, where each rectangle is represented by its **length** and **width**.  

- The **diagonal length** of a rectangle with sides `l` and `w` is:  

\[
\text{diagonal} = \sqrt{l^2 + w^2}
\]

- Among all rectangles, find the one with the **longest diagonal**.  
- If multiple rectangles have the same diagonal length, return the one with the **largest area**.  

---

## Example  

### Example 1  
**Input:**  
```python
dimensions = [[9,3],[8,6]]
```

### Output:
```python
48
```

### Explanation:

- Rectangle (9,3) → diagonal = √(81 + 9) = √90 ≈ 9.49, area = 27

- Rectangle (8,6) → diagonal = √(64 + 36) = √100 = 10, area = 48

- The second rectangle has the longer diagonal → return 48.

###  Example 2
**Input:**
```python
dimensions = [[3,4],[4,3]]
```
**Output:**
```python
12
```

### Explanation:

- Both have diagonal = √25 = 5

- Both have area = 12 → return `12`.

### Constraints

- `1 <= dimensions.length <= 100`

- `1 <= l, w <= 100`

### Approach
**Key Ideas:**

1. For each rectangle `(l, w)` compute:

- - `diag = sqrt(l² + w²)`

- - `area = l * w`

2. Keep track of:

- - the maximum diagonal length so far

- - the area of the rectangle corresponding to this maximum diagonal

3. If a new rectangle has a **longer diagonal**, update both values.

4. If a new rectangle has the **same diagonal**, keep the maximum area.

### Time and Space Complexity

- **Time Complexity:** `O(n)` — iterate once over all rectangles.

- **Space Complexity:** `O(1)` — constant extra space used.

### Tags
`Geometry`, `Math`, `Array`

### Notes

- Instead of using `math.sqrt`, we could compare squared diagonals `(l² + w²)` directly to avoid floating-point precision issues.

- This is safe here since all values are integers and within constraints.