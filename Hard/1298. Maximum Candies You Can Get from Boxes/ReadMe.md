# 🍬 LeetCode 1298 - Maximum Candies You Can Get from Boxes

**Difficulty:** Hard  
**Problem Link:** [LeetCode 1298](https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes)

---

## 📘 Problem Description

Elimizde `n` adet kutu var. Her kutunun:
- Açık mı kapalı mı olduğu bilgisi (`status`)
- İçindeki şeker miktarı (`candies`)
- İçinden çıkan anahtarlar (`keys`)
- İçinden çıkan başka kutular (`containedBoxes`) bilgisi veriliyor.

Başlangıçta elimizde bazı kutular var (`initialBoxes`).  
Amacımız **olabildiğince çok kutu açarak maksimum şeker toplamaktır**.

Kurallar:
- Sadece açık olan kutuları açabiliriz.
- Kutulardan çıkan anahtarlarla yeni kutular açılabilir.
- Kutulardan başka kutular çıkabilir.

---

## ✅ Algorithm Explanation

Bu bir **BFS (Breadth-First Search)** benzeri problem.

### Adımlar:

1. `has_key` → elimizde olan anahtarları gösterir (başlangıçta `status` ile aynı).
2. `boxes` → elimizde fiziksel olarak bulunan kutular.
3. `queue` → açılabilir kutuların sırası.
4. Her kutu açıldığında:
   - Şeker alınır.
   - İçinden çıkan **anahtarlar** ve **kutular** eklenir.
   - Anahtarını bulduğumuz kutu önceden elimizde varsa, onu da açarız.

---

### 🧪 Örnek

```python
status = [1,0,1,0]
candies = [7,5,4,100]
keys = [[],[],[1],[]]
containedBoxes = [[1,2],[3],[],[]]
initialBoxes = [0]

Çözüm akışı:
- Kutular: [0]
- Açık: 0 → 7 şeker
- İçinden çıkan: [1,2]
- 2 zaten açık → aç → 4 şeker → anahtar [1]
- 1 kilitliydi ama artık açabiliriz → 5 şeker → içinden 3
- 3 kilitli ama artık açabiliriz → 100 şeker

Toplam: **7 + 4 + 5 + 100 = 116**
```

### ⏱️ Time & Space Complexity

- **Time Complexity:** `O(n + k)`
(`n` = kutu sayısı, `k` = toplam anahtar + iç kutu)

- **Space Complexity:** `O(n)`

### 🏷️ Tags

`bfs`, `graph`, `set`, `queue`, `greedy`