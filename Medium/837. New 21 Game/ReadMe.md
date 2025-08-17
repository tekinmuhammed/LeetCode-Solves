# 🎲 LeetCode 837 - New 21 Game

**Difficulty:** Medium  
**Problem Link:** [LeetCode 368](https://leetcode.com/problems/new-21-game/description/)

---

## 🧩 Problem Description

Alice bir oyun oynuyor:

- Başlangıçta **0 puanı** var.

- Her turda **[1, maxPts]** arasında rastgele bir sayı çekiyor.

- Eğer toplam puanı **k veya daha fazlaysa**, oyunu durduruyor.

- Alice’in puanı **n veya daha az** olursa kazanıyor.

Görev: Alice’in kazanma olasılığını döndürmek.

## 💡 Intuition

Bu problem, klasik bir **olasılık + dinamik programlama** sorusudur.

- Alice’in puanı **k’den küçük** olduğu sürece kart çekmeye devam ediyor.

- Eğer toplam **k veya daha fazla** ise oyun bitiyor.

- Her skor için kazanma olasılığını **önceki skorların ortalaması** belirliyor.

Yani, bu bir **sliding window DP** problemine dönüşüyor.

### 🚀 Approach

1. **Özel durumlar:**

- Eğer `k == 0` → Alice hiç oynamıyor, otomatik kazanır (`1.0`).

- Eğer `n >= k + maxPts` → Alice’in kaybetme şansı yok, yine `1.0`.

2. **DP tanımı:**

- `dp[i]` = Alice’in **i puanla başladığında** kazanma olasılığı.

- Başlangıç: `dp[0] = 1.0`

3. **Sliding window mantığı:**

- `dp[i] = window_sum / maxPts`

- Eğer `i < k`, Alice hala oynayabilir → `window_sum += dp[i]`

- Eğer `i >= k`, oyun durur → `result += dp[i]`

4. **Window güncelleme:**

- Her adımda pencereyi kaydırmak için `window_sum -= dp[i - maxPts]` yapılır.

### 🧮 Example
```python
Input: n = 10, k = 1, maxPts = 10
Output: 1.0
Explanation:
Alice sadece 1 kart çekiyor.
Kart [1,10] aralığında olacağı için toplam puan ≤ 10 → %100 kazanır.
```

### 🕵️ Complexity

- **Time Complexity:** `O(n)` – her puan için hesaplama yapıyoruz.

- **Space Complexity:** `O(n)` – DP tablosu tutuyoruz.

### 🏷️ Tags

`dynamic-programming`, `probability`, `sliding-window`