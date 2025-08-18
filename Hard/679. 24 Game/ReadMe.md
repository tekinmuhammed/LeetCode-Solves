# 🎲 LeetCode 679 - 24 Game

**Difficulty:** Hard 
**Problem Link:** [LeetCode 679](https://leetcode.com/problems/24-game/description/)

---

## 🧩 Problem Description

You are given an integer array `cards` of length **4**, where each value is between `1` and `9`.

Return **true** if you can get the number `24` using the four numbers in the array, and the operations:

- Addition `+`

- Subtraction `-`

- Multiplication `*`

- Division `/`

You may use each number **exactly once**.

## 💡 Intuition

Bu problem aslında **rekürsif arama (DFS + backtracking)** yaklaşımıyla çözülür:

- Elimizdeki sayıların her ikili kombinasyonu için tüm aritmetik işlemleri deneriz.

- Ortaya çıkan yeni sayıyı geri kalan sayılarla birleştirip tekrar aynı süreci uygularız.

- Sonunda tek bir sayı kalır ve eğer bu sayı `24`’e yakınsa (`|x - 24| < 0.001` toleransıyla), çözüm bulunmuş olur.


### 🚀 Approach

1. **Rekürsif DFS:**

- Eğer elimizde sadece **1 sayı kaldıysa**, bu sayının `24` olup olmadığını kontrol et.

- Aksi halde, her ikili sayıyı seç ve dört işlem sonuçlarını hesapla.

2. **Olası işlemler:**

- `a + b`

- `a - b`, `b - a`

- `a * b`

- `a / b` (sıfıra bölme hariç)

- `b / a` (sıfıra bölme hariç)

3. **Backtracking:**

- Yeni oluşturulan sayıyı listenin geri kalanıyla birleştir.

- DFS çağrısı yap.

- Eğer herhangi bir yolda `24` elde edilirse, direkt `True` döndür.

### 🧪 Example
```python
Input: [4, 1, 8, 7]
Output: true
Explanation: (8 - 4) * (7 - 1) = 24
```

```python
Input: [1, 2, 1, 2]
Output: false
```

### 🕵️ Complexity

- **Time Complexity:** `O(n!)`

- - Çünkü her adımda ikili seçip tüm işlemleri deniyoruz (küçük sabit n = 4 olduğundan pratikte çalışıyor).

- **Space Complexity:** `O(n)`

- - Rekürsif çağrılar derinliği için.

### 🏷️ Tags

`dfs`, `backtracking`, `math`, `recursion`, `search`, `hard`