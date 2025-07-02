# 🔤 3403. Find the Lexicographically Largest String From the Box I

**Difficulty:** Medium  
**Konular:** String, Two Pointers, Greedy  
**Problem Link:** https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-i/

---

## 📘 Problem Açıklaması

Bir kelime (`word`) ve bir `numFriends` değeri verilmiş.  
Sen ve arkadaşların sırayla kutudaki karakterleri seçiyorsunuz. Amacın:

> **Lexicographically en büyük** string'i oluşturmak.

### Özellikle:
- Eğer `numFriends == 1` → kelimenin tamamı senin → sadece `word`'ü döndür.
- Eğer daha fazla arkadaş varsa → kutudan ardışık karakterleri sırayla alarak **en büyük** string'i oluşturmak istiyoruz.

---

## 🧠 Algoritma Açıklaması

Kodun iki ana parçası var:

### 1. `lastSubstring(word)`:  
Bu, verilen kelimedeki **sözlük sırasına göre en büyük substring**'i bulur.

> Örneğin: `word = "abab"` → en büyük substring: `"bab"`

İç mantığı:  
- `i` ve `j` iki farklı başlangıç noktası.
- Her seferinde karakterleri karşılaştırır, eşitse `k` ile devam eder.
- Eğer `s[i+k] < s[j+k]`, yani `j` daha büyük bir string başlatıyorsa, `i = j`.

### 2. `answerString(word, numFriends)`  
- Eğer `numFriends == 1`: kelime olduğu gibi döner.
- Değilse: en büyük substring’in ilk `n - numFriends + 1` karakterini alır.

#### Neden?
Çünkü `numFriends` kişi karakterleri sırayla seçeceği için biz **ilk sırada** olacağımızdan, en büyük substring’in bu uzunluktaki kısmını almak, maksimum kazancı sağlar.

---

## 🧪 Örnek

```python
word = "abcabc"
numFriends = 3
lastSubstring("abcabc") → "cabc"

len(word) = 6, n - numFriends + 1 = 4

return → "cabc"[:4] = "cabc"
```

### ⏱️ Zaman ve Bellek Karmaşıklığı

- `lastSubstring:` `O(n)`, çünkü her karaktere en fazla 2 kez bakılır.

- Toplam: **O(n)** zaman, **O(1)** ekstra alan.

### 🏷️ Etiketler
`string`, `two-pointers`, `greedy`, `lexicographical`