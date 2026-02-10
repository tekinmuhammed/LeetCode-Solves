# 3719. Longest Balanced Subarray I

**Difficulty:** Medium  
**Problem Link:** [LeetCode 3719](https://leetcode.com/problems/longest-balanced-subarray-i/description/)

---

## Problem Özeti

Bir dizi `nums` veriliyor.  
Bir **subarray (alt dizi)** şu şartı sağlıyorsa *balanced* kabul ediliyor:

- Subarray içindeki **farklı (distinct)** çift sayı sayısı  
- Subarray içindeki **farklı (distinct)** tek sayı sayısına **eşit**

Amaç:
- Bu şartı sağlayan **en uzun subarray’in uzunluğunu** bulmak.

---

## Yaklaşım (Brute Force)

Bu soru **Longest Balanced Subarray I** olduğu için,
kısıtlar brute force çözümü mümkün kılıyor.

### Ana Fikir

- Her başlangıç indeksi `i` için:
  - `i`’den başlayarak sağa doğru genişleyen bir subarray kur
- Bu subarray için:
  - Çift sayıları bir `set` içinde tut
  - Tek sayıları ayrı bir `set` içinde tut
- Her adımda:
  - `len(evens) == len(odds)` ise
  - Subarray uzunluğunu güncelle

---

## Neden `set` Kullanıyoruz?

Problem **kaç tane farklı çift / tek sayı var** diye soruyor.

Örnek:
```python
[2, 2, 4, 4] → evens = {2, 4} → 2 adet
```

Yani:
- Tekrar eden sayılar **bir kez** sayılıyor
- Bu yüzden `set` şart

---

## Kod

```python
class Solution(object):
    def longestBalanced(self, nums):
        n = len(nums)
        ans = 0

        for i in range(n):
            evens = set()
            odds = set()

            for j in range(i, n):
                if nums[j] % 2 == 0:
                    evens.add(nums[j])
                else:
                    odds.add(nums[j])

                if len(evens) == len(odds):
                    ans = max(ans, j - i + 1)

        return ans
```

Örnek Üzerinden Anlayalım
```python
nums = [1, 2, 3, 4]
```
Alt dizilerden biri:
```python
[2, 3, 4]
evens = {2, 4} → 2
odds  = {3}    → 1 ❌
```
Ama:
```python
[1, 2, 3, 4]
evens = {2, 4} → 2
odds  = {1, 3} → 2 ✅
uzunluk = 4
```

### Zaman ve Alan Karmaşıklığı
- **Zaman**
- - Dış döngü: `O(n)`
- - İç döngü: `O(n)`
- - Toplam: **O(n²)**

- **Alan**
- - İki adet set:
- - - En kötü durumda `O(n)`
- - Toplam: **O(n)**