# 🎨 LeetCode 1931 - Painting a Grid With Three Different Colors

**Difficulty:** Hard  
**Problem Link:** [LeetCode 1931](https://leetcode.com/problems/painting-a-grid-with-three-different-colors)

---

## 📘 Problem Description

You are given two integers `m` and `n`, representing the dimensions of a grid. You need to paint each cell with one of **three colors** (e.g., red = 0, green = 1, blue = 2) such that:
- No **two adjacent cells in the same row** have the same color.
- No **two adjacent cells in the same column** have the same color.

Return the number of **valid ways** to paint the grid, **modulo 10⁹ + 7**.

---

## 🧠 Intuition

Bu problemde klasik brute-force denemeleri çok pahalı olur çünkü `3^(m*n)` gibi büyük bir kombinasyon vardır.

Ancak dinamik programlama (DP) ve bit manipülasyonu gibi tekniklerle bu büyük uzayı daraltabiliriz:
- **Her kolonu bir durum (state) olarak ele alabiliriz.**
- Geçerli bir kolonu, o kolondaki `m` hücrenin birbirinden farklı komşulara sahip olması şartıyla oluştururuz.
- Daha sonra, her kolon durumunu, bir önceki kolonun durumlarıyla uyumlu olacak şekilde bağlarız (DP geçişi).

---

## 🔨 Approach

1. **Generate valid single-column states:**
   - `m` hücreli her kolonda bitişik renkler farklı olmalı.
   - Yani `product([0,1,2], repeat=m)` içinden sadece bitişik renkleri farklı olanları alırız.

2. **Precompute compatible columns:**
   - `col1` ve `col2` yan yana olabilir mi?
   - Şart: Tüm satırlarda `col1[i] != col2[i]`.

3. **Dynamic Programming:**
   - `dp[col]` = grid’in son kolonu `col` olduğunda oluşabilecek kombinasyon sayısı.
   - Her adımda `new_dp[col] = sum(dp[prev_col] for prev_col in neighbors[col])`.

---

### ⏱️ Complexity

- Time Complexity: `O(N * S^2)`

- - `S` = number of valid column states (exponential in `m` but manageable as m ≤ 5)

- - N = number of columns

- Space Complexity: `O(S)`

### 📌 Example

```python
Input: m = 1, n = 1
Output: 3

Input: m = 1, n = 2
Output: 6
```

### 🏷️ Tags
`dynamic-programming`, `bitmask`, `state-compression`, `graph`, `combinatorics`, `hard`