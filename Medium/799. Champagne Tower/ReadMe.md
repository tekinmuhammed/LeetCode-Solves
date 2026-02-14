# Champagne Tower

**Difficulty:** Medium  
**Problem Link:** [LeetCode 799](https://leetcode.com/problems/champagne-tower/description/)

---

## Problem Özeti

Bir kule düşün:

- 0. satır → 1 bardak
- 1. satır → 2 bardak
- 2. satır → 3 bardak
- ...
- r. satır → r+1 bardak

Her bardak en fazla **1 birim** şampanya alabilir.

Eğer bir bardak 1’i aşarsa:

- Fazlalığın yarısı sol alt bardağa
- Diğer yarısı sağ alt bardağa akar.

Amaç:

Belirli bir satır ve bardakta
ne kadar şampanya olduğunu bulmak.

---

# Ana Fikir

Bu tamamen bir **simülasyon** problemidir.

Her bardak için:

overflow = (mevcut_miktar - 1) / 2

Eğer overflow > 0 ise:

- A[r+1][c]     += overflow
- A[r+1][c + 1] += overflow

Sonuçta:

İstenen bardaktaki miktarı alırız,
ama maksimum 1 olabilir:

min(1, value)

---

# Kod

```python
class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        A = [[0] * k for k in xrange(1, 102)]
        A[0][0] = poured

        for r in xrange(query_row + 1):
            for c in xrange(r + 1):
                q = (A[r][c] - 1.0) / 2.0
                if q > 0:
                    A[r + 1][c] += q
                    A[r + 1][c + 1] += q

        return min(1, A[query_row][query_glass])
```

### Neden 102 Satır?
Problem kısıtına göre:
```python
query_row ≤ 100
```
Bu yüzden güvenli olmak için 101–102 satır oluşturulmuş.

### Örnek
```python
poured = 2

0. satır:
[2]

Overflow = (2 - 1)/2 = 0.5

1. satır:
[0.5, 0.5]

Hiçbiri 1’i aşmadığı için aşağı akış durur.
```

### Zaman Karmaşıklığı
- **En fazla:**
- - query_row ≈ 100
- **İç içe döngü:**
- - 1 + 2 + 3 + ... + 100
- - O(100²) → sabit
- **Yani pratikte `O(1)`**

### Alan Karmaşıklığı
- 2D array:
- - Yaklaşık 100² → sabit