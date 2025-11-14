# 🧮 LeetCode 2536 — Increment Submatrices by One

**Difficulty:** Medium  
**Problem Link:** [LeetCode 2536](https://leetcode.com/problems/increment-submatrices-by-one/description/)

## 📝 Problem Açıklaması
Size bir `n x n` matrisi ve çeşitli *sorgular* veriliyor.  
Her sorgu dört sayı içerir:
```python
[r1, c1, r2, c2]
```

Bu sorgu, şu alt-matris içindeki **tüm hücrelerin değerini 1 artır** anlamına gelir:

- Üst-sol köşe: `(r1, c1)`
- Alt-sağ köşe: `(r2, c2)`

Tüm sorguları uyguladıktan sonra oluşan matrisi döndürmelisiniz.

---

## 💡 Neden 2D Difference Array Kullanıyoruz?

Eğer her sorgu için doğrudan alt-matrisi gezip +1 eklersek:

- Her sorgu O(n²)
- Toplam: O(q * n²)

Bu **çok yavaş** olur.

Bunun yerine **2D difference array** (2D fark matrisi) kullanarak:

- Her sorgu O(1) güncellenir.
- En sonunda yalnızca tek bir 2D prefix sum işlemi yapılır.
- Toplam zaman: **O(n²)**

Bu yaklaşım, 1D prefix sum mantığının 2 boyutlu versiyonudur.

---

## ⚙️ Çözüm Mantığı

### ✔️ 1. Adım  
`diff` adında `(n+1) x (n+1)` boyutlu bir fark matrisi oluşturulur.

### ✔️ 2. Adım  
Her sorgu `[r1, c1, r2, c2]` için 2D difference güncellemeleri yapılır:
```python
diff[r1][c1] += 1
diff[r1][c2 + 1] -= 1
diff[r2 + 1][c1] -= 1
diff[r2 + 1][c2 + 1] += 1
```

Bu dört işlem, ilgili dikdörtgenin tamamına etkisi olan +1 artışını tanımlar.

### ✔️ 3. Adım  
Tüm farkları birleştirmek için **2D prefix sum** uygulanır:
```python
result[r][c] = diff[r][c]
+ result[r-1][c]
+ result[r][c-1]
- result[r-1][c-1]
```

Böylece tüm alt-matris artışları doğru şekilde dağıtılır.

---

## 🧱 Kodun Açıklamalı Hali

```python
class Solution(object):
    def rangeAddQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[List[int]]
        """

        # 2D difference matrix (n+1 x n+1)
        diff = [[0] * (n + 1) for _ in range(n + 1)]

        # Difference array updates for each query
        for r1, c1, r2, c2 in queries:
            diff[r1][c1] += 1
            diff[r1][c2 + 1] -= 1
            diff[r2 + 1][c1] -= 1
            diff[r2 + 1][c2 + 1] += 1

        # Build final matrix via 2D prefix sum
        result = [[0] * n for _ in range(n)]

        for r in range(n):
            for c in range(n):
                above = result[r - 1][c] if r > 0 else 0
                left  = result[r][c - 1] if c > 0 else 0
                diag  = result[r - 1][c - 1] if r > 0 and c > 0 else 0

                result[r][c] = diff[r][c] + above + left - diag

        return result
```

### ⏱️ Zaman ve Bellek Analizi
| Özellik                | Değer                                                         |
| ---------------------- | ------------------------------------------------------------- |
| **Zaman Karmaşıklığı** | O(n²)                                                         |
| **Bellek Kullanımı**   | O(n²)                                                         |
| **Neden?**             | 2D difference + prefix sum işlemi tüm matrisi bir kez dolaşır |

### 🧠 Özet
- 2D difference array sayesinde her sorgu O(1) yapılır.

- 2D prefix sum ile tüm etkiler yayılır.

- En verimli yaklaşım budur ve büyük n için şarttır.

- Çözüm hem temiz hem optimal.

