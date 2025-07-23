# ⚡ LeetCode 1863 - Sum of All Subset XOR Totals

**Difficulty:** Easy  
**Problem Link:** [LeetCode 1863](https://leetcode.com/problems/sum-of-all-subset-xor-totals)

---

## 🧩 Problem Description

Given an array `nums`, return the **sum of all XOR totals for every subset** of `nums`.

- The XOR total of a subset is defined as the bitwise XOR of all its elements.  
- If the subset is empty, its XOR total is 0.

---

## 💡 Intuition

- Her alt küme için XOR değeri hesaplanmalı ve bunların toplamı alınmalıdır.
- Toplam alt küme sayısı `2^n`’dir. Her alt küme tek tek DFS veya bitmask ile üretilebilir.
- XOR işlemi birleşme özelliğine sahip olduğundan, recursive DFS oldukça uygundur.

---

## 🚀 Approach

Klasik **DFS** yaklaşımı:
1. Her eleman için 2 seçenek vardır:
   - Dahil et (XOR'la)
   - Dahil etme
2. Her yol tamamlandığında (`index == len(nums)`), o yoldaki XOR değeri toplam sonuca eklenir.

---

### 🧪 Example
```python
Input: nums = [1,3]
Subsets: [], [1], [3], [1,3]
XORs:     0   1     3     1^3 = 2
Sum = 0 + 1 + 3 + 2 = 6
Output: 6
```

### 🕵️ Complexity

- **Time Complexity:** `O(2^n)` – Her elemanın dahil edilip edilmediği 2 seçenekten dolayı.

- **Space Complexity:** `O(n)` – DFS için maksimum çağrı derinliği.

### 🏷️ Tags
`backtracking`, `bit-manipulation`, `DFS`, `subsets`, `recursion`