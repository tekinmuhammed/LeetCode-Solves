# 🔢 LeetCode 368 - Largest Divisible Subset

**Difficulty:** Medium  
**Problem Link:** [LeetCode 368](https://leetcode.com/problems/largest-divisible-subset/)

---

## 🧩 Problem Description

Given a set of **distinct positive integers** `nums`, return the largest subset such that **every pair (Si, Sj)** in the subset satisfies:

> `Si % Sj == 0` or `Sj % Si == 0`

If there are multiple solutions, return **any** of them.

---

## 💡 Intuition

Bu bir klasik **Longest Increasing Subsequence (LIS)** varyasyonudur. Ancak bu sefer artan sıralar yerine, sayılar birbirini tam bölebilecek şekilde zincir oluşturmalıdır.

---

## 🚀 Approach

1. **Sıralama:** Sayıları küçükten büyüğe sırala. Bu, bölenler daha önce gelmesini sağlar.
2. **DP tablosu:** 
   - `dp[i]`: `nums[i]` ile biten en uzun divisible subset'in uzunluğu.
   - `prev[i]`: `nums[i]`'den önce gelen uygun sayıların indeksini takip eder.
3. Her sayı için daha önceki tüm sayılarla kontrol yapılır:  
   `nums[i] % nums[j] == 0` ise, `dp[i] = max(dp[i], dp[j] + 1)`

4. Maksimum uzunlukta zincir tespit edilir ve `prev` dizisi yardımıyla geri izleme yapılır.

---

### 🧪 Example

```makefile
Input: [1, 2, 4, 8]
Output: [1, 2, 4, 8]
Explanation: Her sayı bir öncekini tam bölebiliyor.
```

### 🕵️ Complexity

- **Time Complexity:** `O(n^2)` – Her `i` için tüm `j` değerleri kontrol ediliyor.

- **Space Complexity:** `O(n)` – DP ve `prev` dizileri için.

### 🏷️ Tags
`dynamic-programming`, `greedy`, `sorting`, `backtracking`, `subsets`, `LIS-variation`