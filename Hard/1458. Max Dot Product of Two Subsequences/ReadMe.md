# 1458. Max Dot Product of Two Subsequences

**Difficulty:** Hard  
**Problem Link:** [LeetCode 1458](https://leetcode.com/problems/max-dot-product-of-two-subsequences/description/)

---

## 🧩 Problem Özeti

İki tam sayı dizisi veriliyor:  
- `nums1`
- `nums2`

Bu dizilerden **boş olmayan** iki subsequence seçiyoruz (sıra korunur).

🎯 Amaç:
> Seçilen iki subsequence’in **dot product**’ını maksimum yapmak.

**Dot product**:
\[
(a_1, a_2, ..., a_k) \cdot (b_1, b_2, ..., b_k)
= \sum_{i=1}^{k} a_i \times b_i
\]

---

## ⚠️ Neden Bu Problem Zor?

- Sayılar **negatif** olabilir
- Subsequence **boş olamaz**
- Klasik LCS benzeri DP ama:
  - “Hiçbir şey seçmemek” **yasak**
  - Bu yüzden başlangıç değerleri çok kritik

---

## 🧠 DP Fikri

### Durum Tanımı

```python
dp[i][j] =
nums1[0..i-1] ve nums2[0..j-1] kullanılarak
elde edilebilecek maksimum dot product
```
**📌 En az bir eşleşme içeren** sonuç tutulur.

### 🔁 Geçişler
`nums1[i-1]` ve `nums2[j-1]` için:
```python
product = nums1[i - 1] * nums2[j - 1]

dp[i][j] = max(
    product,                    # yeni bir subsequence başlat
    dp[i - 1][j - 1] + product, # mevcut subsequence'e ekle
    dp[i - 1][j],               # nums1'den eleman atla
    dp[i][j - 1]                # nums2'den eleman atla
)
```

### 🔑 Kritik Nokta
- `product` tek başına bir adaydır
    → Bu sayede **negatif sonuçlar bile doğru şekilde başlatılır**

### 🧮 Başlangıç (Initialization)
```python
dp = [[-10**18] * (m + 1) for _ in range(n + 1)]
```
✔️ Böylece:
- “Boş subsequence” kazara seçilmez
- En az bir çarpım zorunlu olur

### ✅ Senin Kodun
```python
class Solution(object):
    def maxDotProduct(self, nums1, nums2):
        n, m = len(nums1), len(nums2)

        # dp[i][j]: nums1[0..i-1] ve nums2[0..j-1] kullanılarak
        # elde edilebilecek maksimum dot product
        dp = [[-10**18] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                product = nums1[i - 1] * nums2[j - 1]

                dp[i][j] = max(
                    product,                       # sadece bu çifti başlat
                    dp[i - 1][j - 1] + product,    # önceki subsequence'e ekle
                    dp[i - 1][j],                  # nums1'den atla
                    dp[i][j - 1]                   # nums2'den atla
                )

        return dp[n][m]
```

### 🧪 Örnek
```python
nums1 = [2, 1, -2, 5]
nums2 = [3, 0, -6]
```
En iyi seçim:
- `[2, -2]` ve `[3, -6]`
Dot product:
```python
2*3 + (-2)*(-6) = 6 + 12 = 18
```

### ⏱️ Karmaşıklık
- **Zaman:** `O(n * m)`
- **Alan:** `O(n * m)`