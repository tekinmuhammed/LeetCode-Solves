# 1411. Number of Ways to Paint N × 3 Grid

**Difficulty:** Hard  
**Problem Link:** [LeetCode 1411](https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/description/)

---

## 🧩 Problem Özeti

Elimizde **N × 3** boyutunda bir grid var ve:

- Her hücre **3 farklı renkten** biriyle boyanacak
- **Yan yana (yatay veya dikey) iki hücre aynı renk olamaz**

🎯 Amaç:
> Bu kurallara uyarak grid’i boyamanın **toplam kaç farklı yolu** olduğunu bulmak  
> (Sonuç `10^9 + 7` modunda döndürülür)

---

## 💡 Temel Fikir (DP + Durum Sıkıştırma)

Her satırı **iki temel tipe** ayırabiliriz:

### 🔹 Type A (ABA tipi)
- 1. ve 3. sütun **aynı renk**
- Orta sütun **farklı**
- Örnek: `R G R`

👉 Bir satır için **6 farklı** ABA kombinasyonu vardır

---

### 🔹 Type B (ABC tipi)
- 3 sütunun **tamamı farklı**
- Örnek: `R G B`

👉 Bir satır için **6 farklı** ABC kombinasyonu vardır

---

## 🧠 DP Tanımı

- `typeA` → Şu ana kadar **ABA** tipiyle biten yolların sayısı  
- `typeB` → Şu ana kadar **ABC** tipiyle biten yolların sayısı  

### Başlangıç (1. satır)
```python
typeA = 6
typeB = 6
```

### 🔄 Geçiş Kuralları
Bir satırdan sonraki satıra geçerken:

**Yeni ABA (newA)**
- Önceki ABA → `3` farklı şekilde devam eder
- Önceki ABC → `2` farklı şekilde devam eder
```python
newA = typeA * 3 + typeB * 2
```

**Yeni ABC (newB)**
- Önceki ABA → `2` farklı şekilde
- Önceki ABC → `2` farklı şekilde
```python
newB = typeA * 2 + typeB * 2
```
> Tüm işlemler `MOD = 10^9 + 7` ile yapılır.

### ✅ Çözüm
```python
class Solution(object):
    def numOfWays(self, n):
        MOD = 10**9 + 7
        
        # For row 1
        typeA = 6  # ABA
        typeB = 6  # ABC
        
        for _ in range(2, n + 1):
            newA = (typeA * 3 + typeB * 2) % MOD
            newB = (typeA * 2 + typeB * 2) % MOD
            typeA, typeB = newA, newB
        
        return (typeA + typeB) % MOD
```

### 🧪 Küçük Örnek
**n = 1**
```python
typeA = 6
typeB = 6
Toplam = 12
```
**n = 2**
```python
newA = 6*3 + 6*2 = 30
newB = 6*2 + 6*2 = 24
Toplam = 54
```

### ⏱️ Karmaşıklık Analizi
- **🧮 Zaman**
- - Her satır için sabit işlem
    **👉 O(n)**

- **🧠 Alan**
- - Sadece birkaç değişken
    **👉 O(1)**