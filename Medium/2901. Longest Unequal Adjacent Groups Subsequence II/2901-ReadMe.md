# 🧠 LeetCode 2901 - Longest Unequal Adjacent Groups Subsequence II

**Difficulty:** Hard  
**Problem Link:** [LeetCode 2901](https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-ii)

---

## 📘 Problem Description

Given:
- A list of words `words`
- A list of integers `groups` (same length as `words`), where each integer represents the group of the corresponding word.

Goal:
- Find the **longest subsequence** of `words` such that:
  1. Every **adjacent pair** of words in the subsequence:
     - Have a **Hamming Distance** of exactly **1** (only one character differs),
     - Belong to **different groups**.
  2. Return the actual **subsequence of words** (not just the length).

---

## 🧠 Intuition

Bu problem, klasik **Longest Path in DAG** tarzında düşünülebilir, ama:
- Kenar sadece `hammingDistance(word1, word2) == 1` VE `groups[i] != groups[j]` durumunda çizilebilir.
- Ardından klasik DP+Parent mantığıyla yolu takip ederek en uzun subsequence elde edilir.

---

## 🔨 Approach

1. Tanımlı `hammingValid(w1, w2)` fonksiyonu ile Hamming mesafesi kontrol edilir.
2. `dp[i]`: `i`'inci kelimeyi son olarak kullanarak oluşturulabilecek maksimum uzunluk.
3. `parent[i]`: `i`'inci kelimenin öncesindeki kelimenin indexi (rekonstrüksiyon için).
4. Her `i` için önceki tüm `j` indexleri gezilerek:
   - Eğer `hammingValid(words[i], words[j])` VE `groups[i] != groups[j]` ise:
     - `dp[i] = max(dp[i], dp[j] + 1)`
     - `parent[i] = j`
5. En uzun subsequence'in sonundaki index'ten başlayarak `parent` listesiyle yol geri alınır.

---

### 📈 Example
```python
Input:
words = ["ab", "ac", "bc", "bd"]
groups = [1, 2, 1, 2]

Output:
["ab", "ac", "bc", "bd"]
```
> Explanation: Her komşu çift Hamming uzaklığı 1 ve farklı grupta.

### ⏱️ Complexity

- **Time Complexity:** `O(n² × k)`, where `n` = len(words) and `k` = len(word)

- **Space Complexity:** `O(n)`

### 🏷️ Tags
`dynamic-programming`, `graph`, `sequence`, `string`, `hamming-distance`, `reconstruction`