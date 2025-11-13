# 💡 LeetCode 3228 – Maximum Number of Operations to Move Ones to the End

**Difficulty:** Medium  
**Problem Link:** [LeetCode 3228](https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-end/description/)

## 🧩 Problem Tanımı
Bir ikili (binary) string `s` veriliyor.  
Her operasyonda, bir `'1'` karakteri seçip onu **string’in sonuna taşıyabiliyorsun**,  
ama yalnızca `'1'`’in **hemen sağında `'0'` varsa** bu işlem yapılabiliyor.

Amaç:  
Tüm olası operasyonları en verimli şekilde yaparak maksimum işlem sayısını bulmak.

---

## 💬 Örnek

**Girdi:**
```python
s = "11010"
```

**Adımlar:**
```python
"11010" → "10101" (1. operasyon)
"10101" → "10011" (2. operasyon)
```

- Sonuç: `2` operasyon yapılabilir.
- Çıktı: **2**

#### ⚙️ Çözüm Mantığı
Bu problemde amaç, `'1'` karakterlerini en sona taşımak için kaç kez uygun bir **"1-0" çifti** oluşabileceğini saymaktır.

Ancak doğrudan çift saymak yerine, **"bir grup sıfır"** görüldüğünde
bu sıfırların solundaki `'1'`’ler potansiyel olarak bu sıfır grubuyla işlem yapabilir.
Yani:

- Her `'0'` grubu → o ana kadar görülen `'1'` sayısı kadar katkı yapar.

#### 🔢 Adım Adım Özet

1. `count_one`: Şimdiye kadar görülen `'1'` sayısı.

2. `ans`: Toplam yapılabilecek işlem sayısı.

3. String boyunca soldan sağa gezin:

- Eğer `'0'` grubuna geldiysek (örneğin `"000"`),
o ana kadar görülen `'1'` sayısı kadar `ans`'a ekle.

- Eğer `'1'` görürsen, `count_one`'ı 1 artır.

Her `'0'` bloğu, solundaki `'1'`’ler kadar potansiyel operasyona katkı yapar.

### 🧠 Örnek Üzerinde İzleme
`s = "101001"`

| i | s[i] | count_one | ans | Açıklama                                |
| - | ---- | --------- | --- | --------------------------------------- |
| 0 | 1    | 1         | 0   | İlk `'1'` görüldü                       |
| 1 | 0    | 1         | 1   | `'0'` bloğu, solunda 1 `'1'` var → +1   |
| 2 | 1    | 2         | 1   | Yeni `'1'` görüldü                      |
| 3 | 0    | 2         | 3   | `'0'` bloğu → 2 `'1'` katkı             |
| 4 | 0    | 2         | 5   | Aynı `'0'` bloğunda devam, katkı tekrar |
| 5 | 1    | 3         | 5   | Son `'1'` görüldü                       |


    Sonuç: `ans = 5`

### 🧱 Kodun Açıklamalı Hali
```python
class Solution:
    def maxOperations(self, s: str) -> int:
        count_one = 0  # Şimdiye kadar görülen '1' sayısı
        ans = 0        # Toplam operasyon sayısı
        i = 0
        while i < len(s):
            if s[i] == "0":
                # Arka arkaya gelen sıfırları bir grup olarak say
                while i + 1 < len(s) and s[i + 1] == "0":
                    i += 1
                # Bu sıfır bloğu, solundaki tüm '1'ler kadar operasyona izin verir
                ans += count_one
            else:
                # '1' gördükçe sayacı artır
                count_one += 1
            i += 1
        return ans
```

### 🧮 Zaman ve Bellek Karmaşıklığı
| Özellik                 | Değer                                              |
| ----------------------- | -------------------------------------------------- |
| **Zaman Karmaşıklığı**  | O(n)                                               |
| **Bellek Karmaşıklığı** | O(1)                                               |
| **Açıklama**            | String tek geçişte taranır; ek bellek kullanılmaz. |


### 📋 Özet
| Özellik                | Açıklama                                                                        |
| ---------------------- | ------------------------------------------------------------------------------- |
| **Problem Adı**        | Maximum Number of Operations to Move Ones to the End                            |
| **Numara**             | 3228                                                                            |
| **Zorluk**             | 🟢 Easy – 🟠 Medium arası                                                       |
| **Kavramlar**          | String, Greedy, Counting                                                        |
| **Yaklaşım**           | Her `'0'` bloğu için, solundaki `'1'` sayısı kadar operasyon ekle               |
| **Zaman Karmaşıklığı** | O(n)                                                                            |
| **Uzay Karmaşıklığı**  | O(1)                                                                            |
| **Ana Fikir**          | `'0'` gruplarının her biri, solundaki `'1'` sayısı kadar taşıma fırsatı sağlar. |
