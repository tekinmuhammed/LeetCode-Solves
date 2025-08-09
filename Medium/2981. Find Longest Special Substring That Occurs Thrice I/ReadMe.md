# 🔁 LeetCode 2981 - Find Longest Special Substring That Occurs Thrice I

**Difficulty:** Medium  
**Problem Link:** [LeetCode 2981](https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i)

---

## 📘 Problem Description

Given a string `s`, you need to find the length of the **longest special substring** that occurs **at least three times**.

A **special substring** is defined as a **substring that consists of only one repeating character**, like `"a"`, `"bbb"`, `"zzzz"`.

---

### 🧪 Examples

#### Example 1:
```python
Input: s = "aaaa"
Output: 2
```

## Explanation:
- Substrings of length 1: "a" appears 4 times → valid
- Substrings of length 2: "aa" appears 3 times → valid
- Substrings of length 3: "aaa" appears 2 times → not valid
- Answer is 2

## Example 2:
```python
Input: s = "abcdef"
Output: -1
```

## Explanation:

No special substring appears 3 times.

## 🧠 Approach

- Tüm olası uzunlukları `length = 1` ile `n` arasında deniyoruz.

- Her uzunluk için:

- - Kaydırmalı pencere (sliding window) ile alt string'leri çıkarıyoruz.

- - Eğer substring yalnızca bir harften oluşuyorsa (`len(set(substring)) == 1`), onu `count` sözlüğünde takip ediyoruz.

- Her substring'in **en az 3 kez** geçip geçmediğini kontrol ediyoruz.

- Bu şartı sağlayan substring'lerin uzunlukları arasında en büyüğü cevaptır.

## ⏱️ Complexity

- **Time Complexity:** `O(n²)`

- - En dıştaki `length` döngüsü: `O(n)`

- - İçteki `i` döngüsü: `O(n)`

- - `set(substring)` işlemi: `O(k)` → burada `k = length`, en kötü `O(n)`
Yani toplamda `O(n³)`'e yakın karmaşıklık oluşabilir ama genelde `len(set()) == 1` kontrolü hızlı çalışır.

- **Space Complexity:** `O(n)`

- Substring sayımını tutmak için kullanılan `count` sözlüğü.

## 🏷️ Tags

`string`, `sliding-window`, `frequency-counter`, `brute-force`