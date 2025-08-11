# 🕰️ LeetCode 3342 - Find Minimum Time to Reach Last Room II

**Difficulty:** Hard  
**Problem Link:** [LeetCode 3342](https://leetcode.com/problems/find-minimum-time-to-reach-last-room-ii/)

---

## 🧩 Problem Description

You are in a 2D grid starting from `(0,0)`. Each cell has a `moveTime[r][c]`, indicating the **earliest time** you are allowed to **enter** that cell.

- You alternate between **quick step** and **slow step**:
  - Quick step costs 1 time unit.
  - Slow step costs 2 time units.
- You **start with a quick step**.
- You can **wait any amount of time** before stepping.

Return the **minimum time** required to reach the bottom-right corner `(m-1, n-1)`.

---

## 💡 Intuition

- Bu bir Dijkstra benzeri grid problemsidir.
- Her hücreye hem hızlı adım hem yavaş adımla gelme ihtimali vardır, bu yüzden `visited[r][c][step]` tutulur.
- Bir hücreye gitmek istediğimizde:
  - Eğer oraya varış zamanımız `moveTime[r][c]`'den küçükse, beklememiz gerekir.
  - Alternatif adım tipiyle (`quick` <-> `slow`) ilerlemeliyiz.

---

## 🚀 Approach

1. `heap` kullanılarak en kısa süre öncelikli işlenir (`(time, row, col, step_type)`).
2. 4 yönlü grid dolaşması yapılır.
3. Her hamlede:
   - Gidilecek hücrenin zamanı henüz gelmediyse beklenir.
   - Adım maliyeti (1 veya 2) eklenir.
4. Her hücreye sadece daha düşük zamanla erişiliyorsa heap'e eklenir.

---

### 🧪 Example

**Input**
```python
Input:
moveTime = [
  [0, 2],
  [1, 3]
]
```

**Output:** 
```python
4
```

### Explanation:

`(0,0)` -> `(0,1)` [wait 2], cost `1` (quick)
       -> `(1,1)` [already ≥3], cost `2` (slow)
**Total:** `1` (wait) + `1` + ``2` = `4`

### 🕵️ Complexity

- **Time Complexity:** `O(m * n * 2 * log(m * n))` — çünkü her hücre için 2 adım türü var.

- **Space Complexity:** `O(m * n * 2)` — visited matrisine göre.

### 🏷️ Tags

`graph`, `heap`, `dijkstra`, `grid`, `bfs`, `simulation`