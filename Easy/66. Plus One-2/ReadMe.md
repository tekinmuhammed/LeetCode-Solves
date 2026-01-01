# 66. Plus One

**Difficulty:** Easy  
**Problem Link:** [LeetCode 66](https://leetcode.com/problems/plus-one)

---

## 🧩 Problem Özeti

Bir sayıyı **basamaklarına ayrılmış şekilde** temsil eden bir `digits` dizisi veriliyor.

Örnek:
- `[1,2,3]` → `123`
- `[9,9]` → `99`

🎯 Amaç:
> Bu sayıya **1 ekleyip**, sonucu yine **basamak dizisi** olarak döndürmek.

---

## 🧠 Temel Mantık

Bu problem aslında **elde (carry)** yönetimi problemidir.

- Sondan başla
- Eğer basamak `< 9` ise:
  - +1 yap ve **işi bitir**
- Eğer basamak `9` ise:
  - `0` yap ve sola doğru devam et
- Tüm basamaklar `9` ise:
  - Sonuç başına `1` eklenir

---

## ✅ Senin Çözümün

```python
class Solution(object):
    def plusOne(self, digits):
        n = len(digits)
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits
```

## 🔍 Adım Adım Açıklama
### 1️⃣ Sondan Başa Doğru Dolaşma
```python
for i in range(n - 1, -1, -1):
```
- En sağ basamaktan başlanır
- Elde ihtimali burada ortaya çıkar

### 2️⃣ Basamak 9’dan Küçükse
```python
if digits[i] < 9:
    digits[i] += 1
    return digits
```
✔️ Elde yok
✔️ İşlem biter
✔️ Direkt sonuç döner

### 3️⃣ Basamak 9 ise
```python
digits[i] = 0
```
- 9 + 1 = 10
- 0 yazılır
- Elde bir sonraki basamağa aktarılır

### 4️⃣ Tüm Basamaklar 9 ise
```python
return [1] + digits
```
📌 Örnek:
- `[9,9,9]`
- Döngü sonrası → `[0,0,0]`
- Başına `1` eklenir → `[1,0,0,0]`

### 🧪 Örnek Çalışmalar
| Girdi       | Çıktı       |
| ----------- | ----------- |
| `[1,2,3]`   | `[1,2,4]`   |
| `[4,3,2,1]` | `[4,3,2,2]` |
| `[9]`       | `[1,0]`     |
| `[9,9]`     | `[1,0,0]`   |

### ⏱️ Karmaşıklık Analizi
- **🧮 Zaman**
- - En kötü durumda tüm diziyi gezer
    👉 **O(n)**

- **🧠 Alan**
- - Yerinde güncelleme
- - Sadece özel durumda yeni liste oluşturulur
    👉 **O(1)** (çıktı hariç)