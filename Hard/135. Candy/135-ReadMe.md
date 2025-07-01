# 🍬 LeetCode 135 - Candy

**Difficulty:** Hard  
**Problem Link:** [LeetCode 135](https://leetcode.com/problems/candy)

---

## 📘 Problem Description

There are `n` children standing in a line. Each child is assigned a **rating**. You need to distribute **at least one candy** to each child such that:

1. Each child must have at least one candy.
2. Children with a higher rating than their immediate neighbors must get **more candies** than them.

Return the **minimum total number of candies** you must give.

---

## 💡 Algorithm Insight

Bu problem, **greedy yaklaşımı** ile çözülür. Ana fikir şu:

- Her çocuğa başlangıçta 1 şeker verilir.
- İki geçiş (soldan sağa ve sağdan sola) ile komşulara göre adalet sağlanır.

---

### 🔁 Example
```python
Input: ratings = [1, 0, 2]
Step 1: Initial candies = [1, 1, 1]

Left to Right: 1 < 0 → no change; 0 < 2 → candies = [1, 1, 2]
Right to Left: 0 > 1 → candies = [2, 1, 2]

Output: 5
```

### ⏱️ Time & Space Complexity

- **Time Complexity:** `O(n)`

- **Space Complexity:** `O(n)` — for the candies array

### 🏷️ Tags
`greedy`, `array`, `two-pass`, `ratings`