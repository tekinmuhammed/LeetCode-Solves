# 3432. Count Partitions with Even Sum Difference — Explanation & Analysis

**Difficulty:** Easy
**Problem Link:** [LeetCode 3432](https://leetcode.com/problems/count-partitions-with-even-sum-difference/description/)  

## 🧩 Problem Summary
Bir dizi `nums` veriliyor ve bizden diziyi iki parçaya bölebileceğimiz **geçerli bölme sayısını** bulmamız isteniyor.

Bölme noktası `i` şu anlama gelir:

- Sol parça: `nums[0 : i]`
- Sağ parça: `nums[i : n]`

Geçerli olması için şu koşul sağlanmalı:
```python
abs(sum(left) - sum(right)) % 2 == 0
```

Yani **iki parçanın toplamları arasındaki fark çift olmalıdır**.

---

## 💡 Key Insight

Toplam farkın çift olması şu anlama gelir:
```python
(sum(left) - sum(right)) % 2 == 0
```

Bu da mod 2 aritmetiğinde:
```python
sum(left) % 2 == sum(right) % 2
```

Ayrıca:
```python
sum(right) = totalSum - sum(left)
```

Bu yüzden:
```python
sum(left) % 2 == (totalSum - sum(left)) % 2
```

Mod 2'de çıkarma ve toplama aynıdır, bu bize şunu verir:
```python
totalSum % 2 == 0
```

- ⛔ Eğer dizinin toplamı **tekse**, hiçbir bölme noktası şartı sağlayamaz.

- ✅ Eğer toplam **çiftse**, tüm bölme noktaları geçerlidir:

- Toplam `n` eleman varsa, bölme noktaları: `1` ile `n-1`
- Yani toplam **n - 1** geçerli bölme vardır.

---

## ✔ Final Formula
```python
totalSum % 2 == 0 → answer = n - 1
totalSum % 2 == 1 → answer = 0
```

Senin kodun tam olarak bunu yapıyor ve **doğru + optimal**.

---

## ⏱ Complexity
- **Zaman:** `O(n)`
- **Bellek:** `O(1)`

---

## ✅ Code (Your Solution)

```python
class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        return len(nums) - 1 if totalSum % 2 == 0 else 0
```

### 🧠 Why This Works

Toplamın parity’si (çift/tek olması) bir diziyi böldüğümüzde iki parçanın parity’sine de doğrudan etki eder.

Bu nedenle tek yapılması gereken dizinin toplamını kontrol etmektir.