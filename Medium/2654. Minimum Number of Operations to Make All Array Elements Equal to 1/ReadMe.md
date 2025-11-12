# 🧩 LeetCode 2654 – Minimum Number of Operations to Make All Array Elements Equal to 1

## 🔍 Problem Tanımı
Bir tamsayı dizisi `nums` veriliyor. Her bir işlemde, iki **komşu** eleman seçip birini `gcd(a, b)` (yani ikisinin en büyük ortak böleni) ile değiştirebiliyorsun.  
Amaç, **tüm diziyi sadece `1`’lerden oluşacak hale getirmek** için gereken minimum işlem sayısını bulmaktır.  
Eğer bu imkansızsa `-1` döndürülmelidir.

---

## 💡 Örnek

**Girdi:**
```python
nums = [2, 6, 3, 4]
```

**Çözüm:**

1. `gcd(6, 3) = 3`, `gcd(3, 4) = 1`
→ `3` ve `4` üzerinden bir `1` elde edilebilir.
Bu alt dizinin uzunluğu 2 → 1 işlemle `1` oluşturulabilir.

2. Artık bir tane `1` var. Diğer tüm elemanları bu `1` üzerinden 1 yapmak için
`n - 1 = 3` işlem gerekir.

Toplam = 1 + 3 = 4

**Çıktı:** `4`

### ⚙️ Çözüm Mantığı
**🧠 1. Dizide zaten `1` varsa:**
- O `1`’leri kullanarak geri kalan tüm elemanları `1` yapmak kolaydır.
Çünkü `gcd(1, x) = 1` her zaman.

- Dolayısıyla sadece `1` olmayan elemanları `1` yapmak gerekir.

    Gerekli işlem sayısı = `n - count(1)`

**🔎 2. Dizide hiç `1` yoksa:**
- O zaman önce **bir tane `1` oluşturmak** gerekir.

- Bunun için dizideki her alt dizinin `gcd` değerine bakılır.
Eğer bir alt dizinin `gcd` değeri `1` ise, o alt dizi üzerinden bir `1` üretilebilir.

- Uzunluğu `L` olan bir alt dizide bu işlemi yapmak için `L - 1` işlem gerekir.

**💡 Örnek:**
`[6, 10, 15]` → `gcd(6,10,15)=1`, uzunluk = `3`
→ İlk `1`’i oluşturmak için `3 - 1 = 2` işlem gerekir.

**⚖️ 3. Minimum alt dizi bulunur**
Dizideki tüm olası alt diziler için `gcd` hesaplanır ve
`gcd == 1` olanların en kısa uzunluğu seçilir.
Bu, `min_ops_to_make_one = j - i` ile hesaplanır.

**🚫 4. Eğer hiçbir alt dizide `gcd == 1` çıkmazsa:**
Bu durumda hiçbir zaman `1` üretilemez → `return -1`.

**✅ 5. Sonuç:**
Eğer `1` üretilebiliyorsa, toplam işlem sayısı:
```python
min_ops_to_make_one + (n - 1)
```

Yani:

- `min_ops_to_make_one`: ilk 1’i üretmek için gereken işlem sayısı

- `n - 1`: kalan tüm elemanları 1 yapmak için gereken işlem sayısı

### 🧮 Zaman Karmaşıklığı
- Her alt dizi için `gcd` hesaplanıyor → `O(n²)`

- Her `gcd` hesaplaması ortalama `O(log(max(nums)))`

- **Toplam**: `O(n² * log(max(nums)))`
Küçük diziler için kabul edilebilir.

**🧱 Kodun Açıklamalı Hali**
```python
import math

class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)

        # 1️⃣ Dizide zaten 1 varsa, doğrudan diğerlerini 1 yapmak yeterli
        ones_count = nums.count(1)
        if ones_count > 0:
            return n - ones_count

        # 2️⃣ Dizide hiç 1 yoksa: ilk 1 oluşturmak için en kısa alt diziyi bul
        min_ops_to_make_one = float('inf')

        for i in range(n):
            current_gcd = nums[i]
            for j in range(i + 1, n):
                current_gcd = math.gcd(current_gcd, nums[j])
                if current_gcd == 1:
                    # İlk 1’i oluşturmak için gereken işlem sayısı (j - i)
                    ops_to_make_one = j - i
                    min_ops_to_make_one = min(min_ops_to_make_one, ops_to_make_one)
                    break  # Daha kısa alt dizi bulamayız, iç döngüden çık

        # 3️⃣ Hiçbir alt dizide gcd=1 çıkmadıysa imkansız
        if min_ops_to_make_one == float('inf'):
            return -1

        # 4️⃣ İlk 1 oluşturulduktan sonra kalan elemanları 1 yapmak için (n-1) işlem gerekir
        return min_ops_to_make_one + (n - 1)
```

### 🧩 Özet
| Özellik                | Açıklama                                                                             |
| ---------------------- | ------------------------------------------------------------------------------------ |
| **Problem Adı**        | Minimum Number of Operations to Make All Array Elements Equal to 1                   |
| **Numara**             | 2654                                                                                 |
| **Zorluk**             | 🟠 Medium                                                                            |
| **Kavramlar**          | GCD, Alt dizi, Sayı Teorisi, Brute Force                                             |
| **Yaklaşım**           | En kısa gcd=1 alt diziyi bul, sonra kalanları domino etkisiyle 1 yap                 |
| **Zaman Karmaşıklığı** | O(n² · log(max(nums)))                                                               |
| **Uzay Karmaşıklığı**  | O(1)                                                                                 |
| **Ana Fikir**          | Önce bir tane `1` oluşturmak gerekir; sonra o `1` ile diğerlerini 1 yapmak kolaydır. |