# 865. Smallest Subtree with all the Deepest Nodes

**Difficulty:** Medium  
**Problem Link:** [LeetCode 865](https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/description/)

---

## 🧩 Problem Özeti

Bir **binary tree** veriliyor.

🎯 Amaç:
> Ağaçtaki **en derin node’ların tamamını** kapsayan **en küçük subtree**’nin kökünü bulmak.

Başka bir deyişle:
- En derin seviyedeki tüm node’ları al
- Bu node’ların **en düşük ortak atası (LCA)** aslında aradığımız subtree’nin kökü olur

---

## 🧠 Temel Fikir

Bu problem:
- **Depth (derinlik)**
- **Lowest Common Ancestor (LCA)**

kavramlarının birleşimi gibi düşünülebilir.

Ama senin çözümün çok daha **şık**:
> Tek DFS ile hem derinliği hem de cevabı birlikte hesaplıyor 👌

---

## 🔁 DFS Stratejisi

Her node için şu bilgileri döndürüyoruz:

```python
(depth, subtree_root)
```
- `depth`: Bu node’dan aşağıya maksimum derinlik
- `subtree_root`: En derin node’ları kapsayan subtree’nin kökü

### 🔄 DFS Kuralları
Bir node için:
1. Sol ve sağ subtree’leri gez
2. Derinlikleri karşılaştır

**Durumlar**
**🔹 Sol daha derinse**
→ En derin node’lar solda
```python
return (left_depth + 1, left_node)
```
**🔹 Sağ daha derinse**
→ En derin node’lar sağda
```python
return (right_depth + 1, right_node)
```
**🔹 Derinlikler eşitse**
→ En derin node’lar iki tarafta
→ Bu node **LCA olur**
```python
return (left_depth + 1, node)
```

### ✅ Kod
```python
class Solution(object):
    def subtreeWithAllDeepest(self, root):
        def dfs(node):
            if not node:
                return (0, None)

            left_depth, left_node = dfs(node.left)
            right_depth, right_node = dfs(node.right)

            if left_depth > right_depth:
                return (left_depth + 1, left_node)
            elif right_depth > left_depth:
                return (right_depth + 1, right_node)
            else:
                return (left_depth + 1, node)

        return dfs(root)[1]
```

### 🧪 Örnek
```python
        3
       / \
      5   1
     / \   \
    6   2   8
       / \
      7   4
```
- En derin node’lar: `7` ve `4`
- Ortak en küçük subtree: `2`
👉 Fonksiyon `TreeNode(2)` döner ✔️

### ⏱️ Karmaşıklık
- **Zaman:** `O(n)`
    (Her node sadece 1 kez ziyaret edilir)
- **Alan:** `O(h)`
(DFS recursion stack, `h` = ağaç yüksekliği)