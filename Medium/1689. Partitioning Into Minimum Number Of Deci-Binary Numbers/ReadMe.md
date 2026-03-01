# 1689. Partitioning Into Minimum Number Of Deci-Binary Numbers

**Difficulty:** Medium  
**Problem Link:** [LeetCode 1689](https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/description/)

---

# 1689. Partitioning Into Minimum Number Of Deci-Binary Numbers

## Problem Özeti

Bir **decimal string** `n` veriliyor (örn: `"82734"`).

Bir **deci-binary number**:
- Sadece `0` ve `1` rakamlarından oluşur
- Decimal (10’luk) sistemde değerlendirilir

Amaç:

`n` sayısını, **toplamları `n` olacak şekilde**, en az kaç tane deci-binary sayıya bölebileceğimizi bulmak.

---

## Temel Gözlem (Ana Fikir)

Her basamak **bağımsızdır**.

Bir basamakta örneğin:

```
n[i] = 7
```

Bu basamakta toplamda **7 adet `1`** üretmek zorundayız.

Çünkü:
- Her deci-binary sayı bir basamağa **en fazla 1** katkı yapabilir (`0` veya `1`)
- O basamakta değer `7` ise → **en az 7 sayı gerekir**

Bu durum tüm basamaklar için geçerli olduğundan:

👉 **Gerekli minimum deci-binary sayısı = n içindeki en büyük rakam**

---

## Neden Bu Yeterli?

Örnek:

```
n = "82734"
```

Basamaklar:
```
8, 2, 7, 3, 4
```

- En büyük rakam = `8`
- Demek ki **en az 8 deci-binary sayı** gerekir

Ve bu sayı her zaman **yeterlidir**, çünkü:
- Daha küçük basamaklar (2, 3, 4, 7) zaten 8 sayının içinde karşılanabilir

---

## Kod

```python
class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """
        return int(max(n))
```

---

## Örnekler

### Örnek 1
```
n = "32"
```

En büyük rakam = `3`

Cevap:
```
3
```

---

### Örnek 2
```
n = "1000"
```

En büyük rakam = `1`

Cevap:
```
1
```

---

### Örnek 3
```
n = "999"
```

En büyük rakam = `9`

Cevap:
```
9
```

---

## Zaman Karmaşıklığı

```
O(n)
```

- `n` stringi bir kez dolaşılır

---

## Alan Karmaşıklığı

```
O(1)
```

- Ekstra veri yapısı yok

---

## Neden Bu Soru Güzel?

- DP gibi görünüyor ama değil
- Matematiksel gözlem gerektiriyor
- Tek satırlık ama güçlü bir çözüm
- Interview’da “aha!” anı yaratır

---

## Özet

Bu çözüm:

✔ Basamak bazlı düşünür  
✔ Gereksiz simülasyon yapmaz  
✔ En optimal sonucu verir  
✔ Kod olarak çok sade ama mantık olarak güçlüdür  

Hazırsan 👉 **bir sonraki probleme geçelim** 🚀