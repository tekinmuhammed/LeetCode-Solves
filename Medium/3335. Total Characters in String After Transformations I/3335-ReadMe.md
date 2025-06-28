# 🔁 LeetCode 3335 - Total Characters in String After Transformations I

**Difficulty:** Medium  
**Problem Link:** [LeetCode 3335](https://leetcode.com/problems/total-characters-in-string-after-transformations-i)

---

## 🧩 Problem Description

You are given:
- A lowercase string `s`.
- An integer `t` representing the number of transformation steps.

Each character in the string transforms as follows:
- `'a'` becomes `'b'`
- `'b'` becomes `'c'`
- ...
- `'y'` becomes `'z'`
- `'z'` becomes `'a' + 'b'` (i.e., 2 characters)

This transformation is applied **t times to all characters**, and you must return the **total number of characters** in the final string, modulo `10^9 + 7`.

---

## 💡 Intuition

Her harf için kaç karaktere dönüşeceğini takip edebiliriz. Bu nedenle:

- `dp[i]`: harf sırasındaki `i` (0 = 'a', ..., 25 = 'z') karakterinin `t` adım sonra kaç karaktere dönüştüğünü temsil eder.
- Tüm karakterler başlangıçta `dp[i] = 1` ile başlar.
- Her dönüşümde:
  - `dp[i] = dp[i+1]` (örneğin 'a' → 'b', dolayısıyla 'a' kadar karakter, 'b' kadar olur)
  - `dp[25] = dp[0] + dp[1]` ('z' özel: 'a' + 'b')

---

## 🚀 Approach

1. `dp` dizisini 26 harf için başlat.
2. `t` kez dönüşüm uygula:
   - Yeni `dp` oluştur.
   - `dp[i] = dp[i+1]` (i < 25)
   - `dp[25] = dp[0] + dp[1]`
3. Başlangıç stringindeki her harf için `dp[ord(ch)-ord('a')]` değeri toplanır.

---

### 🧪 Example
```python
Input:
s = "abc"
t = 1

Output:
3

Explanation:
'a' → 'b', 'b' → 'c', 'c' → 'd' → total 3 characters.
```

```python
Input:
s = "z"
t = 1

Output:
2

Explanation:
'z' → 'a' + 'b' → 2 characters
```

### ⏱️ Complexity

- **Time Complexity:** `O(26 × t + |s|)`

- **Space Complexity:** `O(26)`

### 🏷️ Tags
`string`, `dynamic-programming`, `simulation`, `transformation`, `modular-arithmetic`