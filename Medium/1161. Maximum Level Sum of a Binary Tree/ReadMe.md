# 1161. Maximum Level Sum of a Binary Tree

**Difficulty:** Medium  
**Problem Link:** [LeetCode 1123](https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/)

---

## 🧩 Problem Özeti

Bir **binary tree** veriliyor.  
Her seviyedeki (level) düğümlerin değerlerini topluyoruz.

🎯 Amaç:
> **Toplamı en büyük olan seviyenin numarasını (1-indexed)** döndürmek

⚠️ Eğer birden fazla seviye aynı maksimum toplama sahipse:
- **En küçük seviye numarası** seçilir.

---

## 🧠 Çözüm Fikri (BFS – Level Order Traversal)

Bu problem için en doğal yaklaşım **BFS (genişlik öncelikli arama)**:

- BFS zaten ağacı **seviye seviye** gezer
- Her seviyede:
  - O seviyedeki düğüm sayısını biliriz
  - O düğümlerin değerlerini toplayabiliriz

---

## 🔍 Algoritma Adımları

1. Root’u bir **queue** içine koy
2. `level = 1` ile başla
3. Queue boş olana kadar:
   - Mevcut seviyedeki düğüm sayısını al (`size`)
   - Bu `size` kadar düğüm pop edip:
     - Değerlerini `level_sum`’a ekle
     - Çocuklarını queue’ya ekle
4. Eğer `level_sum > max_sum` ise:
   - `max_sum`’ı güncelle
   - `answer = level`
5. Seviyeyi artır

---

## ✅ Senin Kodun

```python
from collections import deque

class Solution(object):
    def maxLevelSum(self, root):
        queue = deque([root])
        level = 1
        max_sum = float('-inf')
        answer = 1
        
        while queue:
            level_sum = 0
            size = len(queue)
            
            for _ in range(size):
                node = queue.popleft()
                level_sum += node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if level_sum > max_sum:
                max_sum = level_sum
                answer = level
            
            level += 1
        
        return answer
```

### 🧪 Örnek
**Ağaç:**
```python
        1
       / \
      7   0
     / \
    7  -8
```
**Seviye Toplamları:**
- Level 1 → `1`
- Level 2 → `7 + 0 = 7`
- Level 3 → `7 + (-8) = -1`
**➡️ En büyük toplam = 7 → Seviye 2**

### ⏱️ Karmaşıklık Analizi
- **Zaman:** `O(n)`
(Her düğüm bir kez ziyaret edilir)

- **Alan:** `O(w)`
(`w` = ağacın maksimum genişliği, queue boyutu)