# 🎨 LeetCode 75 - Sort Colors

**Difficulty:** Medium  
**Problem Link:** [LeetCode 75](https://leetcode.com/problems/sort-colors/)

---

## 📘 Problem Description

Given an array `nums` with `n` objects colored red (`0`), white (`1`), or blue (`2`), sort them **in-place** so that objects of the same color are adjacent, with the colors in the order `red`, `white`, and `blue`.

You must solve this problem **without using the built-in sort function**, and ideally in **one pass** and with **constant space**.

---

## 🧠 Intuition

Bu problem klasik **Dutch National Flag Algorithm**’dır. Üç farklı türde eleman içeren bir dizide:
- `0`'lar başa,
- `1`'ler ortaya,
- `2`'ler sona yerleştirilmelidir.

Bu durumda, 3 pointer kullanarak tek geçişte çözüm yapılabilir:
- `low`: 0'ların son index'ini gösterir.
- `mid`: işlenen mevcut elemanı gösterir.
- `high`: 2'lerin başladığı yeri gösterir.

---

## 🔨 Approach

1. `mid` işaretçisinden başlayarak her elemanı kontrol et:
   - Eğer `nums[mid] == 0`, 0'ı başa al, `low` ve `mid` ilerlet.
   - Eğer `nums[mid] == 1`, hiçbir şey yapmadan sadece `mid` ilerlet.
   - Eğer `nums[mid] == 2`, 2'yi sona al, `high` azalt (ama `mid` sabit tutulur çünkü gelen yeni değer kontrol edilmeli).
2. Dizi, tek bir geçişte sıralanmış olur.

---

### 🧪 Example
```python
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
```

### ⏱️ Complexity

- **Time Complexity:** `O(n)`

- **Space Complexity:** `O(1)`

### 🏷️ Tags
`two-pointers`, `sorting`, `in-place`, `array`, `dutch-national-flag`