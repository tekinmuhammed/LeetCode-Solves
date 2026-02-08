# 110. Balanced Binary Tree

**Difficulty:** Easy  
**Problem Link:** [LeetCode 110](https://leetcode.com/problems/balanced-binary-tree/description/)

---

## Problem Özeti

Bir **binary tree** şu şartı sağlıyorsa **balanced** kabul edilir:

- Her düğüm için  
  **sol alt ağacın yüksekliği** ile  
  **sağ alt ağacın yüksekliği** arasındaki fark **en fazla 1** olmalıdır.

Bu kural **tüm düğümler** için geçerli olmalıdır.

---

## Temel Fikir

Bu problemde en kritik nokta:

- Hem **yüksekliği hesaplamak**
- Hem de aynı anda **dengeyi kontrol etmek**

Bunu iki ayrı traversal ile yapmak verimsiz olur.

Bu yüzden:
- **Post-order traversal** (önce çocuklar, sonra düğüm)
- Ve **erken durdurma (early stop)** tekniği kullanılır.

---

## Ana Strateji

- `height(node)` fonksiyonu:
  - Eğer alt ağaç **balanced değilse** → `-1` döner
  - Aksi halde → ağacın **yüksekliğini** döner
- Her düğümde:
  - Sol ve sağ yükseklikler hesaplanır
  - Fark `> 1` ise direkt `-1` döndürülür
- En üstte:
  - Sonuç `-1` değilse ağaç balanced demektir

---

## Kod

```python
class Solution(object):
    def isBalanced(self, root):
        def height(node):
            if not node:
                return 0

            left = height(node.left)
            if left == -1:
                return -1

            right = height(node.right)
            if right == -1:
                return -1

            if abs(left - right) > 1:
                return -1

            return max(left, right) + 1

        return height(root) != -1
Neden Doğru?
Her düğüm yalnızca bir kez ziyaret edilir

Bir alt ağaç dengesizse:

Daha yukarı çıkmaya gerek kalmadan işlem kesilir

Böylece:

Gereksiz hesaplamalar önlenir

En kötü durumda bile lineer çalışır

Zaman ve Alan Karmaşıklığı
Zaman: O(n)

Her düğüm 1 kez ziyaret edilir

Alan: O(h)

Recursive stack

En kötü durumda h = n (skewed tree)