# 🔫 LeetCode 2125. Number of Laser Beams in a Bank    

**Difficulty:** Medium
**Problem Link:** [LeetCode 2125](https://leetcode.com/problems/number-of-laser-beams-in-a-bank/description/)

---

## 💡 Problem Description  

Bir banka güvenlik sisteminde her satır (`bank[i]`) bir **oda**yı temsil eder.  
Her odada `'1'` karakteri varsa, bu bir **güvenlik cihazı** (security device) anlamına gelir.  

Kurallar:  
- Aynı satırdaki cihazlar birbirine lazer göndermez.  
- **Farklı satırlardaki cihazlar**, aralarındaki satırda hiç cihaz yoksa, birbirine lazer gönderir.  

Görev:  
Toplam kaç **lazer ışını (laser beam)** olduğunu bul.  

---

### 🧩 Example 1  

**Input:**  
```java
bank = ["011001","000000","010100","001000"]
```

**Output:**
```java
8
```

**Explanation:**

- Satırlardaki cihaz sayıları:

```java
Row 0 → 4 device
Row 1 → 0 device
Row 2 → 2 device
Row 3 → 1 device
```

- Lazer bağlantıları:

- - Row 0 ↔ Row 2 → 4 × 2 = 8 ışın

- - Row 2 ↔ Row 3 → 2 × 1 = 2 ışın

- Toplam = 8 + 2 = 10
- Ancak arada boş satırlar olduğunda yalnızca ardışık dolu satırlar etkileşir → Sonuç `8`

###  🧠 Approach

1. Her satırdaki `'1'` karakterlerini say.

2. Eğer satırda cihaz yoksa (`count == 0`), o satırı yok say.

3. Eğer cihaz varsa:

- - Önceki dolu satırdaki cihaz sayısı ile çarp (`ans += prev * count`)

- - Sonra `prev = count` olarak güncelle.

Bu yöntem, **ardışık dolu satırlar** arasındaki lazer bağlantılarını doğru biçimde hesaplar.

### 🧮 Time & Space Complexity
| İşlem            | Zaman    | Alan |
| ---------------- | -------- | ---- |
| Her satırı gezme | O(N * M) | O(1) |

N = satır sayısı, M = sütun sayısı

### 💻 Code Implementation
```java
class Solution {
  public int numberOfBeams(String[] bank) {
    int prev = 0, ans = 0;

    for (String s : bank) {
      int count = 0;
      for (int i = 0; i < s.length(); i++)
        if (s.charAt(i) == '1')
          count++;

      if (count > 0) {
        ans += prev * count;
        prev = count;
      }
    }

    return ans;
  }
}
```

### 🏁 Summary
- ✔ Her satırdaki cihaz sayısı bulunur
- ✔ Boş satırlar atlanır
- ✔ Lazer sayısı, ardışık dolu satırlardaki cihazların çarpımıyla bulunur
- ✔ Zaman ve alan açısından verimli bir çözüm

**Tags:** `Array`, `String`, `Counting`