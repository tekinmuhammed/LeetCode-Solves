# 🧩 3314. Construct the Minimum Bitwise Array I

## 🔍 Problem Özeti
- Bir `nums` dizisi veriliyor.
- Her `nums[i]` için, aşağıdaki şartı sağlayan **en küçük** `ans[i]` bulunmalı:

```text
ans[i] OR (ans[i] + 1) == nums[i]
Eğer böyle bir sayı yoksa, -1 döndürülmeli.

🧠 Temel Gözlem
🔴 Özel Durum: x = 2
2 = 10 (binary)

Hiçbir a için:

text
Kodu kopyala
a | (a + 1) = 2
olamaz.

➡️ Sonuç: x == 2 → -1

🔎 Genel Mantık (x ≠ 2)
LeetCode testlerine göre nums[i] değerleri asal (prime) sayılardır.

2 hariç tüm asal sayılar tektir

Binary gösterimleri mutlaka 1 ile biter

Örnek:
text
Kodu kopyala
x = 11 → 1011
x = 7  → 0111
💡 Kritik Bitwise Fikir
Amaç:
text
Kodu kopyala
a | (a + 1) = x
Bu eşitliği sağlamak için:

a ve a+1 sadece sondaki 1 bloğunda farklı olmalı

x’in en sağdaki 1 bloğunu kontrollü biçimde küçültmeliyiz

🛠️ Adım Adım Çözüm
1️⃣ x + 1 Hesapla
Sondaki tüm 1’ler 0 olur

Bir üst bitten 1 taşar

text
Kodu kopyala
x = 11 (1011)
x+1 = 12 (1100)
2️⃣ En Sağdaki 1 Bit’i Bul (Lowbit)
python
Kodu kopyala
lowbit = (x + 1) & -(x + 1)
Bu:

(x + 1)’deki en küçük 2^k değerini verir

Örnek:

text
Kodu kopyala
12 (1100) → lowbit = 4 (100)
3️⃣ Cevabı Hesapla
text
Kodu kopyala
ans = x - (lowbit / 2)
Örnek:

text
Kodu kopyala
x = 11
lowbit = 4
ans = 11 - 2 = 9
Kontrol:

text
Kodu kopyala
9 | 10 = 1011 = 11 ✅
✅ Kodun Mantığı
python
Kodu kopyala
class Solution:
    def minBitwiseArray(self, nums: list[int]) -> list[int]:
        ans = []
        for x in nums:
            if x == 2:
                ans.append(-1)
            else:
                next_val = x + 1
                lowbit = next_val & -next_val
                ans.append(x - (lowbit >> 1))
        return ans
⏱️ Zaman & Alan Karmaşıklığı
Zaman
text
Kodu kopyala
O(n)
Her sayı için sabit bit işlemleri

Alan
text
Kodu kopyala
O(1) (çıktı hariç)