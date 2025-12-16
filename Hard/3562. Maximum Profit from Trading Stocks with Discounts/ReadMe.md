# 3562. Maximum Profit from Trading Stocks with Discounts — Explanation & Analysis

**Difficulty:** Hard  
**Link:** [LeetCode 3562](https://leetcode.com/problems/maximum-profit-from-trading-stocks-with-discounts/description/)

## 🧩 Problem Summary
Elimizde:
- `n` adet hisse (node)
- Her hisse için:
  - `present[i]`: bugünkü fiyat
  - `future[i]`: gelecekteki satış fiyatı
- Bir **hiyerarşi ağacı** (`hierarchy`):  
  - Bir hisse alınmadan, onun altındaki hisseler **indirimli alınamaz**
- Toplam bir **budget**

🎯 Amaç:  
**Bütçeyi aşmadan maksimum kârı elde etmek**

---

## 🧠 Ana Fikir

Bu problem:
- **Ağaç (tree) DP**
- **Knapsack (bütçe) DP**
- **İndirim koşullu satın alma**

kombinasyonudur.

Bir hisse için:
- **Normal satın alma** → `present[u]`
- **İndirimli satın alma** → `present[u] // 2`
- Satıştan elde edilen kâr:
  ```text
  future[u] - satın alma maliyeti
  ```

### 📌 Kritik kural:

> Bir node indirimli alınacaksa, parent mutlaka alınmış olmalı

### 🌳 Ağaç Yapısının Kurulması
```python
g = [[] for _ in range(n)]
for e in hierarchy:
    g[e[0] - 1].append(e[1] - 1)
```
- Root: `0`

- Directed tree

- DFS ile alttan üste DP yapılır

### 🔁 DFS + DP Yaklaşımı
Her node `u` için DFS şunları döndürür:
```python
dp0[b] → parent alınmadıysa, b bütçeyle max kâr
dp1[b] → parent alındıysa, b bütçeyle max kâr
uSize → bu alt ağacın maksimum maliyet sınırı
```

### 📦 DP State Açıklaması
`dp0`
- Parent alınmadı
- Bu node indirimli alınamaz

`dp1`
- Parent alındı
- Bu node indirimli alınabilir

### 👶 Çocuk Node'ların Birleştirilmesi (Knapsack)
```python
for v in g[u]:
    child_dp0, child_dp1, vSize = dfs(v)
```

**Alt düğümler:**

- Klasik **0/1 knapsack merge**

- Bütçe ters yönde dönülür

- Alt ağaç kârları birleştirilir
```python
subProfit0 → indirim yok
subProfit1 → indirim var
```

### 💰 Mevcut Node'u Satın Alma Kararı
```python
if i >= dCost:
    dp1[i] = max(
        subProfit0[i],
        subProfit1[i - dCost] + future[u] - dCost
    )
```

**📌 Anlamı:**

- Eğer parent alındıysa

- İndirimli alım yapılabilir

- Net kâr eklenir
```python
if i >= cost:
    dp0[i] = max(
        subProfit0[i],
        subProfit1[i - cost] + future[u] - cost
    )
```
📌 Parent alınmadıysa:

- Sadece **normal fiyatla** alım mümkündür

### 🏁 Sonuç
```python
return dfs(0)[0][budget]
```
- Root’un parent’ı olmadığı için

- **dp0** kullanılır

- Tam bütçe ile maksimum kâr alınır

### ⏱️ Karmaşıklık Analizi
- **Zaman:** `O(n * budget²)`

- **Alan:** `O(n * budget)`