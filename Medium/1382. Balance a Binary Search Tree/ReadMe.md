# 1382. Balance a Binary Search Tree

**Difficulty:** Medium  
**Link:** [LeetCode 1382](https://leetcode.com/problems/balance-a-binary-search-tree/description/)

---

## Problem Özeti

Verilen bir **Binary Search Tree (BST)** dengesiz olabilir.  
Ama BST özelliği her zaman geçerlidir:

- Inorder traversal → **sıralı (sorted) dizi** verir.

Amaç:
- Aynı değerleri kullanarak
- **Height-balanced** bir BST oluşturmak.

---

## Temel Fikir

Bu problem iki çok net adıma ayrılır:

### 1️⃣ BST → Sorted Array
- BST’nin inorder traversal’ı yapılır
- Tüm değerler **artan sırada** bir diziye alınır

### 2️⃣ Sorted Array → Balanced BST
- Ortadaki eleman kök seçilir
- Sol yarı → sol alt ağaç
- Sağ yarı → sağ alt ağaç
- Bu işlem **rekürsif** devam eder

Bu yöntem, klasik:
> **“Sorted array → balanced BST”** yaklaşımıdır.

---

## Neden Bu Çalışır?

- BST’nin inorder çıktısı zaten sorted
- Sorted diziden ortayı kök seçmek:
  - Ağacın yüksekliğini minimum yapar
- Sol ve sağ alt ağaçlar **dengeyi otomatik korur**

---

## Kod

```python
class Solution(object):
    def balanceBST(self, root):
        # Step 1: Inorder traversal to get sorted values
        values = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            values.append(node.val)
            inorder(node.right)

        inorder(root)

        # Step 2: Build balanced BST from sorted array
        def build(l, r):
            if l > r:
                return None

            mid = (l + r) // 2
            node = TreeNode(values[mid])
            node.left = build(l, mid - 1)
            node.right = build(mid + 1, r)
            return node

        return build(0, len(values) - 1)
Örnek Akış
BST:

    1
     \
      2
       \
        3
         \
          4
Inorder sonucu:

[1, 2, 3, 4]
Balanced BST:

      2
     / \
    1   3
         \
          4
Zaman ve Alan Karmaşıklığı
Zaman: O(n)

Inorder traversal → O(n)

Tree rebuild → O(n)

Alan: O(n)

Değerleri tutan array

Recursive stack