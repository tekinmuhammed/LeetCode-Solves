# 🔤 LeetCode 1408 - String Matching in an Array

**Difficulty:** Easy  
**Problem Link:** [LeetCode 1408](https://leetcode.com/problems/string-matching-in-an-array/)

---

## 🧩 Problem Description

Given an array of strings `words`, return **all strings** in the array that are **substrings** of another word in the array.

You may return the answer in **any order**.

---

## 💡 Intuition

Bir kelime başka bir kelimenin içinde geçiyorsa, bu kelimeyi sonuç listesine eklememiz gerekiyor. Bu, klasik bir **substring** arama problemidir.

---

## 🚀 Approach

1. Tüm kelimeler çiftler halinde karşılaştırılır.
2. `words[i] in words[j]` kontrolü yapılır.
   - `i != j` koşulu ile aynı kelimeyle kendini karşılaştırma engellenir.
3. Eğer `words[i]`, `words[j]` içinde geçiyorsa, `words[i]` sonucu listesine eklenir.
4. İç içe döngüden dolayı zaman karmaşıklığı `O(n^2 * m)` olur (n: kelime sayısı, m: ortalama uzunluk).

---

🧪 Example
```python
Input: ["mass","as","hero","superhero"]
Output: ["as","hero"]
Explanation: "as" is a substring of "mass" and "hero" is a substring of "superhero".
```

### 🕵️ Complexity

- **Time Complexity:** `O(n^2 * m)`

- - `n` = number of words

- - `m` = average length of the strings

- **Space Complexity:** `O(k)`

- - `k` = number of matching words

### 🏷️ Tags
`string`, `substring`, `brute-force`