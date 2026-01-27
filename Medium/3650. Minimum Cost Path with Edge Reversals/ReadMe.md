## 3650. Minimum Cost Path with Edge Reversals

### Problem Özeti

- `n` adet düğüm (0 → n-1)
- Yönlü kenarlar: `edges[i] = [u, v, w]`
  - `u → v` yönünde geçiş maliyeti `w`
- Bir kenarı **ters yönde kullanmak** istersen:
  - `v → u` geçişi mümkün
  - fakat maliyeti **`2 * w`**

Amaç:
- `0` düğümünden `n-1` düğümüne **minimum toplam maliyetle** ulaşmak

---

## Temel Fikir 💡

Bu problem klasik bir **Shortest Path (En Kısa Yol)** problemidir.

Ama fark şu:
- Her kenar için **iki farklı geçiş** tanımlanabilir:
  1. Normal yön → maliyet `w`
  2. Ters yön (edge reversal) → maliyet `2w`

👉 Bu yüzden grafiği **genişletilmiş adjacency list** ile kurup
**Dijkstra algoritması** kullanmak yeterlidir.

---

## Grafik Modelleme

Her `[u, v, w]` kenarı için:

```text
u ----w----> v
v ----2w---> u
Bu şekilde:

Edge reversal işlemi ayrı bir kenar gibi modellenir

Ekstra state tutmaya gerek kalmaz ✔️

Algoritma
Adjacency list oluştur

Dijkstra:

min_dist[i] → 0’dan i’ye minimum maliyet

Priority Queue (Min-Heap) kullan

n-1 düğümüne ulaşıldığında sonucu döndür

Python Kodu
import heapq

class Solution:
    def minCost(self, n: int, edges: list[list[int]]) -> int:
        # Adjacency List
        adj = [[] for _ in range(n)]
        
        for u, v, w in edges:
            # Normal yön
            adj[u].append((v, w))
            # Ters yön (edge reversal)
            adj[v].append((u, 2 * w))
            
        # Dijkstra
        pq = [(0, 0)]  # (maliyet, düğüm)
        min_dist = [float('inf')] * n
        min_dist[0] = 0
        
        while pq:
            d, u = heapq.heappop(pq)
            
            if u == n - 1:
                return d
            
            if d > min_dist[u]:
                continue
            
            for v, cost in adj[u]:
                nd = d + cost
                if nd < min_dist[v]:
                    min_dist[v] = nd
                    heapq.heappush(pq, (nd, v))
                    
        return -1 if min_dist[n - 1] == float('inf') else min_dist[n - 1]
Örnek Mantık
Edge: 0 -> 1 (w = 5)

Seçenekler:
0 -> 1 : 5
1 -> 0 : 10
Dijkstra:

Hangi yön daha ucuzsa otomatik seçer

Gereksiz ters geçişleri zaten eler ✔️

Karmaşıklık Analizi
Zaman: O((V + E) log V)

Alan: O(V + E)

Standart Dijkstra maliyeti, ek state yok

