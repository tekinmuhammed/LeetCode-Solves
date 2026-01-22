## 3507. Minimum Pair Removal to Sort Array I

**Difficulty:** Easy  
**Problem Link:** [LeetCode 3507](https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/description/)

### Problem Özeti

Bir dizi `nums` veriliyor.  
Aşağıdaki işlemi istediğin kadar yapabilirsin:

- Yan yana duran iki elemanı seç
- Bu iki elemanı diziden sil
- Yerlerine **toplamlarını** tek bir eleman olarak koy

Amaç:
> Diziyi **non-decreasing (artan veya eşit)** hale getirmek için gereken **minimum işlem sayısını** bulmak.

---

### Yaklaşım (Greedy)

Temel fikir şu:

- Dizi sıralı değilken işlem yapmaya devam et
- Her adımda:
  - Yan yana duran çiftler arasından **toplamı en küçük olan çifti** seç
  - Bu çifti tek eleman (toplamları) ile değiştir
  - İşlem sayısını artır

Neden en küçük toplam?
- Küçük değerler dizinin başında kalırsa sıralamayı bozma ihtimali azalır
- Greedy olarak en güvenli hamle

---

### Yardımcı Fonksiyon

```python
def is_sorted(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False
    return True
Dizinin sıralı olup olmadığını kontrol eder.

Algoritma Adımları
ops = 0

Dizi sıralı değilken:

En küçük nums[i] + nums[i+1] toplamını bul

Bu ikiliyi diziden çıkar

Yerine toplamı ekle

ops += 1

Dizi sıralı hale gelince ops döndürülür

Python Kodu
python
Kodu kopyala
class Solution(object):
    def minimumPairRemoval(self, nums):
        ops = 0

        def is_sorted(arr):
            for i in range(1, len(arr)):
                if arr[i] < arr[i - 1]:
                    return False
            return True

        while not is_sorted(nums):
            min_sum = float('inf')
            idx = 0

            for i in range(len(nums) - 1):
                s = nums[i] + nums[i + 1]
                if s < min_sum:
                    min_sum = s
                    idx = i

            nums = nums[:idx] + [min_sum] + nums[idx + 2:]
            ops += 1

        return ops
Zaman ve Alan Karmaşıklığı
Zaman:

Her adımda O(n) tarama

En kötü durumda O(n) adım
→ O(n²)

Alan:

Yeni liste oluşturulduğu için O(n)

