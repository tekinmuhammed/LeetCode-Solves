# 🔢 LeetCode 273 - Integer to English Words

**Difficulty:** Hard  
**Problem Link:** [LeetCode 273](https://leetcode.com/problems/integer-to-english-words/)

---

## 📘 Problem Description

Convert a non-negative integer to its English words representation.  
The input is guaranteed to be less than 2³¹ - 1.

---

### 🧪 Examples

#### Example 1:
```python
Input: num = 123
Output: "One Hundred Twenty Three"
```

#### Example 2:
```python
Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"
```

#### Example 3:
```python
Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
```

## 🧠 Approach
Problemi parça parça ele almak gerekir:

1. İngilizce sayılar 3’lü gruplar halinde okunur: **Billions, Millions, Thousands, Hundreds**.

2. Her 3 basamaklı grubu çözen yardımcı fonksiyonlar tanımlanır:

- `one(num)`: 1-9 arası

- `two_less_20(num)`: 10-19 arası özel sayılar

- `ten(num)`: onlar basamağı (20, 30, ...)

- `two(num)`: 1-99 arası sayıları işler

- `three(num)`: 1-999 arası sayıları işler

3. Sayı `billion`, `million`, `thousand`, `rest` olmak üzere 4 gruba ayrılır.

4. Her grup varsa metne çevrilip uygun ekiyle (`Billion`, `Million`, `Thousand`) birlikte eklenir.

## ⏱️ Complexity
**Time Complexity:** `O(1)`
Sabit sayılarla çalışıldığı için zaman karmaşıklığı sabittir.

**Space Complexity:** `O(1)`

## 🏷️ Tags
`recursion`, `string-manipulation`, `simulation`, `leetcode-hard`