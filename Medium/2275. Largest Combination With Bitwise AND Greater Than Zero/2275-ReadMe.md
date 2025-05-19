# 🟨 LeetCode 2275 - Largest Combination With Bitwise AND Greater Than Zero

**Difficulty:** Medium  
**Problem Link:** [LeetCode 2275](https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/)

---

## 📘 Problem Description

You are given an array `candidates` of positive integers.

Return the **largest size of a subset** of `candidates` such that the **bitwise AND** of all the numbers in the subset is **greater than 0**.

---

## 🧪 Example

### Input:
```cpp
candidates = [16,17,71,62,12,24,14]
```

## Output:
```cpp
4
```

## 🚀 Approach

- Her bir bit pozisyonu (0–23) için kaç sayı bu biti içeriyor onu sayarız.

- Bitwise AND işleminin sonucu > 0 olması için tüm elemanlarda en az bir bitin 1 olması gerekir.

- En fazla kaç sayı aynı biti paylaşıyor bulursak, o kadar eleman içeren bir subset AND > 0 üretir.

## ⏱️ Complexity
- **Time Complexity:** O(24 * n) → ~O(n), where n is the size of `candidates`

- **Space Complexity:** O(1)

## 🏷️ Tags
`bit-manipulation`, `greedy`, `leetcode-medium`