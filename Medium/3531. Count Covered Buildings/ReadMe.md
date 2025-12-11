# 3531. Count Covered Buildings — Explanation & Analysis

**Difficulty:** Medium  
**Problem Link:** [LeetCode 3531](https://leetcode.com/problems/count-covered-buildings/description/)

## 🧩 Problem Summary
We are given **n** buildings placed at coordinates `(x, y)`.  
A building is considered **covered** if:

- Aynı satırda (x sabit):
  - Solunda bir bina var  
  - Sağında bir bina var  
- Aynı sütunda (y sabit):
  - Yukarısında bir bina var  
  - Aşağısında bir bina var  

Yani bina hem yatay hem dikey olarak **iki taraflı sıkışmış** olmalı.

Amaç: Bu şekilde **tamamen çevrelenmiş** kaç bina olduğunu bulmak.

---

## 💡 Key Insight
Her bina için aşağıdakileri bilmemiz gerekir:

- Aynı **row (x)** üzerindeki tüm binaların y-koordinatları  
- Aynı **column (y)** üzerindeki tüm binaların x-koordinatları  

Bu listeler sıralandığında:

- Solda bina olması için → row_list[0] < y  
- Sağda bina olması için → row_list[-1] > y  
- Yukarıda bina olması için → col_list[0] < x  
- Aşağıda bina olması için → col_list[-1] > x  

Dolayısıyla her bina için sadece listenin **ilk ve son** elemanına bakmak yeterli.

---

## 🛠️ Approach

### 1. Satır ve sütunlara göre gruplama  
```python
rows = defaultdict(list)
cols = defaultdict(list)
```

### 2. Her (x, y) noktasını uygun group'a ekleme
```python
rows[x].append(y)
cols[y].append(x)
```
### 3. Satır ve sütun değerlerini sıralama
```python
rows[r].sort()
cols[c].sort()
```

### 4. Her bina için:
- Satırda solda mı var?

- Satırda sağda mı var?

- Sütunda yukarıda mı var?

- Sütunda aşağıda mı var?

Tümü sağlanıyorsa → bina covered.

### ⏱️ Time Complexity
| İşlem    | Karmaşıklık                                  |
| -------- | -------------------------------------------- |
| Gruplama | O(n)                                         |
| Sıralama | Tüm satır ve sütunlar için toplam O(n log n) |
| Kontrol  | O(n)                                         |

- Sonuç: **O(n log n)**

### ✅ Your Code (Correct & Clean)
```python
class Solution(object):
    def countCoveredBuildings(self, n, buildings):
        from collections import defaultdict
        
        rows = defaultdict(list)
        cols = defaultdict(list)
        
        # row = x, col = y
        for x, y in buildings:
            rows[x].append(y)
            cols[y].append(x)
        
        # satır ve sütunlardaki değerleri sırala
        for r in rows:
            rows[r].sort()
        for c in cols:
            cols[c].sort()
        
        def has_left(row_list, y):
            return row_list[0] < y
        
        def has_right(row_list, y):
            return row_list[-1] > y
        
        def has_up(col_list, x):
            return col_list[0] < x
        
        def has_down(col_list, x):
            return col_list[-1] > x
        
        covered = 0
        
        for x, y in buildings:
            row_list = rows[x]
            col_list = cols[y]
            
            if (has_left(row_list, y) and
                has_right(row_list, y) and
                has_up(col_list, x) and
                has_down(col_list, x)):
                covered += 1
        
        return covered
```