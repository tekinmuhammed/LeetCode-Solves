# 712. Minimum ASCII Delete Sum for Two Strings

**Difficulty:** Medium
**Link:** [LeetCode 712](https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/description/)  

---

## 🧩 Problem Özeti

İki string veriliyor: `s1` ve `s2`.

🎯 Amaç:
> İki string’i **eşit hale getirmek** için silinmesi gereken karakterlerin  
> **ASCII değerleri toplamını minimum yapmak**.

📌 Sadece **silme** işlemi var, ekleme veya yer değiştirme yok.

---

## 💡 Temel Fikir (DP Mantığı)

Bu problem, klasik **String DP** problemidir ve şu soruya indirgenir:

> `s1[i:]` ve `s2[j:]` substring’lerini eşit yapmak için  
> minimum ASCII silme maliyeti nedir?

**Bu yüzden:**
```python
dp[i][j] = s1[i:] ve s2[j:] eşit yapmak için minimum maliyet
```

### 🧱 DP Taban Durumları
**1️⃣ `s1` bittiğinde**
`s2`’nin kalan tüm karakterlerini silmemiz gerekir:
```python
dp[m][j] = dp[m][j + 1] + ord(s2[j])
```

**2️⃣ `s2` bittiğinde**
`s`1’in kalan tüm karakterlerini sileriz:
```python
dp[i][n] = dp[i + 1][n] + ord(s1[i])
```

🔄 DP Geçişleri
Eğer karakterler eşitse
Silme gerekmez:

python
Kodu kopyala
dp[i][j] = dp[i + 1][j + 1]
Eğer farklıysa
İki seçenek var:

s1[i] sil → ord(s1[i]) + dp[i+1][j]

s2[j] sil → ord(s2[j]) + dp[i][j+1]

Minimumu alırız:

python
Kodu kopyala
dp[i][j] = min(
    ord(s1[i]) + dp[i + 1][j],
    ord(s2[j]) + dp[i][j + 1]
)
✅ Senin Kodun
python
Kodu kopyala
class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        m, n = len(s1), len(s2)
        
        # dp[i][j]: s1[i:] ve s2[j:] eşit yapmak için minimum ASCII silme maliyeti
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # s1 bitmişse, s2'nin kalanını sil
        for j in range(n - 1, -1, -1):
            dp[m][j] = dp[m][j + 1] + ord(s2[j])
        
        # s2 bitmişse, s1'in kalanını sil
        for i in range(m - 1, -1, -1):
            dp[i][n] = dp[i + 1][n] + ord(s1[i])
        
        # DP doldurma
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = min(
                        ord(s1[i]) + dp[i + 1][j],
                        ord(s2[j]) + dp[i][j + 1]
                    )
        
        return dp[0][0]
🧪 Örnek
text
Kodu kopyala
s1 = "sea"
s2 = "eat"
Sil: 's' → 115

Sil: 't' → 116
➡️ Toplam = 231

Fonksiyon çıktısı: ✅ 231

⏱️ Zaman & Alan Karmaşıklığı
Zaman: O(m * n)

Alan: O(m * n)

📌 İstersen bu çözüm:

O(n) alanlı rolling array ile optimize edilebilir.

