# 2147. Number of Ways to Divide a Long Corridor

**Difficulty:** Hard  
**Problem Link:** [LeetCode 2147](https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/description/)

## 🧩 Problem Summary
Elimizde yalnızca şu karakterlerden oluşan bir string var:

- `'S'` → Seat (koltuk)
- `'P'` → Plant (bitki)

Koridoru **parçalara ayırmak** istiyoruz.  
Her **parça tam olarak 2 adet `'S'`** içermelidir.

👉 Amaç: Koridoru bu kurala uygun şekilde **kaç farklı yolla bölebileceğimizi** bulmak.

Sonuç **mod 10⁹ + 7** ile döndürülmelidir.

---

## 🧠 Temel Fikir (DP + Memoization)

Bu problemde:
- Soldan sağa ilerlerken
- Hangi indekste olduğumuz
- Mevcut parçada kaç tane `'S'` gördüğümüz

bilgileriyle karar veriyoruz.

Bu yüzden **DP state** şu şekilde tanımlanır:

```python
count(index, seats)
```
- `index`: Koridorda bulunduğumuz pozisyon

- `seats`: Mevcut parçada kaç tane `'S'` var (0, 1, 2)

### 🎯 DP State Anlamı
`count(index, seats)`
- → `index`’ten sona kadar olan kısmı, mevcut parçada `seats` tane `'S'` varken
**geçerli şekilde bölmenin kaç yolu vardır?**

### 🧱 Base Case
Koridorun sonuna geldiysek:
```python
index == len(corridor)
```
- Eğer `seats == 2` → geçerli bir bölüm tamamlanmıştır → 1 yol

- Aksi halde → geçersiz → **0 yol**

### 🔀 Geçişler (Transitions)
**1️⃣ Eğer mevcut parçada 2 tane S varsa**
    Artık bu parça **tamamlanmıştır**.

**a) Sonraki karakter 'S' ise**
- Bu `'S'` yeni bir parçada olmalıdır

- Yeni parça 1 koltukla başlar
```python
count(index + 1, 1)
```

**b) Sonraki karakter `'P'` ise → iki seçenek var**
1. Bölümü kapatıp yeni parça başlat

2. Bölümü kapatmadan devam et
```python
count(index + 1, 0)  // yeni parça
+
count(index + 1, 2)  // devam
```

**2️⃣ Eğer mevcut parçada 2’den az S varsa**
    Bölümü kapatamayız, devam etmek zorundayız.

- Eğer karakter `'S'` → `seats + 1`

- Eğer karakter `'P'` → `seats` değişmez

## 🧮 Memoization (Cache)
    Aynı `(index, seats)` durumu tekrar hesaplanmasın diye:
```python
cache[index][seats]
```
kullanılır.
    Bu sayede zaman karmaşıklığı ciddi şekilde düşer.

### ⏱️ Time & Space Complexity
- **State sayısı:** `O(n * 3)`

- **Time Complexity:** `O(n)`

- **Space Complexity:** `O(n)`

### ✅ Your Code (Correct & Clean)
```python
class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 1_000_000_007

        # cache[index][seats]
        cache = [[-1] * 3 for _ in range(len(corridor))]

        def count(index, seats):
            if index == len(corridor):
                return 1 if seats == 2 else 0

            if cache[index][seats] != -1:
                return cache[index][seats]

            if seats == 2:
                if corridor[index] == "S":
                    result = count(index + 1, 1)
                else:
                    result = (count(index + 1, 0) + count(index + 1, 2)) % MOD
            else:
                if corridor[index] == "S":
                    result = count(index + 1, seats + 1)
                else:
                    result = count(index + 1, seats)

            cache[index][seats] = result
            return result

        return count(0, 0)
```

### 🏁 Final Notes
- DP state tanımı **çok yerinde**

- `seats == 2` durumunda yapılan dallanma problemi net çözüyor

- Memoization sayesinde **TLE riski yok**