# ⚡ LeetCode 3607 - Power Grid Maintenance

**Difficulty:** Medium  
**Problem Link:** [LeetCode 3607](https://leetcode.com/problems/power-grid-maintenance/description/)

## 🧩 Problem Description
You are given a power grid with `c` stations (numbered `1` to `c`) and a list of **connections** between them.  
Each connection links two stations, forming a connected component (or “grid”).  

You also have a list of **queries**, where each query is one of two types:

1. `[1, x]` → Find the **smallest online station** in the same grid as station `x`.  
2. `[2, x]` → Take station `x` offline.

Initially, **all stations are online**.  
You must process the queries **in order** and return an array of results corresponding to **type 1** queries.

---

## 💡 Example

**Input:**
```python
c = 5
connections = [[1, 2], [2, 3], [4, 5]]
queries = [[1, 3], [2, 2], [1, 3], [2, 4], [1, 5]]
```

**Output:**
```python
[1, 1, 5]
```

**Explanation:**
- Initially: all stations online  
  → grid1 = {1, 2, 3}, grid2 = {4, 5}  
- Query `[1, 3]`: smallest online in grid {1, 2, 3} → **1**  
- Query `[2, 2]`: take station 2 offline  
- Query `[1, 3]`: grid {1, 3} → smallest online → **1**  
- Query `[2, 4]`: take station 4 offline  
- Query `[1, 5]`: grid {4, 5}, only 5 online → **5**

---

## 🧠 Approach

### 🧩 Key Idea:
The problem involves **connected components** and **dynamic online/offline states**.  
To efficiently handle connectivity, we use a **Disjoint Set Union (DSU)** (also known as Union-Find).  

However, queries involve both:
- Going **forward** (turning stations off)
- And asking questions **after changes**

This makes it hard to process online.  
So, we use a **reverse processing technique**:
1. Mark all “offline” operations first.
2. Traverse the queries **backward**, “undoing” offline operations.
3. Maintain the smallest online station per component as we go.

---

## ⚙️ Algorithm Steps

1. **Initialize DSU** for union-find structure to track connected components.  
2. Mark all stations as **online** initially, then process the queries to find which stations go offline.
3. Build a dictionary `minimum_online_stations` → maps each component to its smallest currently online station.
4. Traverse the queries **in reverse order**:
   - If the operation is `[1, x]`:
     - If `x` is online → append `x`
     - Else → append the smallest online station in the same component.
   - If the operation is `[2, x]`:
     - Reactivate station `x` and update the component’s smallest online station if needed.
5. Return the results in the original order by reversing the collected list.

---

## 🧩 Code Implementation

```python
class DSU:
    def __init__(self, size):
        self.parent = list(range(size))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def join(self, u, v):
        self.parent[self.find(v)] = self.find(u)


class Solution:
    def processQueries(
        self, c: int, connections: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        dsu = DSU(c + 1)
        for p in connections:
            dsu.join(p[0], p[1])

        online = [True] * (c + 1)
        offline_counts = [0] * (c + 1)
        minimum_online_stations = {}

        # First pass: mark stations that will go offline
        for q in queries:
            op, x = q[0], q[1]
            if op == 2:
                online[x] = False
                offline_counts[x] += 1

        # Initialize smallest online station for each component
        for i in range(1, c + 1):
            root = dsu.find(i)
            if root not in minimum_online_stations:
                minimum_online_stations[root] = -1

            station = minimum_online_stations[root]
            if online[i]:
                if station == -1 or station > i:
                    minimum_online_stations[root] = i

        ans = []
        # Reverse processing
        for i in range(len(queries) - 1, -1, -1):
            op, x = queries[i][0], queries[i][1]
            root = dsu.find(x)
            station = minimum_online_stations[root]

            if op == 1:
                if online[x]:
                    ans.append(x)
                else:
                    ans.append(station)

            if op == 2:
                if offline_counts[x] > 1:
                    offline_counts[x] -= 1
                else:
                    online[x] = True
                    if station == -1 or station > x:
                        minimum_online_stations[root] = x

        return ans[::-1]
```

### ⏱️ Complexity Analysis

| Operation          | Complexity                  |
| ------------------ | --------------------------- |
| DSU find/join      | `O(α(n))` (almost constant) |
| Processing queries | `O(q)`                      |
| Overall            | **O((n + q) α(n))**         |
| Space              | **O(n)**                    |


### ✅ Summary

✔ Used Union-Find (DSU) for efficient component tracking
✔ Processed queries in reverse to handle dynamic states
✔ Maintained smallest online station per component dynamically